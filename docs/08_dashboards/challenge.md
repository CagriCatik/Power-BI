# Challenge — Create an Interactive Report

## Objective

Build a complete, multi-page interactive report that uses the full range of skills covered in this course. The report must include visuals, slicers, filters, cards, charts, a matrix, and be publishable to the Power BI Service.

---

## Report Requirements

### Page 1 — Executive Summary

Build a summary page that answers: *"How is the business performing this month vs last month?"*

Requirements:

* **3 KPI cards** at the top: Total Revenue, Total Units, Average Order Value.
* **Line chart** showing monthly revenue trend for the current year.
* **Clustered column chart** showing revenue by top 5 product categories.
* **Region slicer** (dropdown) affecting all visuals on the page.
* Page title: **"Executive Summary"**.

### Page 2 — Product Analysis

Build a product-level analysis page: *"Which products and categories drive the most revenue?"*

Requirements:

* **Matrix visual**: rows = Category → Product, columns = Quarter, values = Sales.
* **Bar chart**: Top 10 products by revenue (Top N filter applied).
* **100% stacked column chart**: Category share by month.
* **Scatter chart**: Quantity vs Revenue per product (bubble size = profit).
* Date slicer (Between style) affecting all visuals on the page.
* Page title: **"Product Analysis"**.

### Page 3 — Trends and Forecast

Build a forward-looking page: *"What do revenue trends and forecasts look like?"*

Requirements:

* **Line chart**: Monthly revenue with trend line and 6-month forecast (95% confidence).
* **Area chart**: Cumulative revenue by category over time.
* **Reference line**: Constant line at the annual monthly target value.
* Date slicer synced from Page 1.
* Page title: **"Trends and Forecast"**.

---

## Interactivity Requirements

* All visuals on each page cross-filter each other.
* The Region slicer on Page 1 is synced to Pages 2 and 3.
* At least one visual on Page 2 has a **drill-through** link to Page 3.
* Clicking a product in the matrix drills through to the trend page filtered to that product.

---

## Formatting Requirements

* Consistent color theme across all pages (amber, matching the site theme, or your own choice).
* All visuals have clear, descriptive titles.
* KPI cards have conditional color (green above target, red below).
* At least one chart uses conditional formatting.

---

## Bonus Tasks

* Add a **4th page** with a Q&A visual for natural language queries.
* Add **bookmarks** for two different slicer states with a toggle button on the Summary page.
* Add a **mobile layout** for Page 1 optimised for phone screens.

---

## Submission Checklist

| Requirement | Done |
| --- | --- |
| 3 pages with correct titles | ☐ |
| KPI cards with conditional color | ☐ |
| Line chart with trend and forecast | ☐ |
| Matrix with drill-down | ☐ |
| Top 10 product bar chart (Top N filter) | ☐ |
| Scatter chart | ☐ |
| Region slicer synced across pages | ☐ |
| Drill-through from matrix to trend page | ☐ |
| Consistent color theme | ☐ |
| Report published to Power BI Service | ☐ |

---

## Reference

* [Create and Format Table Visualizations – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-tables)
* [Create a Matrix Visual in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-matrix-visual)
* [Use the Analytics pane in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-analytics-pane)
* [Publish semantic models and reports from Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-upload-desktop-files)
