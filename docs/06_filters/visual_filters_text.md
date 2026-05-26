# Visual Level Filters — Text

## Overview

**Visual-level filters** restrict the data shown in a single visual without affecting any other visual on the page. A text visual-level filter is applied to a category or text column and uses condition-based or list-based filtering to include or exclude specific values.

> **Reference:** [Add a Filter to a Report in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-report-add-filter)
> **Reference:** [Filter Data in Power BI Reports – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/explore-reports/end-user-report-filter)

---

## Accessing Visual-Level Filters

1. Select the visual you want to filter.
2. In the **Filters pane** (right side), look for the **Filters on this visual** section.
3. Drag a text/category column from the **Fields pane** into this section.
4. The filter card expands with options.

---

## Filter Modes for Text Fields

### Basic Filtering

Displays a checkbox list of all unique values in the column. Check or uncheck values to include or exclude them.

* **Select all** — includes all values (no filter applied).
* Unchecking a value excludes rows with that value from the visual.
* Unchecking all values shows no data.

### Advanced Filtering

Click **Advanced filtering** in the filter card to use condition-based rules:

| Condition | Meaning |
| --- | --- |
| **Contains** | Value includes the typed text anywhere |
| **Does not contain** | Value does not include the typed text |
| **Starts with** | Value begins with the typed text |
| **Does not start with** | Value does not begin with the typed text |
| **Is** | Exact match |
| **Is not** | Excludes exact match |
| **Is blank** | Null or empty values only |
| **Is not blank** | Non-null, non-empty values only |

Combine two conditions with **And** (both must be true) or **Or** (either can be true).

**Example:** Show only products where Category **contains** "Hardware" **or** Category **is** "Software".

---

## Applying the Filter

After setting conditions, click **Apply filter** at the bottom of the filter card. The visual immediately updates.

---

## Filter vs Slicer — Text Comparison

| Aspect | Visual-level filter | Text slicer |
| --- | --- | --- |
| Visible to consumer | No (hidden in pane) | Yes (on canvas) |
| Applies to | One visual | All visuals on page |
| Consumer can change | Only if pane is unlocked | Always |
| Advanced conditions | Yes | No |

Use visual-level filters when you need to **permanently restrict** what a visual shows (e.g., a chart that should only ever show the Top 3 categories). Use slicers when you want consumers to interactively choose which categories to view.

---

## Top N Filter (Text)

A special filter type — **Top N** — available when a text field is combined with a numeric measure:

1. In the filter card, change filter type to **Top N**.
2. Set **Show**: Top or Bottom.
3. Set **N**: the number of items (e.g., 5).
4. Drag a measure into the **By value** field (e.g., Sales).
5. Click **Apply filter**.

Result: the visual shows only the top (or bottom) N items by the specified measure.

**Example:** Show only the top 5 products by total sales in a bar chart.

---

## Locking and Hiding Filters

In the Filters pane, each filter card has two icons:

* **Eye icon** — toggles visibility for report consumers (hide a filter so consumers do not know it exists).
* **Lock icon** — prevents consumers from modifying the filter.

Use both together to create a **read-only, invisible** filter that constrains a visual without the consumer being able to change or see it.

---

## Best Practices

* Use visual-level filters with **Top N** to keep bar and column charts focused on the most relevant items rather than showing all 50+ categories.
* **Hide and lock** visual-level filters that represent business rules (e.g., "only show active products") so consumers cannot accidentally remove them.
* Combine **Advanced filtering** with the "contains" condition for fuzzy matching when values are inconsistently named.

---

## References

* [Add a Filter to a Report in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-report-add-filter)
* [Filters and highlighting in Power BI reports – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-reports-filters-and-highlighting)
* [Filter Data in Power BI Reports – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/explore-reports/end-user-report-filter)
