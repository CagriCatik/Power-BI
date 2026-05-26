# Table Styles and Formatting

## Overview

Power BI offers extensive formatting options for table visuals — from quick preset styles to per-column conditional rules based on data values. Good formatting makes data scannable and draws attention to what matters.

> **Reference:** [Create and Format Table Visualizations – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-tables)
> **Reference:** [Apply Conditional Table Formatting – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-conditional-table-formatting)

---

## Accessing Format Options

1. Select the table visual.
2. In the **Visualizations pane**, click the **Format visual** tab (paint roller icon).
3. Expand sections: **Style presets**, **Grid**, **Column headers**, **Values**, **Totals**, **Specific columns**.

---

## Style Presets

The quickest way to apply a consistent look:

| Preset | Description |
| --- | --- |
| **None** | Minimal, borderless grid |
| **Minimal** | Thin lines, light headers |
| **Bold header** | Dark header row, white text |
| **Alternating rows** | Banded rows for readability |
| **Contrast alternating rows** | High-contrast banding |
| **Flashy rows** | Stronger color accent |
| **Condensed** | Reduced row height |

Select a preset under **Format visual › Style presets** to apply it instantly, then override individual settings below it.

---

## Grid Settings

| Option | Effect |
| --- | --- |
| **Horizontal gridlines** | Show/hide lines between rows |
| **Vertical gridlines** | Show/hide lines between columns |
| **Row padding** | Set padding (pixels) above/below cell text |
| **Text size** | Global font size for the table body |
| **Font family** | Choose a font for all cells |

---

## Column Headers

| Option | Effect |
| --- | --- |
| **Font color** | Header text color |
| **Background color** | Header background color |
| **Font size** | Header text size |
| **Bold / Italic / Underline** | Text decoration |
| **Alignment** | Left, center, or right |
| **Text wrap** | Allow long headers to wrap |
| **Auto size column width** | Fit column width to content |

---

## Values (Body Cells)

Same controls as column headers, applied to data rows:

* Background color, font color, font size, font family, bold/italic.
* **Alternating row colors** — set two colors for banded rows.

---

## Conditional Formatting

Conditional formatting applies dynamic visual cues based on data values. To add it:

1. Right-click (or click the **chevron ∨**) on a column in the **Columns** well.
2. Select **Conditional formatting**.
3. Choose a format type:

| Type | What It Shows |
| --- | --- |
| **Background color** | Fill cell background by value or rule |
| **Font color** | Color text by value or rule |
| **Data bars** | Horizontal in-cell bar proportional to value |
| **Icons** | KPI-style symbols (arrows, shapes, flags) |
| **Web URL** | Make cell text a clickable hyperlink |

### Background Color — Gradient

Applies a continuous color scale between a minimum and maximum value.

1. Select **Background color**.
2. Set **Format style** to **Gradient**.
3. Define **Minimum** and **Maximum** colors and their corresponding values.

Result: cells shade from one color to another proportionally.

### Background Color — Rules

Applies discrete color based on threshold rules.

1. Set **Format style** to **Rules**.
2. Add rules: if value is **between X and Y**, color is **green**.
3. Stack multiple rules — they are evaluated top-to-bottom.

### Data Bars

Renders a fill bar inside each cell proportional to its value relative to the column range.

* Set **Minimum** and **Maximum** bar values.
* Choose **Positive** and **Negative** bar colors.
* Enable **Show bar only** to hide the text value.

### Icons

Displays icons (up/down arrows, circles, flags, etc.) alongside or instead of the value.

1. Define the number of **icon sets** (3, 4, or 5 icons).
2. Set threshold rules for each icon.
3. Choose **Icon layout**: Left of data, Right of data, or Data only.

> **Reference:** [Conditional formatting in Power BI visuals – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-conditional-formatting)

---

## Specific Column Overrides

Under **Format visual › Specific columns**, you can override formatting for a single column independently of the rest:

* Select the column name from the dropdown.
* Change font, background, alignment, display units, and decimal places for that column only.

---

## Totals Row Formatting

Under **Format visual › Totals**:

* Toggle the totals row on or off.
* Set a separate **background color** and **font color** for the total row.
* Adjust **font size** and **bold** independently of body cells.

---

## Best Practices

* Use **alternating row colors** for tables with many rows — it reduces the chance of reading the wrong row.
* Apply **background color conditional formatting** to KPI columns so under-performers stand out immediately.
* Keep conditional formatting consistent across related tables in the same report.
* Reserve **data bars** for a single key metric column — too many bars create visual noise.
* Use **specific column overrides** to right-align numeric columns and left-align text columns.

---

## References

* [Create and Format Table Visualizations – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-tables)
* [Apply Conditional Table Formatting – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-conditional-table-formatting)
* [Conditional formatting in Power BI visuals – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-conditional-formatting)
* [Expression-based titles in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-conditional-format-visual-titles)
