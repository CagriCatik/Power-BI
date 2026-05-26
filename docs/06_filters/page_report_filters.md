# Page and Report Level Filters

## Overview

Beyond visual-level filters and slicers, Power BI supports **page-level** and **report-level** filters that apply silently across multiple visuals simultaneously. These filters are set by the report designer and can be hidden or locked to enforce data governance rules.

> **Reference:** [Add a Filter to a Report in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-report-add-filter)
> **Reference:** [Filters and highlighting in Power BI reports – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-reports-filters-and-highlighting)

---

## Page-Level Filters

A **page filter** applies to every visual on one specific report page. It is the equivalent of adding the same visual-level filter to every visual on the page — but managed in a single place.

### Adding a Page Filter

1. Click an **empty area** of the canvas (deselect all visuals).
2. In the **Filters pane**, look for the **Filters on this page** section.
3. Drag a column or measure from the **Fields pane** into that section.
4. Configure the filter condition (Basic, Advanced, Top N, or Relative date).
5. Click **Apply filter**.

All visuals on the page now show data constrained by this filter.

### Use Cases

* A "Q4 Performance" page that should only ever show Q4 data.
* A regional page locked to one country, preventing consumers from seeing other regions.
* A page filtered to "Active Customers Only" without a visible slicer cluttering the layout.

---

## Report-Level Filters

A **report filter** applies to every page in the entire report.

### Adding a Report Filter

1. Click an empty area of the canvas.
2. In the **Filters pane**, look for the **Filters on all pages** section.
3. Drag a column or measure into that section.
4. Configure and apply the filter.

Every page and every visual in the report now filters to the configured scope.

### Report Filter Use Cases

* Restricting a shared report to a single business unit without building separate reports.
* Setting a global date window (e.g., "Only show data from the last 3 years").
* Hiding confidential categories from all pages simultaneously.

---

## Visibility and Lock Controls

Each filter card in the Filters pane has two controls at the top-right:

| Control | Icon | Function |
| --- | --- | --- |
| **Visibility** | Eye | Show or hide the filter card from consumers |
| **Lock** | Padlock | Prevent consumers from modifying or removing the filter |

Combining **hidden + locked** creates an invisible, unmodifiable filter — an effective way to embed business rules in the report without exposing them to consumers.

---

## Filter Interaction with Slicers

Filters in the Filters pane and slicers on the canvas both modify the filter context, and they stack:

* A page filter restricting to **Region = North**
* Plus a consumer slicer selecting **Category = Hardware**
* Results in visuals showing: North region AND Hardware category

The more restrictive the combination, the less data is shown.

---

## Persistent Filters

By default, Power BI Service saves a consumer's filter and slicer selections between sessions (**persistent filters**). When the consumer reopens the report, they see their previous selections.

Designers can disable this per-report under **File › Options and settings › Options › CURRENT FILE › Report settings › Persistent filters**.

Alternatively, a **Reset to default** button (added via **Insert › Buttons**) lets consumers restore the designer's original filter state at any time.

---

## Filter Order of Precedence

When multiple filter types are active simultaneously:

1. Report-level filters (widest — always applied)
2. Page-level filters
3. Visual-level filters
4. Slicer selections
5. Cross-filter from clicking another visual (narrowest — most temporary)

Each subsequent layer further restricts what data is visible — they do not override each other, they compound.

---

## Best Practices

* Use **report-level filters** for global constraints (e.g., exclude test data, exclude a specific tenant).
* Use **page-level filters** to give each page its own data scope without rebuilding filters on every visual.
* Always **lock** filters that represent compliance or governance requirements.
* **Hide** page/report filters from consumers when the scope is an internal design decision, not a consumer choice.
* Avoid stacking so many filters that the report becomes unusable — clearly document the active filters in a tooltip or info card on the page.

---

## References

* [Add a Filter to a Report in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-report-add-filter)
* [Filters and highlighting in Power BI reports – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-reports-filters-and-highlighting)
* [Filter Data in Power BI Reports – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/explore-reports/end-user-report-filter)
