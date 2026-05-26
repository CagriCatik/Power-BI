# Column Graph Challenge — Completed

## Task 1 — Clustered Column: Field Assignment

| Well | Field |
| --- | --- |
| X-axis | Quarter (from date hierarchy) |
| Y-axis | Sum of Sales |
| Legend | Region |

### Key points

* To get the **Quarter** level of the date hierarchy, expand the date column in the Fields pane and drag just the Quarter field (not the parent date column).
* To sort ascending by quarter: click the visual ellipsis **(…) › Sort axis › Quarter**, then **(…) › Sort ascending**.
* Data labels: **Format visual › Data labels › On**, Units = Thousands, decimal places = 0.

---

## Task 2 — Stacked Column: Month Sorting

The most common mistake here is months appearing in alphabetical order (April, August, December…) instead of chronological order.

### Fix — Sort Month Name by Month Number

1. Go to **Data View**.
2. Select the **Month Name** column.
3. In **Column tools › Sort by column**, select **Month Number**.
4. Return to Report View — months now appear Jan → Dec.

This setting applies to every visual in the report that uses Month Name.

### Total Labels

Under **Format visual › Total labels**, toggle **On**. This shows the stacked bar's total height — useful when absolute values matter alongside the composition.

---

## Task 3 — 100% Stacked Column: Percentage Labels

When you enable data labels on a 100% stacked chart, Power BI shows raw measure values by default. To show percentages:

1. Under **Format visual › Data labels**, set **Label contents** to **Percent of total** (if available in your version).
2. Alternatively, create a measure that explicitly calculates the percentage:

```dax
Category Share % =
DIVIDE(
    SUM(Sales[SalesAmount]),
    CALCULATE(SUM(Sales[SalesAmount]), REMOVEFILTERS(Sales[Category]))
)
```

Format this measure as a percentage in the Modeling tab.

---

## Task 4 — Ranking Bar Chart

### Visual filter: Top 10

1. Drag **Product Name** into **Filters on this visual**.
2. Change type to **Top N**.
3. Set: Top 10, By value: Sum of Sales.
4. Click **Apply filter**.

### Sorting

* Click visual ellipsis **(…) › Sort axis › Sum of Sales › Sort descending**.
* The product with the highest sales appears at the top of the horizontal bars.

### Why horizontal?

Product names are often long. Horizontal bars allow the full name to appear left-aligned without rotation, improving readability compared to rotated X-axis labels on a vertical column chart.

---

## Task 5 — Slicer Cross-Filter Verification

All four visuals update when the Region slicer selection changes. If a visual is not responding:

1. Select the slicer.
2. Go to **Format › Edit interactions**.
3. Ensure the visual has the **Filter** (funnel) icon active, not the **None** (circle) icon.

---

## Bonus — Combo Chart Notes

The combo chart requires:

* The **Line and clustered column** chart visual (not the standard column chart).
* Two Y-axis wells: **Column y-axis** and **Line y-axis**.
* Two separate scales: left axis for Sales, right axis for Units.
* Units on the right axis must be formatted clearly to avoid confusion with the left axis scale.

Under **Format visual › Y-axis**, enable **Show secondary** and configure the right axis independently.

---

## References

* [Create and use column charts in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-column-charts)
* [Create and use combo charts in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-combo-chart)
* [Customize X-Axis and Y-Axis Properties – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-customize-x-axis-and-y-axis)
