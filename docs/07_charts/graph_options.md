# Graph Options

## Overview

Every chart visual in Power BI exposes a rich set of formatting options in the **Format visual** pane. This page covers the most important common options shared across column, bar, line, and area charts.

> **Reference:** [Get Started Formatting Report Visualizations – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/service-getting-started-with-color-formatting-and-axis-properties)

---

## General Settings

### Visual Title

Under **Format visual › General › Title**:

* Toggle the title on or off.
* Set custom text, font, size, color, and alignment.
* Use an expression (fx) for dynamic titles that change with slicer selections.

> **Reference:** [Create Expression-Based Titles – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-conditional-format-visual-titles)

### Background and Border

Under **Format visual › General**:

* **Background color** — fill the visual container.
* **Border** — add a border with custom color, width, and rounded corners.
* **Shadow** — add a drop shadow.
* **Padding** — control internal whitespace.

---

## Axes

### X-Axis (Category Axis)

| Option | Effect |
| --- | --- |
| **Toggle** | Show or hide the axis entirely |
| **Title** | Set a label for the axis |
| **Values** | Font, size, color of axis tick labels |
| **Label rotation** | Rotate labels (0°, 45°, 90°) |
| **Type** | Categorical or Continuous (for date axes) |
| **Gridlines** | Show/hide vertical gridlines |
| **Scroll bar** | Enable horizontal scrolling when many categories |

### Y-Axis (Value Axis)

| Option | Effect |
| --- | --- |
| **Toggle** | Show or hide |
| **Start at zero** | Force the axis to start at 0 (recommended) |
| **Range (Min/Max)** | Manually set axis bounds to zoom in |
| **Display units** | None, Thousands, Millions, Billions |
| **Decimal places** | Precision on axis tick labels |
| **Secondary Y-axis** | Enable for combo charts (dual axes) |

---

## Data Labels

Under **Format visual › Data labels**:

* **Toggle** — show or hide value labels on bars/lines.
* **Position** — Inside end, Outside end, Center, Inside base (column charts).
* **Display units** — Thousands (K), Millions (M).
* **Decimal places** — precision of displayed values.
* **Overflow text** — allow labels to overflow the bar boundaries.
* **Background color / color** — make labels readable against the bar color.

---

## Legend

Under **Format visual › Legend**:

* **Toggle** — show or hide the legend.
* **Position** — Top, Bottom, Left, Right, Top center, etc.
* **Title** — custom legend title text.
* **Font** — size and color of legend items.

For charts without a Legend field, the legend section is grayed out.

---

## Colors (Bars / Lines)

### Single Color

Under **Format visual › Columns** (or **Bars**, **Lines**):

* **Default color** — one color for all bars.

### Series Colors

When a **Legend** field is set, each series gets its own color:

* Click each legend item in the Colors section to change its color.
* Or apply a **theme** to set colors consistently across all visuals.

### Conditional Formatting

Click the **fx** icon next to the color to open the conditional formatting dialog:

* Color by **field value** — a column holding color hex codes or names.
* Color by **rules** — threshold-based conditional colors.
* Color by **gradient** — continuous scale based on measure value.

---

## Zoom Slider

Under **Format visual › Zoom slider**:

* Toggle on to add an interactive range slider below the X-axis.
* Consumers can drag the slider handles to zoom into a specific X-axis range.
* Useful for line and area charts with many time periods.

---

## Plot Area

Under **Format visual › Plot area**:

* Set a background image or color for the chart plot area (inside the axes).
* Useful for watermarking or adding context to charts.

---

## Tooltips

Under **Format visual › Tooltips**:

* **Default tooltips** — Power BI auto-generates tooltips from the visual fields.
* **Report page tooltip** — link to a custom tooltip report page with richer content.
* **Values** — add additional measures shown on hover without showing them in the visual.

---

## Best Practices

* Always enable a visual **title** — a chart without a title requires consumers to interpret it without context.
* Keep the **Y-axis starting at zero** to avoid misleading comparisons.
* Use **display units (K/M)** so numbers are readable without scientific notation.
* Limit **data labels** to visuals where exact values matter — unnecessary labels add noise.
* Use a **report theme** for consistent colors across all visuals rather than coloring each chart individually.

---

## References

* [Get Started Formatting Report Visualizations – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/service-getting-started-with-color-formatting-and-axis-properties)
* [Customize X-Axis and Y-Axis Properties – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-customize-x-axis-and-y-axis)
* [Create Expression-Based Titles – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-conditional-format-visual-titles)
