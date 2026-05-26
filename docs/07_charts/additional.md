# Additional Graph Types

## Overview

Beyond columns, bars, and area charts, Power BI includes a range of specialised chart types for specific analytical needs — scatter plots for correlation, pie/donut for simple composition, waterfall for variance analysis, funnel for pipeline analysis, and ribbon charts for rank changes over time.

> **Reference:** [Overview of visualizations in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualizations-overview)

---

## Scatter Chart

A scatter chart plots two numeric measures on the X and Y axes, revealing correlation between them. A third measure can encode bubble size (bubble chart variant).

| Well | Field |
| --- | --- |
| **X-axis** | First numeric measure |
| **Y-axis** | Second numeric measure |
| **Values** | The entity being plotted (e.g., Product, Customer) |
| **Size** | Third measure for bubble size (optional) |
| **Legend** | Category for color grouping |
| **Play axis** | Date field for animated time playback |

### Use cases

* Revenue vs Profit Margin per product — identify high-margin outliers.
* Customer spend vs Frequency — segment customers by value.
* Risk vs Return per investment — classic portfolio analysis.

A **trend line** can be added from the Analytics pane to show the overall correlation direction.

### Scatter Chart Use Cases

* Revenue vs Profit Margin per product — identify high-margin outliers.
* Customer spend vs Frequency — segment customers by value.
* Risk vs Return per investment — classic portfolio analysis.

---

## Pie and Donut Charts

Pie and donut charts show part-to-whole composition for a **single time point or filter context**. Each slice represents a category's share of the total.

| Well | Field |
| --- | --- |
| **Legend** | The category dimension |
| **Values** | The numeric measure |

### Donut vs Pie

A donut chart has a hollow centre that can display a total value label — making it slightly more informative than a pie chart. Both are limited to the same data structure.

### Limitations

* Hard to compare slice sizes when values are close (e.g., 24% vs 26%).
* Avoid using when you have more than 5–6 slices — use a bar chart instead.
* Do not use for comparing the same category across multiple time periods.

---

## Waterfall Chart

A waterfall chart (also called a bridge chart) shows how an initial value increases or decreases through a series of positive and negative contributions to reach a final value.

| Well | Field |
| --- | --- |
| **Category** | The steps/drivers (e.g., months, cost components) |
| **Y-axis** | The numeric change value |
| **Breakdown** | Optional sub-category for each bar |

### Waterfall Use Cases

* Budget variance analysis: actual vs plan, showing which factors drove the difference.
* Profit bridge: revenue → minus COGS → minus operating expenses → = net profit.
* Monthly cash flow: opening balance + inflows − outflows = closing balance.

---

## Funnel Chart

A funnel chart shows values progressing through sequential stages, typically decreasing at each step — common for sales pipelines and conversion analysis.

| Well | Field |
| --- | --- |
| **Category** | The stage names (e.g., Leads → Qualified → Proposal → Closed) |
| **Values** | The numeric count or value at each stage |

The chart draws proportional horizontal bars from widest (top stage) to narrowest (final stage), visually representing the drop-off at each step.

### Funnel Use Cases

* Sales pipeline conversion rates.
* Website conversion: visitors → sign-ups → purchases.
* Support ticket resolution stages.

---

## Ribbon Chart

A ribbon chart shows how rankings change over time. Each series is rendered as a "ribbon" that moves up or down as its rank position changes across time periods.

| Well | Field |
| --- | --- |
| **X-axis** | Time dimension |
| **Y-axis** | Numeric measure |
| **Legend** | The series/category being ranked |

> **Reference:** [Use Ribbon Charts in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/desktop-ribbon-charts)

### Ribbon Chart Use Cases

* Product ranking changes by month.
* Regional revenue rankings over quarters.
* Employee performance ranking changes.

---

## Treemap

A treemap shows hierarchical composition using nested rectangles. The area of each rectangle is proportional to its value.

| Well | Field |
| --- | --- |
| **Category** | The grouping dimension |
| **Values** | The numeric measure determining rectangle size |
| **Details** | Optional sub-category for nested rectangles |

Use when you want to show part-to-whole with **more categories** than a pie chart can handle readably.

---

## Choosing Between Additional Charts

| Question | Best chart |
| --- | --- |
| Are two measures correlated? | Scatter chart |
| What is each category's share? | Pie / donut (≤6 slices), treemap (many) |
| How does a value change through steps? | Waterfall chart |
| How do stages reduce in a pipeline? | Funnel chart |
| How do rankings shift over time? | Ribbon chart |

---

## References

* [Overview of visualizations in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualizations-overview)
* [Use Ribbon Charts in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/desktop-ribbon-charts)
* [Create and use combo charts in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-combo-chart)
