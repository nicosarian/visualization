# Visualization 1 — Visits per Square Foot (Busiest Branches by Space Efficiency)

**Dataset:** City of Toronto Open Data Portal — Toronto Public Library
- Branch General Information: https://open.toronto.ca/dataset/library-branch-general-information/
- Visits: https://open.toronto.ca/dataset/library-visits/

![Visits per square foot](figures/viz1_visits_per_sqft.png)

---

> *Answer each question below in your own voice. Prompts in italics are scaffolding — replace them. Keep the combined word count across both files under 1000.*

**What software did you use to create your data visualization?**

Python (matplotlib, pandas), data fetched live via the City of Toronto CKAN API. *[Add a sentence on why Python — reproducibility, the live API pull, etc.]*

**Who is your intended audience?**

*[Who benefits from a space-efficiency ranking? e.g. TPL facilities/planning staff, library board members deciding on branch investment, civic-minded residents. Pick one primary audience and commit to it — your design choices below should follow from who they are.]*

**What information or message are you trying to convey?**

*[The message is roughly: raw visit counts hide that small branches can be intensely used per square foot. State what you want the viewer to take away. Tie to "use data viz to tell a story."]*

**What aspects of design did you consider? How did you apply them? With what elements?**

*[Concrete elements to discuss — make these your own observations:]*
- *Horizontal bars chosen because branch names are long text labels (legibility).*
- *Single colour rather than a rainbow palette — colour is not encoding a variable here, so multiple colours would be decorative chartjunk (Tufte, data-ink ratio).*
- *Direct value labels on each bar so the reader doesn't interpolate against gridlines.*
- *Removed top/right spines to raise the data-ink ratio.*
- *[Cite: Tufte, *The Visual Display of Quantitative Information*; or your deck on design principles.]*

**How did you ensure your visualization is reproducible? If your tool is not reproducible, how does that impact it?**

*[The pipeline pulls live from CKAN by dataset slug, all transforms are commented code, figure exported at 300 dpi from code. Note the versioning caveat: the City refreshes the data, so record your run date and the year used.]*

**How did you ensure your visualization is accessible?**

*[Discuss: single high-contrast colour (#2c7fb8 on white), text labels rather than colour-only encoding (works for colour-blind readers and greyscale printing), readable font sizes, descriptive title. What would you still improve — alt text? WCAG contrast check?]*

**Who are the individuals and communities who might be impacted?**

*[Branch-level usage framing can influence funding/closure decisions. A small branch that looks "low traffic" in raw counts but is space-efficient here serves a real neighbourhood. Who is helped or harmed if this chart informs a budget conversation? This is the equity question — engage it seriously.]*

**How did you choose which features to include or exclude?**

*[You used branch name, square footage, and visits; you excluded ward, workstations, address, etc. Why? You also showed only the top 15 — what does truncating the ranking hide, and why was it a defensible choice?]*

**What 'underwater labour' contributed to your final product?**

*[The unseen work: TPL staff and door sensors recording visits during operating hours; facilities staff measuring square footage; Open Data staff cleaning, formatting, and maintaining the CKAN datastore; your own cleaning/merging decisions. Name the labour that doesn't show up in the final image.]*
