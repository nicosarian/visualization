"""
Assignment 3 — Final Project: Toronto Public Library Data Visualizations
Code appendix (mirrors final_project.ipynb).

Dataset: City of Toronto Open Data Portal — Toronto Public Library
  - Branch General Information:
    https://open.toronto.ca/dataset/library-branch-general-information/
  - Visits:
    https://open.toronto.ca/dataset/library-visits/

Data is fetched LIVE from the City of Toronto CKAN API for reproducibility.
Run on a machine with internet access. Produces two 300-dpi PNGs in ./figures.

Note: the two datasets share a BRANCHCODE key (the visits table has no branch
name), so they are joined on branchcode and the branch name is pulled across
for readable plot labels.
"""

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from pathlib import Path

OUT = Path("figures")
OUT.mkdir(exist_ok=True)
CKAN = "https://ckan0.cf.opendata.inter.prod-toronto.ca"


def get_ckan_records(package_id, ckan=CKAN, max_records=100000):
    """Return a DataFrame of all records from the first active datastore
    resource in a CKAN package."""
    pkg = requests.get(f"{ckan}/api/3/action/package_show",
                       params={"id": package_id}, timeout=60).json()
    resources = pkg["result"]["resources"]
    ds = next((r for r in resources if r.get("datastore_active")), None)
    if ds is None:
        raise RuntimeError(f"No active datastore resource in '{package_id}'.")
    rows, offset, page = [], 0, 32000
    while True:
        resp = requests.get(f"{ckan}/api/3/action/datastore_search",
                            params={"id": ds["id"], "limit": page, "offset": offset},
                            timeout=60).json()
        recs = resp["result"]["records"]
        rows.extend(recs)
        if len(recs) < page or len(rows) >= max_records:
            break
        offset += page
    return pd.DataFrame(rows)


def snake(df):
    """Normalize column names to lowercase_snake_case."""
    df = df.copy()
    df.columns = (df.columns.str.strip()
                  .str.replace(r"[ \-]+", "_", regex=True).str.lower())
    return df


def find_col(df, *keywords):
    """Find a column whose name contains all given keywords."""
    for c in df.columns:
        if all(k in c for k in keywords):
            return c
    raise KeyError(f"No column matching {keywords} in {list(df.columns)}")


def main():
    # 1. Fetch live
    branches = snake(get_ckan_records("library-branch-general-information"))
    visits = snake(get_ckan_records("library-visits"))

    # 2. Resolve columns. The two tables join on BRANCHCODE; the visits table
    #    has no branch name, so we also keep branchname from the branch table.
    b_name = find_col(branches, "branchname")     # readable label for plots
    b_code = find_col(branches, "branchcode")     # join key
    b_sqft = find_col(branches, "square")         # square footage
    v_code = find_col(visits, "branchcode")       # join key
    v_year = find_col(visits, "year")
    v_visit = find_col(visits, "visit")

    branches[b_sqft] = pd.to_numeric(branches[b_sqft], errors="coerce")
    visits[v_visit] = pd.to_numeric(visits[v_visit], errors="coerce")
    visits[v_year] = pd.to_numeric(visits[v_year], errors="coerce")

    # 3. Most recent year, then merge visits onto branch attributes by branchcode
    latest_year = int(visits[v_year].max())
    vl = visits[visits[v_year] == latest_year][[v_code, v_visit]].dropna()
    merged = vl.merge(branches[[b_code, b_name, b_sqft]],
                      on=b_code, how="inner").dropna(subset=[b_sqft, v_visit])

    # 4. Viz 1 — visits per square foot, top 15
    m1 = merged[merged[b_sqft] > 0].copy()
    m1["visits_per_sqft"] = m1[v_visit] / m1[b_sqft]
    top = m1.sort_values("visits_per_sqft", ascending=False).head(15).iloc[::-1]

    fig, ax = plt.subplots(figsize=(9, 7))
    bars = ax.barh(top[b_name], top["visits_per_sqft"], color="#2c7fb8")
    ax.set_xlabel("Visits per square foot (annual)")
    ax.set_title(f"Toronto Public Library: Busiest Branches by Space Efficiency "
                 f"({latest_year})", fontsize=13, weight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    for bar in bars:
        ax.text(bar.get_width(), bar.get_y() + bar.get_height() / 2,
                f" {bar.get_width():.1f}", va="center", fontsize=9)
    fig.tight_layout()
    fig.savefig(OUT / "viz1_visits_per_sqft.png", dpi=300, bbox_inches="tight")

    # 5. Viz 2 — size vs visits scatter + trend
    m2 = merged[(merged[b_sqft] > 0) & (merged[v_visit] > 0)].copy()
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.scatter(m2[b_sqft], m2[v_visit], s=45, alpha=0.7,
               color="#2c7fb8", edgecolor="white", linewidth=0.5)
    x, y = m2[b_sqft].values, m2[v_visit].values
    coef = np.polyfit(x, y, 1)
    xs = np.linspace(x.min(), x.max(), 100)
    ax.plot(xs, np.polyval(coef, xs), color="#d95f0e", linewidth=2,
            label=f"Trend (slope = {coef[0]:.1f} visits/sq ft)")
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{int(v):,}"))
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{int(v):,}"))
    ax.set_xlabel("Branch size (square feet)")
    ax.set_ylabel(f"Annual visits ({latest_year})")
    ax.set_title("Toronto Public Library: Branch Size vs. Annual Visits",
                 fontsize=13, weight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(OUT / "viz2_size_vs_visits.png", dpi=300, bbox_inches="tight")

    print(f"Done. Latest year={latest_year}, branches matched={len(merged)}, "
          f"r={np.corrcoef(x, y)[0,1]:.3f}")


if __name__ == "__main__":
    main()
