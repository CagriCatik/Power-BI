# Cards and Matrix — Completed Activity

## Overview

This page provides the solutions and explanations for the Cards and Matrix Practical Activity.

---

## Part A — Card Visuals

### Task A1 — Total Sales Card

The card should display a single large number formatted as millions (e.g., **$4.2M**). Setting display units to Millions and decimal places to 1 keeps the number readable without overwhelming the viewer with digits.

The title field is found under **Format visual › General › Title › Title text**. Always title cards clearly — a number without context is meaningless on a dashboard.

### Task A2 — Total Units Card

Similar setup with Thousands as the display unit. **$3.1K units** is more scannable than **3,145**.

### Task A3 — Avg Order Value Measure

The correct DAX expression:

```dax
Avg Order Value = DIVIDE(SUM(Sales[SalesAmount]), COUNT(Sales[OrderID]))
```

Using `DIVIDE` instead of `/` prevents a divide-by-zero error if there are no orders in the current filter context. The result should show no display units and 2 decimal places — for example, **$47.32**.

### Why not use AVERAGE directly?

`AVERAGE(Sales[SalesAmount])` computes the average of the SalesAmount column — which is the average value per row. If each row already represents one order, this is equivalent. But if a row can contain multiple items, you need to compute total revenue divided by a distinct count of orders. Always understand your data grain before choosing the formula.

### Task A4 — Conditional Card Color

The conditional formatting dialog (accessed via the **fx** button next to Font color) lets you define rules. Example rule:

| Rule | Color |
| --- | --- |
| Value ≥ 1,000,000 | Green (`#107C10`) |
| Value < 1,000,000 | Red (`#D83B01`) |

This gives instant visual feedback on whether the target has been met.

---

## Part B — Matrix Visual

### Task B1 — Matrix Field Assignment

| Well | Fields | Result |
| --- | --- | --- |
| Rows | Category → Product | Two-level hierarchy; drill-down available |
| Columns | Year → Quarter | Time axis across the top |
| Values | Sales (Sum) | Revenue at each intersection |

A correctly built matrix shows revenue by product broken down by quarter — a classic cross-tab for performance analysis.

### Task B2 — Subtotals

Enabling row subtotals adds a **Category Total** row after each category's products. Column subtotals add an **Annual Total** column after each year's quarters. The grand total cell (bottom-right) shows the overall revenue across all filters.

### Task B3 — Conditional Formatting

The amber gradient draws the eye to the cells with the highest revenue. Because the gradient scales to the visible min/max, filtering by a slicer or cross-filter recalibrates the color scale automatically.

### Task B4 — Drill-Down

* The **↓** button expands **all** category rows to product level simultaneously.
* Right-clicking a single category and choosing **Drill down** expands only that category — useful when you have many categories and want to focus on one.
* The **Expand all down one level in the hierarchy** button (⊞) is different from Drill down — it shows both the category row and its product rows at the same time.

---

## Part C — Interaction

### Cross-Filter Behavior

When you click a matrix row, all card visuals on the page re-evaluate their DAX measures with that row's filter context applied. This is how a single page becomes interactive without any additional configuration.

If a card does not update when you click the matrix, check **Format → Edit interactions** and ensure the card is set to **Filter** (not None) from the matrix.

---

## References

* [Create a Matrix Visual in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-matrix-visual)
* [Create a card visual in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-card-visual-new-format-settings)
* [CALCULATE function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/calculate-function-dax)
* [How visuals cross-filter each other – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/explore-reports/end-user-interactions)
