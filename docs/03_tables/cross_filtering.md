# Cross Filtering Tables

## Overview

**Cross-filtering** is the mechanism by which selecting a data point in one visual automatically filters or highlights the other visuals on the same report page. It is one of the most powerful interactivity features in Power BI and requires no code — it works by default between most visual types.

> **Reference:** [How visuals cross-filter each other in a Power BI report – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/explore-reports/end-user-interactions)

---

## How Cross-Filtering Works

When a user clicks a row in a table (or a bar in a chart, a slice of a pie, etc.), Power BI injects a temporary filter into the report's filter context. Every other visual on the page re-evaluates its data against that filter.

Two modes exist:

| Mode | Visual Behaviour |
| --- | --- |
| **Cross-filter** | Other visuals show only the matching rows (non-matching rows hidden) |
| **Cross-highlight** | Other visuals dim non-matching data but keep the visual structure visible |

By default, clicking a table row **cross-highlights** bar and column charts, while it **cross-filters** other table and matrix visuals.

---

## Demonstrating Cross-Filter with a Table

### Setup

1. Place a **Table visual** on the canvas with columns: Category, Region, Sales.
2. Place a **Clustered column chart** on the same page: Category on X-axis, Sales on Y-axis.

### Interaction

* Click the row for **Category = Hardware** in the table.
* The column chart highlights the Hardware bar; other bars are dimmed.
* The table itself highlights only the Hardware rows.
* Click away (or press **Esc**) to clear the selection.

---

## Editing Visual Interactions

You can control how each pair of visuals interacts:

1. Select the visual that will *drive* the filter (the source).
2. Go to **Format** ribbon tab.
3. Click **Edit interactions** — icons appear on all other visuals.

| Icon | Effect |
| --- | --- |
| Funnel (filter) | Applies cross-filter (hides non-matching data) |
| Bar chart (highlight) | Applies cross-highlight (dims non-matching data) |
| Circle with line (none) | No interaction from this source |

1. Click the desired icon on each target visual.
2. Click **Edit interactions** again to exit interaction-edit mode.

> **Reference:** [Change How Visuals Interact in a Report – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/service-reports-visual-interactions)

---

## Slicers vs Cross-Filter

Slicers always **cross-filter** (they filter, not highlight). A slicer selection removes non-matching data from all visuals it affects. A table row click, by contrast, uses cross-highlight by default for chart visuals. You can change this with Edit interactions.

---

## Multi-Select Cross-Filter

Hold **Ctrl** and click multiple rows in a table to filter/highlight by multiple values simultaneously. For example, clicking `Hardware` then `Ctrl + click` `Software` will show data for both categories in other visuals.

---

## Drill-Through vs Cross-Filter

| Feature | Scope | Mechanism |
| --- | --- | --- |
| **Cross-filter** | Same page | Click a data point |
| **Drill-through** | Navigates to another page | Right-click › Drill through |

Cross-filtering is ephemeral (clears on click-away); drill-through navigates to a dedicated detail page and persists filters until you navigate back.

---

## Best Practices

* Use **Edit interactions › None** to prevent a logo or decorative visual from triggering filters accidentally.
* Disable cross-highlighting on KPI cards if you want them to always show the grand total — set interaction to **None** from every other visual.
* Test cross-filter behavior during development by clicking every visual on the page to ensure interactions behave as expected.
* Document intended interaction patterns in a tooltip or info button on the report page.

---

## References

* [How visuals cross-filter each other – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/explore-reports/end-user-interactions)
* [Change How Visuals Interact in a Report – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/service-reports-visual-interactions)
* [Filters and highlighting in Power BI reports – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-reports-filters-and-highlighting)
