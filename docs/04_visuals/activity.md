# Cards and Matrix — Practical Activity

## Objective

Build a summary page using card visuals and a matrix visual that work together interactively. You will practice assigning fields to matrix wells, enabling drill-down, formatting cards with conditional color, and verifying cross-filter behavior between the matrix and cards.

---

## Setup

Open the training Power BI Desktop file and add a new report page named **"Cards & Matrix Activity"**.

---

## Part A — Card Visuals

### Task A1 — Total Sales Card

1. Add a **Card** visual to the top-left of the canvas.
2. Drag the **Sales** measure (or column set to Sum) into the **Callout value** well.
3. In **Format visual › Callout value**, set:
   * Display units: **Millions (M)**
   * Decimal places: **1**
4. Rename the card title to **"Total Revenue"** via **Format visual › General › Title**.

### Task A2 — Total Units Card

1. Add a second **Card** visual next to the first.
2. Add the **Units** field (Sum) as the callout value.
3. Set display units to **Thousands (K)**, 1 decimal place.
4. Title: **"Units Sold"**

### Task A3 — Average Order Value Card

1. Create a DAX measure in your model:

```dax
Avg Order Value = DIVIDE(SUM(Sales[SalesAmount]), COUNT(Sales[OrderID]))
```

1. Add a third **Card** visual with this measure.
2. Format: no display units, 2 decimal places, title **"Avg Order Value"**.

### Task A4 — Conditional Card Color

1. Select the Total Revenue card.
2. Go to **Format visual › Callout value → Font color → Conditional formatting (fx)**.
3. Set a rule: if value is **greater than** your target (e.g., 1,000,000), color is **green**; else **red**.

---

## Part B — Matrix Visual

### Task B1 — Build the Matrix

1. Add a **Matrix** visual to the lower half of the canvas.
2. Assign fields:
   * **Rows**: Category → Product
   * **Columns**: Year → Quarter (use the Date hierarchy if available)
   * **Values**: Sales (Sum)

### Task B2 — Enable Subtotals

1. In **Format visual**:
   * Enable **Row subtotals** — shows a subtotal row per Category.
   * Enable **Column subtotals** — shows a subtotal column per Year.
   * Enable **Grand total** for rows and columns.

### Task B3 — Conditional Formatting on the Matrix

1. Click the chevron next to **Sum of Sales** in the Values well.
2. Select **Conditional formatting › Background color**.
3. Apply a gradient from white (lowest) to amber/orange (highest).

### Task B4 — Drill Down

1. Click the **↓** button in the matrix header to expand all categories to their products.
2. Click the **↑** button to collapse back.
3. Right-click a single category row and select **Drill down** to expand only that category.

---

## Part C — Interaction

### Task C1 — Cross-Filter Cards from Matrix

1. Click a Category row in the matrix.
2. Observe that all three card visuals update to show totals for that category only.
3. Press **Esc** or click away to clear the filter.

### Task C2 — Verify Card Totals

1. Confirm that the cards show grand totals when nothing is selected.
2. Select one year in the column headers — confirm cards update to that year's data.

---

## Checklist

| Task | Done |
| --- | --- |
| Three card visuals created and formatted | ☐ |
| Avg Order Value DAX measure created | ☐ |
| Conditional color on Total Revenue card | ☐ |
| Matrix with Category/Product rows and Year/Quarter columns | ☐ |
| Subtotals and grand totals enabled | ☐ |
| Conditional formatting on matrix values | ☐ |
| Drill-down tested | ☐ |
| Cross-filter from matrix to cards tested | ☐ |

---

## References

* [Create a Matrix Visual in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-matrix-visual)
* [Create a card visual in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-card-visual-new-format-settings)
* [CALCULATE function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/calculate-function-dax)
