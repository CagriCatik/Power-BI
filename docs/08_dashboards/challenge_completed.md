# Interactive Report Challenge — Completed

## Overview

This page walks through the key decisions and solutions for the Interactive Report challenge.

---

## Page 1 — Executive Summary

### KPI Card Setup

Three card visuals with conditional color communicate health at a glance:

* **Total Revenue** — measures the sum of all sales.
* **Total Units** — sum of quantity sold.
* **Average Order Value** — `DIVIDE([Total Revenue], DISTINCTCOUNT(Sales[OrderID]))`.

For conditional color on each card: **Format visual › Callout value → Font color → fx (conditional formatting)** → Rules → value ≥ target = green, else red.

### Line Chart — Monthly Trend

* X-axis: Month Name (sorted by Month Number, not alphabetically).
* Y-axis: Total Revenue.
* No legend — single series enables forecasting if desired.
* Under **Format visual › X-axis → Type = Continuous** for proper date rendering.

### Clustered Column — Top 5 Categories

* X-axis: Category.
* Y-axis: Total Revenue.
* Visual filter: Top N = 5 by Revenue.
* Sorted descending by Revenue.

### Region Slicer Sync

Open **View › Sync slicers** and enable sync for Pages 2 and 3. Leave visible only on Page 1 (sync on, visible off for other pages) to save canvas space while keeping the filter active everywhere.

---

## Page 2 — Product Analysis

### Matrix Setup

| Well | Field |
| --- | --- |
| Rows | Category → Product |
| Columns | Year → Quarter |
| Values | Total Revenue |

Enable **Row subtotals** and **Column subtotals** for category and year rollups. Apply amber gradient conditional formatting on Values cells.

### Scatter Chart

| Well | Field |
| --- | --- |
| X-axis | Quantity Sold |
| Y-axis | Total Revenue |
| Values | Product Name |
| Size | Profit (or Margin %) |

Products in the top-right quadrant (high quantity AND high revenue) are star performers. Products in the bottom-right (high quantity, low revenue) may need pricing review.

### Drill-Through Setup

1. On Page 3 (Trends), go to the **Filters pane › Drill-through** section.
2. Drag **Product Name** into the Drill-through field.
3. On Page 2, right-click any product in the matrix → **Drill through › Trends and Forecast**.
4. Page 3 opens pre-filtered to that product.

Power BI automatically adds a **Back button** to the drill-through destination page.

---

## Page 3 — Trends and Forecast

### Forecast Settings

* Single-series line chart (no Legend field).
* X-axis: Month (continuous date axis).
* Analytics pane › Forecast: Length = 6 months, Seasonality = 12, Confidence = 95%.
* Constant line at monthly revenue target (e.g., 150,000).

### Area Chart — Cumulative Revenue

Using a DAX measure for cumulative total:

```dax
Revenue Running Total =
CALCULATE(
    SUM(Sales[SalesAmount]),
    DATESINPERIOD(
        'Date'[Date],
        LASTDATE('Date'[Date]),
        -12,
        MONTH
    )
)
```

Plot this measure alongside individual category revenues in a stacked area chart.

---

## Bonus Tasks

### Q&A Visual

Add the **Q&A visual** from the Visualizations pane. Consumers can type questions like "total revenue by region last year" and Power BI generates the chart automatically. Configure suggested questions under **Format visual › Q&A setup**.

### Bookmarks

1. Set Slicer to State A (e.g., North region) → **View › Bookmarks → Add bookmark** → name it "North View".
2. Set Slicer to State B (All regions) → **Add bookmark** → name it "All Regions".
3. Add a **Button** (Insert › Buttons › Blank) → under **Action**, set Type = Bookmark, Bookmark = "North View".
4. Duplicate and set the second button to "All Regions".

### Mobile Layout

1. Go to **View › Mobile layout**.
2. Drag the 3 KPI cards and the line chart from the right panel onto the phone canvas.
3. Arrange vertically — cards stacked at top, chart below.
4. Visuals stack full-width on mobile automatically.

---

## References

* [Create a Power BI dashboard from a report – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboard-create)
* [Publish semantic models and reports – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-upload-desktop-files)
* [Use the Analytics pane in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-analytics-pane)
* [Power BI Mobile Layout View – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-create-mobile-optimized-report-mobile-layout-view)
