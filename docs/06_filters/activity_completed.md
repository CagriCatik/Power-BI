# Practical Activity Filters — Completed

## Overview

This page provides the expected outcomes and explanations for the Filters Practical Activity.

---

## Part A — Visual-Level Filters

### Task A1 — Top 5 Products

The **Top N filter** is one of the most practical visual-level features in Power BI. Rather than manually selecting 5 products, the filter dynamically recalculates every time the data changes or a slicer is applied — always showing the current top 5, not a fixed list.

If you apply a Region slicer after this, the chart will show the Top 5 products **within that region** — the Top N filter re-evaluates in the current filter context.

### Task A2 — Advanced Text Filter

The "does not contain" condition uses a substring match. Setting Category **does not contain** "Misc" removes rows like "Miscellaneous", "Misc Hardware", or simply "Misc".

If you needed to exclude multiple keywords, add a second condition with **And** or create separate filter entries.

---

## Part B — Page-Level Filter

### Task B1 — Current Year Lock

The **Relative date** filter "In this Calendar year" uses today's date at runtime to determine the year boundary. On 1 January, it automatically resets to the new year — the report does not need to be updated.

Using the **lock icon** prevents consumers from changing or removing the filter. If they open the Filters pane, they can see the filter exists but cannot modify it. The padlock icon is a report design control, not a security boundary — use Row-Level Security for true access control.

---

## Part C — Report-Level Filter

### Task C1 — Inactive Product Filter

Hiding and locking the report-level filter means:

* Consumers see clean, active-only data without knowing a filter exists.
* The report behaves as if inactive products were never imported.
* If you need to audit or change the filter, switch back to **Edit mode** in Power BI Desktop.

This pattern is common in production reports where the underlying data contains historical or archived records that should not appear in operational dashboards.

---

## Part D — Slicers

### Task D1 — Sync Slicers

After syncing the Region slicer across both pages, the **Sync slicers pane** shows:

| Page | Sync | Visible |
| --- | --- | --- |
| Page 1 — Sales Overview | On | On |
| Page 2 — Product Detail | On | Off (or On) |

Setting **Sync = On** means the slicer's selection applies to visuals on that page. Setting **Visible = On** means the slicer widget itself appears on that page. You can sync a slicer to a page without showing it there — the filter applies silently.

### Task D2 & D3 — Stacked Filters

When consumers use the date slicer, the numeric slicer, and the synced region slicer simultaneously on Page 2, all three filters stack. The visible data satisfies:

* Region = `<selected region>`
* OrderDate **between** `<selected start>` and `<selected end>`
* Sales **between** `<selected min>` and `<selected max>`

And on top of those — the report-level Status = Active filter also applies. Five filter layers are active simultaneously, all contributing to the final result.

---

## Filter Precedence Summary

| Layer | Scope | Consumer can change |
| --- | --- | --- |
| Report filter (Status = Active) | All pages | No (locked + hidden) |
| Page filter (Current year) | Page 1 only | No (locked) |
| Visual filter (Top 5) | Bar chart only | No |
| Slicer (Region) | Both pages | Yes |
| Slicer (Date, Sales) | Page 2 only | Yes |

---

## References

* [Add a Filter to a Report in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-report-add-filter)
* [Slicers in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-slicers)
* [How visuals cross-filter each other – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/explore-reports/end-user-interactions)
