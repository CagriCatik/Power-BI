# Matrix Visualization

## Overview

The **matrix visual** is Power BI's equivalent of a pivot table. It organizes data into rows and columns, supports hierarchical drill-down, and can display subtotals and grand totals at every level. Use a matrix when you need to compare measures across two or more dimensional axes simultaneously.

> **Reference:** [Create a Matrix Visual in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-matrix-visual)

---

## When to Use a Matrix vs a Table

| Feature | Table | Matrix |
| --- | --- | --- |
| Row grouping only | Yes | Yes |
| Column grouping | No | Yes |
| Hierarchical rows | No | Yes (drill-down) |
| Subtotals per group | No | Yes |
| Cross-tab comparison | No | Yes |

Use a **table** for flat, detail-level data. Use a **matrix** when you need to compare a measure across two dimensions simultaneously (e.g., Sales by Region × Quarter).

---

## Building a Matrix Visual

### Step 1 — Add the Visual

1. In the **Visualizations pane**, click the **Matrix** icon.
2. An empty matrix placeholder appears on the canvas.

### Step 2 — Assign Fields

The matrix has three field wells:

| Well | Purpose | Example |
| --- | --- | --- |
| **Rows** | Groups rows; supports hierarchies | Category > Product |
| **Columns** | Groups columns; supports hierarchies | Year > Quarter |
| **Values** | The measures or aggregated columns to display | Total Sales, Units |

Drag fields into each well. A dimension hierarchy (e.g., Date hierarchy: Year → Quarter → Month) can be added to Rows or Columns for drill-down.

---

## Drill-Down in a Matrix

When a hierarchy is in the Rows or Columns well, drill-down buttons appear in the visual header:

| Button | Action |
| --- | --- |
| **↓** (Go to next level) | Expands all rows to the next hierarchy level |
| **⊞** (Expand to next level) | Shows the next level below each current row |
| **↑** (Drill up) | Collapses back to the previous level |

You can also **click a row value** and use the right-click context menu to drill down on a single item.

> **Reference:** [Matrix visual considerations and limitations – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-matrix-visual-considerations)

---

## Layout Options

Open **Format visual › Row headers** to choose:

* **Compact layout** — all hierarchy levels in a single indented column (default, saves space).
* **Outline layout** — each hierarchy level in its own column.
* **Tabular layout** — flat, no indentation.

---

## Subtotals and Grand Totals

Under **Format visual › Row subtotals** and **Column subtotals**:

* Toggle subtotals on or off for rows and columns independently.
* Set subtotal label text (e.g., "Total", "Subtotal").
* Choose font color, background, and font size for subtotal rows.

Under **Format visual › Grand total**:

* Toggle grand total rows and columns on or off.
* Apply independent formatting to distinguish grand totals from subtotals.

> **Reference:** [Matrix visual format settings in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-matrix-visual-format-settings)

---

## Conditional Formatting on a Matrix

Conditional formatting works on **Values cells only** — not on row or column headers.

1. Click the chevron next to a field in the **Values** well.
2. Select **Conditional formatting**.
3. Choose **Background color**, **Font color**, **Data bars**, or **Icons**.

This is identical to the table conditional formatting workflow.

> **Reference:** [Apply Conditional Table Formatting – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-conditional-table-formatting)

---

## Stepped Layout

**Stepped layout** (under Format visual › Row headers) renders each hierarchy level indented within the same column. This is the default compact layout. Disable it to see separate columns for each level (outline layout).

---

## Column Width and Autofit

* **Autofit column width** (Format visual › Column headers) — dynamically sizes columns to content width.
* **Word wrap** — wraps long header text to multiple lines.
* To manually resize a column, hover over the column border in the matrix header and drag.

---

## Best Practices

* Keep hierarchies to **three levels maximum** in a matrix — deeper hierarchies become unwieldy on screen.
* Use **conditional formatting** on the Values cells to immediately surface outliers.
* Add **drill-through** from a matrix row to a detail report page for a two-click deep-dive workflow.
* For large matrices with many columns, enable **horizontal scroll** by reducing the canvas width and placing the matrix inside a scrollable container.

---

## References

* [Create a Matrix Visual in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-matrix-visual)
* [Matrix visual format settings – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-matrix-visual-format-settings)
* [Matrix visual considerations and limitations – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-matrix-visual-considerations)
* [Apply Conditional Table Formatting – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-conditional-table-formatting)
