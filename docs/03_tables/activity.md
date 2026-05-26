# Tables Practical Activity

## Objective

Apply the table skills covered in this section to build and format a table visual from the training dataset. By the end of this activity you will have a formatted, interactive table that demonstrates aggregation, conditional formatting, and cross-filter interaction.

---

## Dataset

Use the training Excel file loaded into your Power BI Desktop file. It contains columns such as:

* **Product** — product name (text)
* **Category** — product category (text)
* **Region** — sales region (text)
* **Sales** — revenue amount (numeric)
* **Units** — quantity sold (numeric)
* **OrderDate** — transaction date (date)

---

## Tasks

### Task 1 — Create a Basic Table

1. Open a blank report page. Name it **"Tables Activity"**.
2. Add a **Table visual** to the canvas.
3. Add these fields to the Columns well in order:
   * Product
   * Category
   * Region
   * Sales
   * Units
4. Resize the table to fill roughly half the canvas.
5. Sort the table by **Sales descending**.

**Expected result:** A multi-column table showing products, their categories and regions, and aggregated sales and units, sorted from highest to lowest sales.

---

### Task 2 — Apply a Style Preset

1. With the table selected, open the **Format visual** pane.
2. Under **Style presets**, choose **Alternating rows**.
3. Confirm the table now shows banded rows.

---

### Task 3 — Format Column Headers

1. Under **Format visual › Column headers**:
   * Set background color to **dark grey** (e.g., `#333333`).
   * Set font color to **white** (`#FFFFFF`).
   * Set font size to **12**.
   * Enable **Bold**.
2. Confirm the headers are now white text on a dark background.

---

### Task 4 — Conditional Formatting on Sales

1. In the **Columns** well, click the chevron (∨) next to **Sales**.
2. Select **Conditional formatting › Background color**.
3. Set **Format style** to **Gradient**.
4. Choose:
   * Minimum: white (`#FFFFFF`)
   * Maximum: green (`#107C10`)
5. Click **OK**.

**Expected result:** The Sales column now shades from white (lowest) to green (highest), making top performers visually obvious.

---

### Task 5 — Add a Data Bar to Units

1. Click the chevron next to **Units** in the Columns well.
2. Select **Conditional formatting › Data bars**.
3. Keep default colors (blue positive bar).
4. Click **OK**.

---

### Task 6 — Add a Second Visual and Test Cross-Filtering

1. Add a **Clustered column chart** to the canvas (Category on X-axis, Sales on Y-axis).
2. Click a bar in the column chart.
3. Observe the table filtering to show only rows from that category.
4. Click the same bar again (or press **Esc**) to clear the filter.

---

## Checklist

| Task | Done |
| --- | --- |
| Table created with 5 fields | ☐ |
| Sorted by Sales descending | ☐ |
| Alternating rows style applied | ☐ |
| Header formatted (dark/white/bold) | ☐ |
| Conditional formatting on Sales | ☐ |
| Data bars on Units | ☐ |
| Cross-filter tested with column chart | ☐ |

---

## Tips

* If a column shows "Sum of Sales" in the header, you can rename it: click the field in the Columns well, choose **Rename for this visual**, and type a cleaner name like "Revenue".
* If totals row aggregation looks wrong for a measure, check the DAX expression — totals evaluate at the grand total filter context, not as a sum of row values.

---

## Reference

* [Create and Format Table Visualizations – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-tables)
* [Apply Conditional Table Formatting – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-conditional-table-formatting)
