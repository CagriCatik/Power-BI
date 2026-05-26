# Answers to Tables Practical Activity

## Overview

This page provides the expected outcomes and guidance for each task in the Tables Practical Activity. Use it to verify your work or to understand the correct approach if you encountered difficulties.

---

## Task 1 — Create a Basic Table

### Steps taken

1. Added a new report page named "Tables Activity".
2. Selected the **Table** visual icon in the Visualizations pane.
3. Added fields in order: Product → Category → Region → Sales → Units.
4. Clicked the **Sales** column header once — the arrow pointed up (ascending). Clicked again — arrow pointed down (descending). Table now shows highest-sales products first.

**Key point:** Sorting is applied per visual and is saved with the report. When a user opens the report, they will see the table already sorted descending by Sales.

---

## Task 2 — Apply a Style Preset

**Format visual › Style presets › Alternating rows**

The banded row effect alternates between white and a light grey or the accent color defined in your report theme. This is purely cosmetic — it does not change data or filtering behavior.

---

## Task 3 — Format Column Headers

**Settings applied:**

| Setting | Value |
| --- | --- |
| Background color | `#333333` (dark grey) |
| Font color | `#FFFFFF` (white) |
| Font size | 12 |
| Bold | On |

**Troubleshooting:** If the header color is not changing, ensure you are in the **Format visual** tab (paint roller), not the **Build visual** tab.

---

## Task 4 — Conditional Formatting on Sales

**Full path:** Columns well → Sales chevron → Conditional formatting → Background color

| Setting | Value |
| --- | --- |
| Format style | Gradient |
| Minimum color | `#FFFFFF` (white) |
| Maximum color | `#107C10` (green) |
| Minimum value | (Lowest) |
| Maximum value | (Highest) |

The gradient uses the minimum and maximum values in the currently visible rows. If you filter the table via a slicer, the gradient re-scales to the filtered range — this is expected behavior.

**Alternative:** If you wanted a fixed scale (e.g., always 0 = white, 100,000 = green), set explicit number values for Minimum and Maximum instead of leaving them as "Lowest/Highest".

---

## Task 5 — Add a Data Bar to Units

**Full path:** Columns well → Units chevron → Conditional formatting → Data bars

Data bars scale relative to the column minimum and maximum visible in the table. A product with 0 units sold shows no bar; the product with the most units sold shows a full-width bar.

**Tip:** Enable **Show bar only** (under data bar settings) if you want a sparkline-like effect without the number cluttering the cell.

---

## Task 6 — Cross-Filtering

**Expected behavior:**

* Clicking a bar in the column chart highlights matching rows in the table and dims the others.
* The table totals row updates to reflect only the filtered records.
* Right-clicking a bar and selecting **Keep only this** applies a persistent filter.

**How cross-filtering works:** By default, Power BI enables cross-highlighting between visuals on the same page. When you click a data point, the other visuals re-evaluate their data against the implicit filter created by that selection.

> **Reference:** [How visuals cross-filter each other in a Power BI report – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/explore-reports/end-user-interactions)

To change cross-filter behavior between two specific visuals:

1. Select the visual you want to change interaction from.
2. Go to **Format › Edit interactions**.
3. On other visuals, toggle between **Filter** (funnel icon), **Highlight** (bar icon), or **None** (circle with line).

---

## References

* [Create and Format Table Visualizations – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-tables)
* [How visuals cross-filter each other – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/explore-reports/end-user-interactions)
* [Change How Visuals Interact in a Report – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/service-reports-visual-interactions)
