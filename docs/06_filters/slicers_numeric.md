# Using Slicers — Numeric

## Overview

A **numeric slicer** filters visuals by a numeric range, letting users drag a slider or enter minimum and maximum values to restrict the data. Common uses include filtering by price range, quantity, discount percentage, or age.

> **Reference:** [Slicers in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-slicers)

---

## Adding a Numeric Slicer

1. Click an empty area of the canvas.
2. In the **Visualizations pane**, click the **Slicer** icon.
3. Drag a **numeric column** (e.g., Sales Amount, Discount %, Quantity) into the **Field** well.
4. Power BI automatically renders a **Between** range slider.

---

## Numeric Slicer Styles

Open **Format visual › Slicer settings › Style** to change the style:

| Style | Description |
| --- | --- |
| **Between** | Two-handle slider — set a min and max value |
| **Less than or equal to** | Single right-side handle — values up to a maximum |
| **Greater than or equal to** | Single left-side handle — values from a minimum |
| **List** | Checkbox list of all distinct numeric values (use only for low-cardinality fields) |

---

## Using the Slider

* Drag the **left handle** to set the minimum value.
* Drag the **right handle** to set the maximum value.
* Type values directly into the input boxes above the slider for precise control.
* The displayed range updates all connected visuals as you drag.

---

## Numeric Slicer with a Measure

You cannot directly place a DAX measure in a slicer — slicers require a column from a table. If you need to filter by a calculated metric:

* Create a **calculated column** in the model that stores the value per row (e.g., `Profit Margin = Sales[Profit] / Sales[Revenue]`).
* Use that calculated column in the slicer.

Alternatively, use **visual-level filters** in the Filters pane with advanced filter conditions for measure-based thresholds.

---

## Formatting a Numeric Slicer

### Slicer Header

Under **Format visual › Slicer header**:

* Set a custom title (e.g., "Filter by Sales Amount").
* Toggle and format the header text.

### Slider

Under **Format visual › Slider**:

* **Color** — the color of the filled (selected) range on the slider track.
* **Track color** — the unfilled portion of the track.

### Input boxes

Under **Format visual › Input**:

* Font family and size for the number input boxes.

### Values font

Under **Format visual › Values**:

* Controls font size and color for the min/max numbers shown below the slider.

---

## Clearing a Numeric Slicer

* Hover over the slicer header — an **eraser icon** appears.
* Click the eraser to reset the range back to its full extent (all values included).

---

## Practical Example

You have a product sales table and want to let users focus on products with sales between $10,000 and $50,000:

1. Add a slicer with the **Sales Amount** column.
2. Change to **Between** style.
3. Set the left handle to 10,000 and the right handle to 50,000.
4. The table and charts on the page now show only products within that revenue range.

---

## Best Practices

* Use numeric slicers for **continuous ranges** — price bands, percentages, quantities.
* Avoid using numeric slicers on **high-cardinality integer columns** (like OrderID) — the slider is meaningless for ID values; use a search filter instead.
* Label the slicer header clearly with the unit of measure (e.g., "Sales Amount ($)" or "Discount (%)") so consumers know the scale.
* Combine a numeric slicer with a histogram visual so users can see the data distribution before adjusting the range.

---

## References

* [Slicers in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-slicers)
* [Filters and highlighting in Power BI reports – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-reports-filters-and-highlighting)
