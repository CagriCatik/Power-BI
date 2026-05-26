# Clustered Column and Bar Charts

## Overview

**Clustered column charts** (vertical bars) and **clustered bar charts** (horizontal bars) are the workhorses of comparative analysis. They place bars side-by-side to compare a measure across categories, or to compare multiple measures for the same category.

> **Reference:** [Create and use column charts in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-column-charts)

---

## Column Chart vs Bar Chart

| Chart type | Bar orientation | Best for |
| --- | --- | --- |
| **Clustered column** | Vertical | Comparing categories over time (X-axis = time) |
| **Clustered bar** | Horizontal | Comparing long category names; ranking |

The data is identical — only the orientation changes. Use horizontal bars when category labels are long, since they read left-to-right naturally without rotation.

---

## Building a Clustered Column Chart

1. In the **Visualizations pane**, click the **Clustered column chart** icon.
2. Assign fields:
   * **X-axis** — a category or date (e.g., Month, Product Category)
   * **Y-axis** — a numeric measure (e.g., Total Sales)
   * **Legend** (optional) — a second dimension to create clustered groups (e.g., Region)
3. Resize the visual on the canvas.

When a **Legend** field is added, each X-axis value gets multiple side-by-side bars, one per legend value — this is the "clustered" behavior.

---

## Adding a Second Measure (Combo)

To compare two measures with different scales (e.g., Revenue and Units), use a **Line and clustered column chart** (combo chart):

1. Select the **Line and clustered column chart** icon.
2. Assign one measure to **Column y-axis** and another to **Line y-axis**.
3. The Y-axis splits into a left (column) and right (line) scale.

> **Reference:** [Create and use combo charts in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-combo-chart)

---

## Formatting Options

### Colors

Under **Format visual › Columns** (or **Bars**):

* **Default color** — the fill color applied to all bars.
* **Show all** — assign a distinct color to each category individually.
* **Conditional formatting (fx)** — color bars based on measure values or rules.

### Data Labels

Under **Format visual › Data labels**:

* Toggle on to show the value above each bar.
* Set display units (none, K, M) and decimal places.
* Adjust font, size, and color.

### Column/Bar Spacing

Under **Format visual › Columns** (or **Bars**):

* **Inner padding** — space between bars within a cluster.
* **Category spacing** — space between each cluster of bars.

Reduce these values when you have many categories to fit more bars on screen.

### X-Axis and Y-Axis

Under **Format visual › X-axis** and **Y-axis**:

* Toggle axis labels and titles on or off.
* Set axis range (min/max) for the Y-axis to zoom in on a specific value range.
* Rotate X-axis labels (0°, 45°, 90°) when category names are long.
* Enable/disable gridlines under **Format visual › Gridlines**.

> **Reference:** [Customize X-Axis and Y-Axis Properties – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-customize-x-axis-and-y-axis)

---

## Sorting

* Click the **ellipsis (…)** in the visual header.
* Select **Sort axis** → choose the field to sort by and the direction (ascending/descending).
* Common: sort by the measure value (Sales) descending to show a ranking chart.

---

## Small Multiples

Add a field to the **Small multiples** well to repeat the chart for each value of that field — for example, one column chart per Region. This is a powerful way to compare patterns across groups without overlapping the data.

> **Reference:** [Create Small Multiples in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-small-multiples)

---

## Best Practices

* Start the Y-axis at **zero** — truncating the axis exaggerates differences and misleads viewers.
* Limit clusters to **2–3 series** in the Legend field; more series makes the chart hard to read.
* Use **horizontal bar charts** for rankings (sorted descending) — they are easier to compare than vertical charts with many narrow bars.
* Add **data labels** only when exact values are important; otherwise the bar height conveys the relative comparison.
* Use **conditional color** to highlight bars above/below a target threshold.

---

## References

* [Create and use column charts in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-column-charts)
* [Create and use combo charts in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-combo-chart)
* [Customize X-Axis and Y-Axis Properties – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-customize-x-axis-and-y-axis)
* [Create Small Multiples in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-small-multiples)
