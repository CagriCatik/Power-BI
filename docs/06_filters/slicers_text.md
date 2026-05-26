# Using Slicers — Text

## Overview

A **text slicer** filters other visuals on the page by one or more selected category values — such as Product Name, Region, or Sales Rep. It is the most common slicer type and provides a checkbox-based or dropdown interface.

> **Reference:** [Slicers in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-slicers)

---

## Adding a Text Slicer

1. Click an empty area of the canvas.
2. In the **Visualizations pane**, click the **Slicer** icon.
3. Drag a **text/category column** (e.g., Region, Category, Product) into the **Field** well.
4. Power BI renders a vertical list of checkboxes, one per unique value.

---

## Slicer Styles for Text Fields

Open **Format visual › Slicer settings › Style** to change the slicer appearance:

| Style | Best for |
| --- | --- |
| **Vertical list** | 5–15 values, needs labels |
| **Horizontal list** | 2–5 short values |
| **Dropdown** | More than 15 values, saves canvas space |
| **Tile** | Few values that act like toggle buttons |

---

## Single vs Multi-Select

### Single select (default: off)

By default, the slicer allows multiple values to be selected simultaneously (OR logic — shows data matching any selected value).

To restrict to single-select:

1. Open **Format visual › Slicer settings › Selection**.
2. Enable **Single select**.

With single select enabled, clicking a new value automatically deselects the previous one.

### Multi-select with Ctrl

When single select is **off**, consumers can:

* Click individual checkboxes to select/deselect.
* Hold **Ctrl** and click to select multiple values without checkboxes.
* Click the **Select all** checkbox (if enabled) to toggle all values.

---

## Enabling "Select All"

Under **Format visual › Slicer settings › Selection**, toggle **Show "Select all" option** on. A "Select all" checkbox appears at the top of the list.

---

## Search in Slicer

For long lists, enable the search box:

1. In the slicer visual, click the **magnifying glass** icon in the visual header (hover to see it).
2. Type to filter the list to matching values.

This is especially useful when the slicer has hundreds of unique product names.

---

## Formatting a Text Slicer

### Slicer Header

Under **Format visual › Slicer header**:

* Toggle the header on or off.
* Set custom title text (e.g., "Filter by Region").
* Change font, size, bold, italic, and background color.

### Items (List Values)

Under **Format visual › Values**:

* Font family, size, bold, italic, color.
* Background color for the item rows.
* **Show value** — toggle the text label alongside the checkbox.

### Selected Item Highlight

Under **Format visual › Slicer settings › Selection**:

* Set font color and background color for **selected** items to make chosen selections visually distinct.

---

## Controlling Which Visuals the Slicer Affects

By default, a slicer filters all visuals on the same page. To exclude specific visuals:

1. Select the slicer.
2. Go to **Format › Edit interactions**.
3. Click the **circle with line** (None) icon on any visual you want to exclude from the slicer's filter.

---

## Practical Example

Scenario: You have a sales report with a table of transactions and a bar chart of revenue by month. You add a Region slicer.

* Selecting **North** filters both the table and the bar chart to show only North region data.
* Selecting **North** + **South** shows data for both regions combined.
* Deselecting all (or clicking Select All off then on) resets to showing all regions.

---

## Best Practices

* Use a **dropdown slicer** when you have more than 15 category values — it takes less vertical space.
* Place slicers in a **header strip** at the top of the page so consumers always find them in the same place.
* Use **Select all** for slicers where the default state should be "all selected" rather than "nothing selected".
* **Sync text slicers** across pages when the same category filter should apply globally (e.g., a Region slicer on every page).

---

## References

* [Slicers in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-slicers)
* [Use Slicers in the Power BI Service – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/explore-reports/end-user-slicer)
* [Change How Visuals Interact – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/service-reports-visual-interactions)
