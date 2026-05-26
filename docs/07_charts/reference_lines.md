# Reference Lines

## Overview

**Reference lines** add horizontal or vertical marker lines to a chart at a constant value, a dynamic statistical value (min, max, average, percentile), or an error bound. They let viewers immediately compare data points against a benchmark without building a separate visual.

> **Reference:** [Use the Analytics pane in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-analytics-pane)

---

## Accessing the Analytics Pane

1. Select a chart visual (line, column, bar, area, or scatter).
2. In the **Visualizations pane**, click the **Analytics** tab (magnifying glass icon).
3. The available reference line types appear as expandable sections.

Not all line types are available for every chart type — the Analytics pane only shows options supported by the selected visual.

---

## Reference Line Types

| Line type | Description |
| --- | --- |
| **Constant line** | Horizontal line at a fixed value you specify |
| **Min line** | Line at the minimum value of the plotted measure |
| **Max line** | Line at the maximum value |
| **Average line** | Line at the mean value of the plotted measure |
| **Median line** | Line at the median value |
| **Percentile line** | Line at a specified percentile (e.g., 75th) |
| **Error bars** | Vertical error bands around data points |
| **Forecast** | Forward projection beyond the last data point |
| **Anomaly detection** | Highlights statistically unusual data points |

---

## Adding a Constant Line

A **constant line** marks a fixed target or threshold — for example, a sales quota of $50,000:

1. In the **Analytics** tab, expand **Constant line**.
2. Click **Add line**.
3. Set the **Value** field to your target number (e.g., 50000).
4. Optionally set the line name, color, line style (solid, dashed, dotted), and position (in front of / behind data).
5. Toggle **Data label** on to show the value on the line itself.

Multiple constant lines can be added — for example, a lower bound, target, and stretch goal.

---

## Adding a Dynamic Line (Average, Min, Max)

1. Expand the **Average line** (or Min/Max/Median) section.
2. Click **Add line**.
3. Select the **Measure** the line is based on.
4. Configure color, style, width, and label.

The line updates dynamically with filters and slicers — if a slicer filters to a specific region, the average line reflects the average for that region.

---

## Adding a Percentile Line

1. Expand **Percentile line**.
2. Click **Add line**.
3. Set the percentile value (e.g., 90 for the 90th percentile).
4. Configure color and label.

Useful for identifying outliers — points above the 90th percentile line are in the top 10% of values.

---

## Reference Line Formatting

For each line you can configure:

| Setting | Options |
| --- | --- |
| **Color** | Any color via color picker |
| **Transparency** | 0–100% opacity |
| **Style** | Solid, dashed, dotted |
| **Position** | In front of data / behind data |
| **Data label** | On/off, label text (value, name, both) |
| **Label position** | Left or right, above or below line |

---

## Error Bars

**Error bars** show a range of uncertainty around each data point. They are available on line and column charts.

1. Expand **Error bars** in the Analytics tab.
2. Set the **Upper bound** and **Lower bound** fields (columns or measures that define the error range).
3. The chart displays error bar extensions above and below each data point.

---

## Practical Example

A line chart shows monthly revenue. You want to mark the annual target and the average:

1. Add a **Constant line** at 100,000 (monthly target). Label it "Target". Color: green, dashed.
2. Add an **Average line** for Sum of Sales. Label: "Average". Color: orange, solid.

Now the chart shows three layers of information: actual revenue, the target, and the running average — all on one visual.

---

## Best Practices

* Use **constant lines** for fixed targets, budgets, or regulatory thresholds.
* Use **average lines** on operational charts to quickly flag anomalies above/below the mean.
* Keep lines **visually distinct** from the data — use dashes or dots and a contrasting color so lines do not look like data series.
* Add **data labels** to reference lines so viewers know the exact threshold without having to read the Y-axis.
* Do not add more than **2–3 reference lines** to a single chart — more than that creates visual clutter.

---

## References

* [Use the Analytics pane in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-analytics-pane)
* [Line Charts in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-line-chart)
