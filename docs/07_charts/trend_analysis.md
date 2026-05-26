# Trend Analysis Graphs

## Overview

Trend analysis in Power BI involves identifying patterns, directions, and rates of change in data over time. Line charts are the primary tool, supplemented by trend lines, moving averages, and the Analytics pane to surface underlying signals beneath short-term noise.

> **Reference:** [Line Charts in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-line-chart)
> **Reference:** [Use the Analytics pane in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-analytics-pane)

---

## The Line Chart for Trend Analysis

A line chart is ideal for time-series data:

1. Select the **Line chart** visual.
2. Assign:
   * **X-axis**: a date or time column (or date hierarchy level: Year, Month, Week)
   * **Y-axis**: the measure to track (e.g., Total Sales, Website Visits)
   * **Legend** (optional): a dimension to show multiple lines (e.g., Region)
3. Power BI draws a continuous line connecting each time point.

For continuous X-axis behavior (smooth interpolation), ensure your date column type is set to **Date** or **Date/Time** and the axis type is **Continuous** under **Format visual › X-axis › Type**.

---

## Adding a Trend Line

A trend line fits a linear regression to the data — it shows the overall direction of the trend even when individual points fluctuate.

1. Select the line chart.
2. Open the **Analytics** tab.
3. Expand **Trend line**.
4. Click **Add**.
5. Configure color, style, and data label.

The trend line equation is not shown by default, but the direction (slope upward = positive trend) and confidence band options reveal the trend's strength.

> **Note:** Trend lines require a **single series** (no Legend field) and a **continuous X-axis** (date or numeric).

---

## Moving Average with DAX

A **moving average** smooths short-term fluctuations. It is not a built-in Analytics option but can be created with a DAX measure.

### 3-Month Moving Average

```dax
Sales 3M MA =
CALCULATE(
    AVERAGE(Sales[SalesAmount]),
    DATESINPERIOD(
        'Date'[Date],
        LASTDATE('Date'[Date]),
        -3,
        MONTH
    )
)
```

Add this measure as a second line on the chart (alongside raw Sales) to show smoothed vs actual.

> **Reference:** [DATESINPERIOD function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/datesinperiod-function-dax)

---

## Year-Over-Year Comparison

Compare the current period to the same period last year to identify growth or decline:

```dax
Sales PY =
CALCULATE(
    SUM(Sales[SalesAmount]),
    SAMEPERIODLASTYEAR('Date'[Date])
)
```

Plot both **Sum of Sales** and **Sales PY** as two lines on the same chart. The gap between the lines shows growth or contraction.

> **Reference:** [Time intelligence functions (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/time-intelligence-functions-dax)

---

## Small Multiples for Multi-Series Trends

When comparing trends across many categories (e.g., 10 regions), adding all as a Legend creates an unreadable chart. Use **small multiples** instead:

1. Add the category to the **Small multiples** well.
2. Power BI renders a separate mini line chart for each category in a grid.
3. All charts share the same X-axis scale, making comparisons accurate.

> **Reference:** [Create Small Multiples in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-small-multiples)

---

## Zoom Slider

For detailed exploration of a specific time window:

* Under **Format visual › Zoom slider**, toggle on.
* A mini-range control appears below the X-axis.
* Drag to zoom into any period while keeping the full timeline visible.

---

## Chart Markers

Under **Format visual › Markers**:

* Toggle markers (dots) on each data point.
* Set marker shape, size, and color.
* Markers make individual data points easier to click and identify in dense line charts.

---

## Best Practices

* Use a **continuous date axis** (not categorical) for time series so gaps in the data do not produce misleading flat segments.
* Add a **trend line** when you want to communicate direction, not just individual data points.
* Use **DAX moving averages** on weekly/daily data to show underlying patterns without short-term noise.
* Plot **year-over-year comparisons** on the same chart instead of separate charts for direct visual comparison.
* Use **small multiples** to compare trends across many segments without overlapping lines.

---

## References

* [Line Charts in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-line-chart)
* [Use the Analytics pane in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-analytics-pane)
* [DATESINPERIOD function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/datesinperiod-function-dax)
* [Time intelligence functions (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/time-intelligence-functions-dax)
* [Create Small Multiples in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-small-multiples)
