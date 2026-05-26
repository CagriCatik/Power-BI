# Stacked and 100% Stacked Charts

## Overview

**Stacked charts** extend column and bar charts by breaking each bar into segments — one per series value. They reveal both the total magnitude and the part-to-whole composition in a single visual. The **100% stacked** variant normalizes all bars to the same height, making proportional comparisons the focus rather than absolute values.

> **Reference:** [Create and use column charts in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-column-charts)

---

## Chart Variants

| Chart | Icon name | Bar | Shows |
| --- | --- | --- | --- |
| **Stacked column** | Stacked column chart | Vertical | Total + composition by absolute value |
| **Stacked bar** | Stacked bar chart | Horizontal | Total + composition (horizontal) |
| **100% stacked column** | 100% stacked column | Vertical | Proportional composition (all bars = 100%) |
| **100% stacked bar** | 100% stacked bar | Horizontal | Proportional composition (horizontal) |

---

## Building a Stacked Column Chart

1. Select the **Stacked column chart** icon in the Visualizations pane.
2. Assign:
   * **X-axis** — category or time period (e.g., Quarter)
   * **Y-axis** — numeric measure (e.g., Sales)
   * **Legend** — the dimension to stack by (e.g., Product Category)
3. Each bar now stacks one segment per category.

The total bar height represents the grand total for that X-axis value; each segment represents one category's contribution.

---

## When to Use Each Variant

### Stacked Column / Bar

* Use when **absolute totals matter** and you also want to see composition.
* Example: Total monthly revenue stacked by product category — shows both the monthly revenue trend and which categories drive it.

### 100% Stacked Column / Bar

* Use when **proportions matter more than absolute values**.
* Example: Market share by region over time — each bar is 100%, and the segments show relative share.
* Limitation: you cannot read absolute values, only percentages.

---

## Formatting Stacked Charts

### Stacked Colors

Each legend value gets its own color. To customize:

1. Under **Format visual › Columns**, click **Show all colors**.
2. Assign specific colors to each series.

For brand consistency, set all series colors explicitly rather than relying on the default theme palette.

### Data Labels

Under **Format visual › Data labels**:

* **Position**: Center (inside segment), Outside end.
* Show labels only for large segments — small segments get cluttered.
* Set display units to **%** for 100% stacked charts to show each segment's percentage.

### Totals (Stacked Column)

Under **Format visual › Total labels**, toggle on a label above each full bar showing the grand total value. This adds the total height information back to a stacked chart where the segments alone don't show the total.

---

## 100% Stacked — Key Differences

* The **Y-axis** scale is 0–100%.
* Data labels in the segments naturally show percentages.
* **No Y-axis total label** — every bar ends at 100% by definition.
* You cannot tell from the chart alone whether one period's total volume was larger than another — use a regular stacked chart for that.

---

## Limitations

* **Hard to compare segments** that are not at the bottom of the stack — the segment baselines shift, making it difficult to judge their individual sizes. Use a clustered chart if precise comparison of mid-stack series is important.
* **Many legend values** create too many thin segments — limit to 4–5 series for readability.
* **Avoid stacked line charts** (stacked area) for showing composition — the area chart section covers these.

---

## Practical Example

Revenue by quarter, stacked by product category:

* X-axis: Quarter (Q1, Q2, Q3, Q4)
* Y-axis: Sales Amount
* Legend: Product Category (Electronics, Apparel, Food, Other)

Each bar shows the quarterly total broken down by category. The trend of the full bar height shows revenue growth; the segment sizes show which category contributed more or less each quarter.

---

## Best Practices

* Use **100% stacked** when comparing proportions across groups of different total sizes (e.g., comparing 5 regions with very different revenues).
* Use **regular stacked** when the total magnitude is also meaningful.
* Always add a **legend** with clear labels — without a legend, stacked colors are meaningless.
* Apply **consistent color conventions** (e.g., always blue for Electronics, green for Apparel) across all visuals in the report.

---

## References

* [Create and use column charts in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-column-charts)
* [Overview of visualizations in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualizations-overview)
* [Get Started Formatting Report Visualizations – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/service-getting-started-with-color-formatting-and-axis-properties)
