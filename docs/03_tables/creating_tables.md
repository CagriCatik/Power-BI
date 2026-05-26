# Creating Tables in Power BI

## Overview

A **table visual** displays data in a rows-and-columns grid — the simplest way to present detail-level data, multi-column comparisons, or aggregated summaries. Power BI tables support rich formatting, conditional rules, and interactive cross-filtering.

> **Reference:** [Create and Format Table Visualizations in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-tables)

---

## Step 1 — Add a Table Visual

1. Open a report page in **Report View**.
2. Click an empty area of the canvas (deselect any existing visual).
3. In the **Visualizations pane**, click the **Table** icon (grid with rows and columns).
4. An empty table placeholder appears on the canvas.

Alternatively, select fields first in the Fields pane — Power BI will auto-choose a visual type, often a table for multi-field selections.

---

## Step 2 — Add Fields

With the table selected, drag columns from the **Fields pane** into the **Columns** well (inside the Visualizations pane), or simply click a field checkbox to add it.

**Recommended field order:**

1. **Dimension** columns first (text, categories, dates) — these group rows.
2. **Measure or numeric** columns after — these aggregate the values.

Example layout:

| Product | Category | Region | Total Sales | Units Sold |
| --- | --- | --- | --- | --- |
| Widget A | Hardware | North | 12,450 | 312 |
| Widget B | Software | South | 8,900 | 89 |

---

## Step 3 — Resize and Reorder Columns

* **Resize:** Hover over a column border in the table header until the cursor changes, then drag.
* **Reorder:** Drag column names within the **Columns** well in the Visualizations pane.
* **Remove:** Click the **×** next to a field in the Columns well.

---

## Step 4 — Sort the Table

* Click any **column header** to sort ascending; click again for descending.
* A small arrow indicator shows the current sort direction.
* To sort by a field not shown in the table, use the **Sort by column** feature in the Modeling tab.

---

## Step 5 — Resize the Visual on Canvas

* Drag the handles at the corners and edges of the visual frame.
* Hold **Shift** while resizing to maintain aspect ratio.
* Use **View › Align** and **View › Distribute** to precisely position multiple visuals.

---

## Totals Row

Power BI automatically adds a **Total** row at the bottom of tables for numeric columns.

* **Show totals:** Format pane › **Totals** › toggle on/off.
* Totals use the same aggregation as the column (e.g., Sum of Sales, Count of Orders).
* For measures, the total reflects the measure evaluated over the entire visible data.

> **Note:** The total row for a measure is **not** necessarily the sum of visible row values — it evaluates the DAX expression at the full filter context.

---

## Column Aggregation Behaviour

When you add a numeric column (not a measure) to a table, Power BI defaults to **Sum**. You can change this per-column:

1. Right-click the field in the **Columns** well.
2. Hover over **Summarize** (or the aggregation name shown).
3. Choose: Sum, Average, Minimum, Maximum, Count, Count (Distinct), Standard Deviation, Variance, Median, or **Don't summarize**.

> **Reference:** [Change How a Visual Aggregates Data – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/service-aggregates)

---

## Best Practices

* Keep tables to **5–8 columns** maximum for readability.
* Place tables on a **detail page** accessed via drill-through, rather than cluttering summary dashboards.
* Use **measures** instead of raw numeric columns for calculated aggregations — this gives you full DAX control.
* Enable **Autofit column width** (Format pane) so column widths adjust to content automatically.

---

## References

* [Create and Format Table Visualizations – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-tables)
* [Overview of visualizations in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualizations-overview)
