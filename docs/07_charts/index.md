# Graph Visualizations — Section Introduction

## Overview

Charts and graphs are the visual language of business intelligence. Power BI provides a rich library of chart types — each suited to a different type of comparison, composition, distribution, or trend analysis question. This section covers the most widely used chart families and their configuration options.

> **Reference:** [Overview of visualizations in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualizations-overview)

---

## Choosing the Right Chart

| Question you are answering | Recommended chart type |
| --- | --- |
| How do categories compare? | Clustered bar / column chart |
| What is each part's share of the whole? | Stacked bar, 100% stacked bar, pie, donut |
| How has a value changed over time? | Line chart, area chart |
| How do two measures relate? | Scatter chart, combo chart |
| How does a metric compare to a target? | KPI visual, bullet chart (custom) |
| What is the distribution of values? | Histogram, box plot (custom) |
| How do values flow between states? | Funnel chart, waterfall chart |
| What trends and forecasts exist? | Line chart with Analytics pane |

---

## Chart Types Covered in This Section

| File | Topic |
| --- | --- |
| `07_clustered_column_graphs.md` | Clustered column and bar charts |
| `07_stacked_graphs.md` | Stacked and 100% stacked charts |
| `07_column_graph_challenge.md` | Practice challenge |
| `07_column_graph_completed.md` | Challenge solution |
| `07_graph_options.md` | Common formatting options |
| `07_reference_lines.md` | Constant, min/max, and average lines |
| `07_trend_analysis_graphs.md` | Trend lines and smoothing |
| `07_trends_forecasting.md` | Forecasting with the Analytics pane |
| `07_area_graphs.md` | Area and stacked area charts |
| `07_additional_graphs.md` | Line, scatter, pie, donut, waterfall |

---

## The Visualizations Pane — Build Tab

Every chart is configured through the three tabs of the **Visualizations pane**:

* **Build visual** — assign fields to axis wells, legend, values, tooltips, and small multiples.
* **Format visual** — set colors, titles, axes, gridlines, data labels, and legends.
* **Analytics** — add reference lines, trend lines, forecasts, and anomaly detection.

---

## Anatomy of a Chart Visual

| Component | Purpose |
| --- | --- |
| **X-axis (Category axis)** | Grouping dimension — usually a category or time period |
| **Y-axis (Value axis)** | The numeric scale |
| **Legend** | Color-codes a second dimension (series grouping) |
| **Values** | The measure(s) to plot |
| **Tooltips** | Additional fields shown on hover |
| **Small multiples** | Repeats the chart for each value of a dimension |

---

## Prerequisites

Before starting this section you should be comfortable with:

* Adding and resizing visuals on the canvas.
* Using the Fields pane to assign dimensions and measures.
* Basic formatting (titles, font sizes, background colors).
* The concept of cross-filtering and slicers.

---

## References

* [Overview of visualizations in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualizations-overview)
* [Create and use column charts in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-column-charts)
* [Use the Analytics pane in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-analytics-pane)
