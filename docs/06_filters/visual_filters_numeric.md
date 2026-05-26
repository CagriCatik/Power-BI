# Visual Level Filters — Numeric

## Overview

A **numeric visual-level filter** restricts a visual to rows where a numeric column or measure satisfies a mathematical condition — for example, only showing sales greater than $10,000, or products with a profit margin between 10% and 30%.

> **Reference:** [Add a Filter to a Report in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-report-add-filter)

---

## Adding a Numeric Visual Filter

1. Select the visual.
2. In the **Filters pane**, locate **Filters on this visual**.
3. Drag a numeric column or measure from the **Fields pane** into the filter section.
4. Expand the filter card to configure it.

---

## Filter Modes for Numeric Fields

### Basic Filtering

Shows a list of all distinct numeric values with checkboxes. Only practical for low-cardinality numeric fields (e.g., a rating 1–5 or a status code 0/1).

### Advanced Filtering

Provides condition-based filtering with two rule slots:

| Condition | Meaning |
| --- | --- |
| **Is less than** | Value < threshold |
| **Is less than or equal to** | Value ≤ threshold |
| **Is greater than** | Value > threshold |
| **Is greater than or equal to** | Value ≥ threshold |
| **Is** | Exact match |
| **Is not** | Not equal to |
| **Is blank** | Null values only |
| **Is not blank** | Non-null values only |

Combine two conditions with **And** (range filter) or **Or** (exclude a specific range).

**Range example:** Sales Amount **is greater than or equal to** 10000 **And** Sales Amount **is less than or equal to** 50000 → shows only rows between $10K and $50K.

### Top N Filter

Filters to the top or bottom N items by a measure value:

1. Change filter type to **Top N**.
2. Set **Show: Top** (or Bottom) and **N** (e.g., 10).
3. Drag a measure into the **By value** field.
4. Click **Apply filter**.

This is a powerful way to focus a chart on the most or least significant contributors without a complex DAX formula.

---

## Filtering by a Measure

Unlike slicers (which only accept columns), visual-level filters accept **DAX measures**. This allows you to filter a visual by calculated metrics that do not exist as a column:

1. Drag a measure (e.g., **Profit Margin %**) into the filter section.
2. Use **Advanced filtering** to set a threshold (e.g., Profit Margin % **is greater than** 0.15).
3. The visual shows only items where the profit margin exceeds 15%.

This is one of the few places in Power BI where you can directly filter by a measure value.

---

## Practical Example

You have a bar chart showing revenue by salesperson, but you only want to show salespeople who exceeded quota ($100,000):

1. Drag **Sales Amount** into the visual filter.
2. Set: Advanced filtering → **Is greater than or equal to** → 100000.
3. Click **Apply filter**.

The chart now shows only high-performing salespeople, without changing any other visual on the page.

---

## Numeric Filter vs Numeric Slicer

| Aspect | Visual-level numeric filter | Numeric slicer |
| --- | --- | --- |
| Visible to consumer | No (hidden in pane) | Yes (on canvas) |
| Works with measures | Yes | No |
| Consumer can adjust | Only if unlocked | Always |
| Advanced conditions | Yes | No (slider only) |

---

## Best Practices

* Use **Top N** numeric filters on bar charts to display only the most significant items and reduce visual clutter.
* Use **measure filters** to apply business logic thresholds (e.g., only show products with a margin above a breakeven point).
* **Lock** numeric visual filters that represent data governance rules so consumers cannot inadvertently remove them.

---

## References

* [Add a Filter to a Report in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-report-add-filter)
* [Filters and highlighting in Power BI reports – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-reports-filters-and-highlighting)
