# Column Graph Challenge

## Objective

Apply your knowledge of clustered and stacked column charts to build a complete, formatted comparison page from scratch. This challenge tests your ability to choose the right chart type, configure fields, format for clarity, and add interactivity.

---

## Dataset Requirements

Use the training dataset loaded in Power BI Desktop. You need at least:

* A **Category** or **Product** dimension.
* A **Region** or **Segment** dimension (for the Legend field).
* A **Date** column (for time-based X-axis).
* A **Sales** or **Revenue** measure.
* A **Units** or **Quantity** measure.

---

## Challenge Tasks

### Task 1 — Quarterly Revenue by Region (Clustered Column)

Build a clustered column chart that answers: *"How did revenue compare across regions in each quarter?"*

Requirements:

* X-axis: Quarter (use the date hierarchy quarter level)
* Y-axis: Total Sales (sum)
* Legend: Region (each region gets its own cluster)
* Sort: by quarter ascending (Q1 → Q4)
* Data labels: on, Thousands (K), 0 decimal places
* Title: **"Quarterly Revenue by Region"**

### Task 2 — Category Revenue Composition (Stacked Column)

Build a stacked column chart that answers: *"How does each product category contribute to monthly revenue?"*

Requirements:

* X-axis: Month Name (sorted by month number — not alphabetically)
* Y-axis: Total Sales
* Legend: Category
* Total labels: on (showing the full bar height)
* Title: **"Monthly Revenue by Category"**

### Task 3 — Market Share Over Time (100% Stacked)

Build a 100% stacked column chart showing proportional category share per quarter.

Requirements:

* X-axis: Quarter
* Y-axis: Sales (will display as %)
* Legend: Category
* Data labels: on, showing % values
* Title: **"Category Share by Quarter (%)"**

### Task 4 — Ranking Bar Chart

Build a horizontal bar chart ranking the top 10 products by total sales.

Requirements:

* Y-axis: Product Name
* X-axis: Total Sales
* Visual filter: Top 10 by Sales
* Sort: Sales descending (highest at top)
* No legend field
* Title: **"Top 10 Products by Revenue"**

### Task 5 — Add a Region Slicer

Add a **dropdown slicer** for Region that affects all four charts simultaneously. Verify that selecting a region updates all visuals.

---

## Bonus Task — Combo Chart

Replace Task 1 with a **Line and clustered column** combo chart:

* Column Y-axis: Total Sales
* Line Y-axis: Units Sold
* X-axis: Quarter
* Legend: Region

This allows revenue (columns) and volume (line) to be compared on the same visual with dual axes.

---

## Evaluation Criteria

| Criterion | Points |
| --- | --- |
| All 4 charts built with correct field assignments | 40 |
| Correct chart types chosen | 20 |
| Formatting applied (labels, titles, sorting) | 20 |
| Region slicer affects all charts | 10 |
| Bonus combo chart completed | 10 |
| **Total** | **100** |

---

## Reference

* [Create and use column charts in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-column-charts)
* [Customize X-Axis and Y-Axis Properties – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-customize-x-axis-and-y-axis)
