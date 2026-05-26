# Introduction to Filters and Slicers

## Overview

Filtering is the mechanism by which a user or report designer restricts the data visible in a report. Power BI provides multiple filtering layers — from interactive slicers on the canvas to hidden filters in the Filters pane — giving you precise control over what each visual shows and how users can interact with the data.

> **Reference:** [Filters and highlighting in Power BI reports – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-reports-filters-and-highlighting)

---

## Filter Hierarchy

Power BI applies filters in a hierarchy. Each level is additive — a lower-level filter cannot show data that has been excluded by a higher-level filter.

| Level | Scope | Who sets it |
| --- | --- | --- |
| **Report filter** | All pages in the report | Report designer |
| **Page filter** | One specific page | Report designer |
| **Visual filter** | One specific visual | Report designer |
| **Slicer** | All visuals on the page (by default) | Report consumer |
| **Cross-filter** | Temporary, from clicking another visual | Report consumer |

> **Reference:** [Add a Filter to a Report in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-report-add-filter)

---

## The Filters Pane

The **Filters pane** is the panel on the right side of the report canvas (in edit mode). It has three sections:

### Filters on this visual

Appears when a visual is selected. Filters here apply only to that visual and are invisible to consumers by default.

### Filters on this page

Applies to every visual on the current page. Report consumers can see and interact with these filters if you leave them visible.

### Filters on all pages

Applies to the entire report. Useful for locking a report to a specific date range or a single business unit.

### How to Add a Filter

1. Click the visual (for visual-level) or click an empty area of the canvas (for page/report level).
2. Drag a field from the **Fields pane** into the appropriate section of the **Filters pane**.
3. Set the filter condition: **Basic filtering** (checkboxes) or **Advanced filtering** (conditions like "contains", "is greater than").

---

## Slicers

A **slicer** is a visual placed on the canvas that filters other visuals on the page. Unlike the Filters pane, slicers are visible to report consumers and provide a self-service filtering experience.

### Slicer vs Filter Pane

| Feature | Slicer | Filters pane |
| --- | --- | --- |
| Visible to consumer | Yes | Optional |
| Canvas space required | Yes | No |
| Interactable by consumer | Yes | Yes (if not locked) |
| Supports all field types | Text, Numeric, Date | All |
| Can sync across pages | Yes | No |

---

## Slicer Types

Power BI automatically chooses a slicer style based on the field type:

| Field type | Default slicer style |
| --- | --- |
| Text / Category | Vertical list with checkboxes |
| Numeric | Between slider |
| Date | Date range picker (calendar) |

You can change the slicer style via **Format visual › Slicer settings › Style**:

* **Vertical list** — checkboxes stacked
* **Horizontal list** — checkboxes side by side (good for few values)
* **Dropdown** — compact; expands on click
* **Tile** — button-style tiles
* **Between / Before / After** — range controls for numeric and date fields
* **Relative date / Relative time** — dynamic date filters

> **Reference:** [Slicers in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-slicers)

---

## Slicer Selection Modes

| Mode | Behavior |
| --- | --- |
| **Single select** | Only one value can be selected at a time |
| **Multi-select** | Multiple values selected (Ctrl+click or checkbox) |
| **Select all** | Checkbox at the top selects/deselects all values |

Configure under **Format visual › Slicer settings › Selection**.

---

## Sync Slicers Across Pages

A slicer can filter visuals on other report pages — useful for a consistent "Year" or "Region" filter across an entire report.

1. Select the slicer.
2. Go to **View › Sync slicers**.
3. In the Sync slicers pane, toggle on which pages the slicer should **sync** (filter) and which pages it should **show** (be visible on).

> **Reference:** [Slicers in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-slicers)

---

## Clearing Filters

* **Consumer:** Click the eraser icon that appears on hover at the top-right of a slicer, or use **Reset to default** on the toolbar.
* **Designer:** Remove filters from the Filters pane by clicking the **×** on each filter card.

---

## Best Practices

* Place slicers in a **consistent position** on every page (e.g., top bar or left panel) so consumers always know where to find them.
* Use **sync slicers** for global filters like Year or Region to avoid rebuilding the same slicer on every page.
* **Lock** filters in the Filters pane that consumers should not change (click the lock icon on the filter card).
* Use **dropdown slicers** for fields with many values to save canvas space.
* Avoid putting more than **three or four slicers** on a single page — too many choices can overwhelm users.

---

## References

* [Filters and highlighting in Power BI reports – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-reports-filters-and-highlighting)
* [Add a Filter to a Report – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-report-add-filter)
* [Slicers in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-slicers)
* [Filter Data in Power BI Reports – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/explore-reports/end-user-report-filter)
