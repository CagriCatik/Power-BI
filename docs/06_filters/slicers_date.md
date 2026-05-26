# Using Slicers — Date

## Overview

A **date slicer** lets report consumers filter visuals by a date or date range. Power BI provides several date slicer modes — from fixed range pickers to dynamic relative-date filters that automatically update relative to today's date.

> **Reference:** [Slicers in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-slicers)
> **Reference:** [Create a relative time slicer or filter – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/slicer-filter-relative-time)

---

## Adding a Date Slicer

1. Click an empty area of the canvas.
2. In the **Visualizations pane**, click the **Slicer** icon.
3. Drag a **Date or Date/Time column** into the **Field** well.
4. Power BI renders a **Between** date range picker by default.

---

## Date Slicer Styles

Under **Format visual › Slicer settings › Style**:

| Style | Description |
| --- | --- |
| **Between** | Calendar pickers for start and end date |
| **Before** | All dates up to a selected date |
| **After** | All dates from a selected date onwards |
| **List** | Checkbox list of years, quarters, months (from the date hierarchy) |
| **Dropdown** | Compact dropdown of date values |
| **Relative date** | Dynamic — "Last N days/weeks/months/years" |
| **Relative time** | Dynamic — "Last N hours/minutes" (for real-time) |

---

## Between Date Picker

The default style. Shows two calendar widgets:

* Click the **left field** to set the start date.
* Click the **right field** to set the end date.
* Use the **left/right arrows** in the calendar header to navigate months.
* Click a date to select it.

Users can also type dates directly into the input boxes.

---

## Relative Date Slicer

The **relative date** style is the most powerful option for operational dashboards because it requires no manual adjustment — it always filters relative to today.

### Configuration

1. Change the slicer style to **Relative date**.
2. Set the parameters:
   * **Show items when the value** is: **In the last** / **In this** / **In the next**
   * **Number**: enter a number (e.g., 30)
   * **Period**: Days / Weeks / Calendar weeks / Months / Calendar months / Quarters / Calendar quarters / Years / Calendar years
3. Optionally enable **Include today**.

### Examples

| Setting | What it shows |
| --- | --- |
| In the last 30 Days | Rolling 30-day window ending today |
| In this Calendar month | Current calendar month (e.g., all of May 2026) |
| In the last 3 Months | Last 3 complete calendar months |
| In the next 7 Days | Next 7 days from today |

---

## Date Hierarchy in a List Slicer

If you use a **List** style with a date column that has Auto date/time enabled, the slicer shows the date hierarchy levels (Year, Quarter, Month). Consumers can expand to select individual months or entire quarters.

---

## Clearing a Date Slicer

* Hover over the slicer — click the **eraser icon** in the visual header.
* Or click the **between** input boxes and delete the values.

---

## Formatting a Date Slicer

### Date Input Format

Under **Format visual › Input**:

* Controls the format of dates shown in the input boxes (uses the locale date format by default).
* Match the format to your audience's regional expectations.

### Slicer Header

Set a custom title such as "Filter by Order Date" under **Format visual › Slicer header › Title text**.

---

## Practical Examples

### Example 1 — Fixed Range

You want users to filter a sales report by order date:

1. Add a date slicer on the Order Date column, Between style.
2. Users can pick any start and end date to view transactions in that window.

### Example 2 — Always Show Last 7 Days

For a daily operations dashboard:

1. Change style to **Relative date**.
2. Set "In the last 7 Days".
3. The dashboard always shows yesterday through 7 days ago without any manual adjustment.

### Example 3 — Year List

For an annual report where users select one or more full years:

1. Use **List** style on the year column of a dedicated date dimension.
2. Enable multi-select so users can compare two years side by side.

---

## Best Practices

* Use **relative date** slicers on operational dashboards — they stay current automatically.
* For historical analysis, use the **Between** style so users can pick any arbitrary range.
* Sync date slicers across pages so the selected period applies to the entire report.
* Combine a date slicer with a **line chart** so the trend immediately reflects the selected period.

---

## References

* [Slicers in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-slicers)
* [Create a relative time slicer or filter – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/slicer-filter-relative-time)
* [Use Slicers in the Power BI Service – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/explore-reports/end-user-slicer)
