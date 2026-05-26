# Visual Level Filters — Date

## Overview

A **date visual-level filter** restricts a single visual to rows within a specific date range or matching a date condition. It is useful when one visual on a page needs a different date scope than others — for example, one chart showing the full year while another shows only Q4.

> **Reference:** [Add a Filter to a Report in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-report-add-filter)

---

## Adding a Date Visual Filter

1. Select the visual.
2. In the **Filters pane**, look for **Filters on this visual**.
3. Drag a **date column** from the **Fields pane** into the section.
4. Expand the filter card.

---

## Filter Modes for Date Fields

### Basic Filtering (Date List)

Shows unique date values as checkboxes. Only useful for very small date ranges — not practical for a column with thousands of distinct dates.

For date hierarchies (Year/Quarter/Month), the list shows the hierarchy levels and lets you select individual months, quarters, or years.

### Advanced Filtering

Provides date condition rules:

| Condition | Meaning |
| --- | --- |
| **Is** | Exact date match |
| **Is not** | Excludes an exact date |
| **Is before** | All dates before the entered date |
| **Is before or on** | All dates on or before |
| **Is after** | All dates after the entered date |
| **Is after or on** | All dates on or after |
| **Is blank** | Null date values |
| **Is not blank** | Non-null dates |

Combine two conditions:

* **Between:** Is after or on `<start>` **And** Is before or on `<end>`.
* **Exclude period:** Is before `<date>` **Or** Is after `<date>`.

### Relative Date Filtering

In the filter card, switch to **Relative date** filter type:

1. Choose **In the last**, **In this**, or **In the next**.
2. Enter a number.
3. Choose the period: Days, Weeks, Months, Quarters, Years.
4. Toggle **Include today** if needed.
5. Click **Apply filter**.

This works identically to the relative date slicer but is invisible to consumers.

---

## Practical Use Case

A dashboard has two line charts on the same page:

* **Chart A** — shows a 5-year revenue trend (needs full historical data).
* **Chart B** — shows the last 90 days in detail.

A single date slicer would affect both charts. Instead:

* Leave Chart A with no date visual filter.
* Add a date visual filter to **Chart B**: Relative date → In the last 90 Days.

Both charts display their intended scope simultaneously regardless of any page-level date slicer.

---

## Date Filter vs Date Slicer

| Aspect | Date visual filter | Date slicer |
| --- | --- | --- |
| Visible to consumer | No | Yes |
| Affects | One visual | All visuals (by default) |
| Consumer can change | Only if unlocked | Always |
| Relative date support | Yes | Yes |
| Different scopes per visual | Yes | No (affects all) |

---

## Best Practices

* Use date visual filters to give **each visual its own time scope** when a single date slicer would be too restrictive.
* Use the **relative date** filter mode for charts that should always show a fixed rolling window (e.g., last 12 months).
* **Lock and hide** date visual filters when they encode business rules the consumer should not override.
* Combine with a **date slicer** — the visual filter narrows the scope, and the slicer lets the user zoom within that scope.

---

## References

* [Add a Filter to a Report in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-report-add-filter)
* [Filters and highlighting in Power BI reports – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-reports-filters-and-highlighting)
* [Create a relative time slicer or filter – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/slicer-filter-relative-time)
