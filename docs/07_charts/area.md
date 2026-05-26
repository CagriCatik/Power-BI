# Area Graphs

## Overview

An **area chart** is a line chart where the region between the line and the axis is filled with color. It emphasises the **magnitude** of a value over time, not just the direction. **Stacked area charts** show part-to-whole composition over time, making them useful for comparing how multiple series contribute to a total.

> **Reference:** [Line Charts in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-line-chart)

---

## Area Chart Variants

| Chart | Description | Best for |
| --- | --- | --- |
| **Area** | Single filled line | One series, magnitude over time |
| **Stacked area** | Multiple filled areas stacked | Part-to-whole over time |
| **100% stacked area** | All areas normalised to 100% | Proportional composition over time |

---

## Building an Area Chart

1. In the **Visualizations pane**, click the **Area chart** icon.
2. Assign:
   * **X-axis** — a date or ordered category column.
   * **Y-axis** — a numeric measure (e.g., Monthly Revenue).
   * **Legend** (optional) — a dimension for a stacked area chart.
3. The fill color appears automatically below the line.

---

## Stacked Area Chart

Add a field to the **Legend** well to convert a simple area chart into a stacked area chart. Each series is stacked on top of the previous, and the full height of the stacked area represents the total.

### When to use stacked area

* Showing cumulative totals with visible contribution from each component.
* Tracking how the mix of series changes while the total grows or shrinks.

### Limitation

Individual series in the middle of the stack are hard to compare precisely because their baseline shifts. If accurate comparison of individual series matters, use a stacked column chart or separate line charts instead.

---

## 100% Stacked Area Chart

All series are normalised so the total height always equals 100%. This makes proportional composition visible even when absolute values vary greatly.

Use this when the **relative contribution** of each series is the key question, not the absolute magnitude.

---

## Formatting Area Charts

### Fill Color and Transparency

Under **Format visual › Lines**:

* **Color** — set the line color.
* **Transparency** — reduce opacity to 20–40% for overlapping fills to remain visible.

### Markers

Under **Format visual › Markers**:

* Toggle markers (dots) on each data point.
* Useful when data points are sparse (monthly or quarterly).

### Smooth Lines

Under **Format visual › Lines**:

* Toggle **Stepped** on for a step-chart style (useful for data that changes at discrete points).
* Leave off for smooth interpolated curves.

### Shaded Area

Unlike line charts, area charts always show a fill. The transparency setting controls how much of the background shows through — important when multiple series overlap.

---

## Analytics Pane Support

Area charts support a subset of Analytics pane features:

| Feature | Supported |
| --- | --- |
| Trend line | Yes (basic area only) |
| Forecast | Yes (basic area only) |
| Anomaly detection | Yes (basic area only) |
| Reference lines | Yes |

Stacked and 100% stacked area charts do **not** support forecasting or trend lines — they require a single-series, continuous-axis chart.

---

## Area Chart vs Line Chart

| Feature | Line chart | Area chart |
| --- | --- | --- |
| Emphasises trend | Yes | Yes |
| Emphasises magnitude | Slightly | Strongly |
| Part-to-whole (stacked) | No | Yes |
| Forecasting | Yes | Yes (single series) |
| Readability with many series | Better | Worse (overlapping fills) |

---

## Best Practices

* Use **low transparency** (20–40%) for stacked areas so overlapping segments remain distinguishable.
* Limit to **3–4 series** in a stacked area chart — more series create illegible overlapping fills.
* Use **markers** on sparse data (monthly, quarterly) to make individual data points identifiable.
* Prefer **stacked column charts** over stacked area charts when precise segment comparison is needed.
* Use area charts when you want to visually communicate **volume** or **accumulation** — they read as "filling up" to a total.

---

## References

* [Line Charts in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-line-chart)
* [Use the Analytics pane in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-analytics-pane)
* [Overview of visualizations in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualizations-overview)
