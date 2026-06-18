# Visualization 2 — Branch Size vs. Annual Visits (Relationship Scatter)

**Dataset:** City of Toronto Open Data Portal — Toronto Public Library
- Branch General Information: https://open.toronto.ca/dataset/library-branch-general-information/
- Visits: https://open.toronto.ca/dataset/library-visits/

![Size vs visits](figures/viz2_size_vs_visits.png)

---

> *Answer in your own voice. This visualization is deliberately a different type (scatter + trend) and answers a different question than Viz 1, satisfying the "distinct from each other" requirement.*

**What software did you use?**

Python (matplotlib, pandas), live CKAN API fetch. *[Same stack as Viz 1 — you can note the consistency aids reproducibility.]*

**Who is your intended audience?**

*[Could be the same audience as Viz 1 or a different one — e.g. a more analytical reader testing the assumption "bigger branches are busier." Be explicit.]*

**What information or message are you trying to convey?**

*[The scatter + trend line tests whether square footage predicts visits. The correlation in the sample is weak-to-moderate — the message is that size alone doesn't explain usage; location/community matter. State your takeaway.]*

**What aspects of design did you consider? How did you apply them?**

- *Scatter chosen because the question is about the relationship between two continuous variables — the correct encoding.*
- *Trend line summarizes direction/strength without overstating it; slope reported in the legend.*
- *Thousands separators on both axes for readability.*
- *Point transparency (alpha) so overlapping branches remain visible.*
- *[Cite a source on choosing chart types to match data relationships.]*

**How did you ensure reproducibility?**

*[Same live-fetch pipeline; commented code; 300 dpi export. The correlation coefficient is printed so the claim in your write-up is traceable to the code.]*

**How did you ensure accessibility?**

*[High-contrast points, trend line distinguished by both colour AND being a line (redundant encoding), labelled axes, plain-language title. Note improvements: alt text, a colour-blind-safe check of the blue/orange pairing.]*

**Who are the individuals and communities who might be impacted?**

*[If "size doesn't predict visits" enters a planning conversation, it could protect smaller neighbourhood branches from being judged purely on footprint — or be misused. Engage the equity dimension.]*

**How did you choose which features to include or exclude?**

*[Two continuous variables plus an inner join that drops branches present in one dataset but not the other. What gets silently excluded by the join, and does that bias the picture?]*

**What 'underwater labour' contributed?**

*[Same chain as Viz 1 — sensor counts, facilities measurement, Open Data maintenance — plus the analytical judgement in fitting and interpreting a trend line responsibly rather than overclaiming causation.]*
