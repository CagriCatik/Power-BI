# Practical Activity — Filters

## Objective

Practice applying all three filter levels (visual, page, report), configure text/numeric/date slicers, and verify their combined behavior. By the end you will have a two-page report where filters work independently per page and a global filter constrains the whole report.

---

## Setup

Open the training Power BI Desktop file. You need at least two report pages. Name them:

* **Page 1 — Sales Overview**
* **Page 2 — Product Detail**

---

## Part A — Visual-Level Filters

### Task A1 — Top 5 Products Bar Chart

1. On Page 1, add a **Clustered column chart**: Product on X-axis, Sales on Y-axis.
2. With the chart selected, drag **Product** into **Filters on this visual**.
3. Change filter type to **Top N**.
4. Set: Top 5, By value: Sales.
5. Click **Apply filter**.

Expected result: the chart shows only the 5 highest-selling products.

### Task A2 — Advanced Text Filter

1. Add a **Table visual** on Page 1 with columns: Product, Category, Sales.
2. Drag **Category** into **Filters on this visual**.
3. Set filter type to **Advanced filtering**.
4. Condition: Category **does not contain** "Misc".
5. Click **Apply filter**.

Expected result: the table hides any row where Category contains "Misc".

---

## Part B — Page-Level Filter

### Task B1 — Lock Page 1 to Current Year

1. Click an empty area of **Page 1**.
2. Drag **OrderDate** (or your date column) into **Filters on this page**.
3. Change filter type to **Relative date**.
4. Set: In this Calendar year.
5. Click **Apply filter**.
6. Click the **lock icon** on the filter card.

Expected result: all visuals on Page 1 now show only current-year data, and the filter cannot be removed by consumers.

---

## Part C — Report-Level Filter

### Task C1 — Exclude Inactive Products

1. Click an empty area of the canvas.
2. Drag **Status** (or an equivalent column) into **Filters on all pages**.
3. Set basic filter to include only "Active".
4. Click the **eye icon** to hide the filter from consumers.
5. Click the **lock icon** to lock it.

Expected result: inactive products are hidden across all pages and consumers cannot see or change the filter.

---

## Part D — Slicers

### Task D1 — Text Slicer on Page 1

1. Add a **Slicer** visual with **Region** as the field.
2. Change style to **Dropdown**.
3. Enable **Select all**.
4. Sync this slicer to Page 2 (**View › Sync slicers**, toggle Page 2 on).

### Task D2 — Date Slicer on Page 2

1. On Page 2, add a **Slicer** with **OrderDate** as the field.
2. Change style to **Between**.
3. Set an initial default range in the slicer (optional — consumers can adjust).

### Task D3 — Numeric Slicer on Page 2

1. On Page 2, add a **Slicer** with **Sales** as the field.
2. Keep the default **Between** slider style.
3. Add a title: "Filter by Sales Amount".

---

## Part E — Verification

1. On Page 1, select a region in the dropdown slicer.
2. Navigate to Page 2 — confirm the same region is pre-selected (sync working).
3. On Page 1, verify the bar chart shows only 5 products (visual filter working).
4. On Page 1, verify the table has no "Misc" rows (advanced text filter working).
5. On Page 1, verify dates are current year only (page filter working).
6. On both pages, verify inactive products are not shown (report filter working).

---

## Checklist

| Task | Done |
| --- | --- |
| Top 5 visual filter on bar chart | ☐ |
| Advanced text filter excluding "Misc" | ☐ |
| Page-level date filter locked to current year | ☐ |
| Report-level status filter hidden and locked | ☐ |
| Dropdown region slicer synced across pages | ☐ |
| Date between slicer on Page 2 | ☐ |
| Numeric sales slicer on Page 2 | ☐ |
| All filters verified end-to-end | ☐ |

---

## References

* [Add a Filter to a Report in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-report-add-filter)
* [Slicers in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-slicers)
* [Filters and highlighting in Power BI reports – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-reports-filters-and-highlighting)
