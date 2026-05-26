# Introduction to Measures

## Overview

**Measures** are the primary calculation mechanism in Power BI. A measure is a DAX formula that computes a result dynamically based on the **filter context** — the combination of slicers, filters, and visual dimensions that are active when the measure is evaluated. Unlike calculated columns, measures are not stored in the model; they are recomputed on demand each time a visual renders.

> **Reference:** [Measures in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-measures)

---

## What Makes Measures Different

| Property | Measure | Calculated Column |
| --- | --- | --- |
| Computed when | At query time (visual render) | At data refresh |
| Responds to filters/slicers | Yes — automatically | No |
| Row context | No (uses filter context) | Yes |
| Memory usage | None — no storage | Stored in model memory |
| Visible in Fields pane | Yes (calculator icon) | Yes (sigma or column icon) |
| Can be used as slicer | No | Yes |

---

## Filter Context

The most important concept for understanding measures is **filter context**. When Power BI renders a bar chart showing Sales by Region, each bar is evaluated with a different filter context — the measure `[Total Sales]` computes the total for "North", then "South", then "East", etc. The measure formula does not change; the filter context changes.

Slicers, report/page/visual filters, and the dimensions placed on a visual's axes all contribute to the filter context. Writing effective measures means understanding how to work with, modify, and override that filter context.

---

## Section Contents

| Topic | Description |
| --- | --- |
| Intro to DAX Measures | Creating measures, implicit vs explicit, naming conventions |
| DAX Measures Activity | Hands-on practice with SUM, COUNT, AVERAGE, DIVIDE |
| DAX Measures — Completed | Reference solutions with explanations |
| CALCULATE Formula | Modifying filter context with CALCULATE and FILTER |
| DAX Query View | Writing and testing DAX queries directly in Power BI Desktop |

---

## Implicit vs Explicit Measures

When you drag a numeric column into a visual, Power BI automatically creates an **implicit measure** — a quick aggregation (usually SUM) applied to that column. Implicit measures are convenient but have limitations:

* They cannot be reused across visuals by name.
* They do not appear in the Fields pane as named items.
* They cannot use CALCULATE or other context-modifying functions.

**Explicit measures** are defined via **New measure** in the Modeling ribbon, given a name, and are reusable across all visuals in the report.

Best practice: always create explicit measures for any calculation you need more than once or that requires DAX beyond a simple aggregation.

---

## Prerequisites

Before working through this section you should understand:

* The difference between **fact tables** (transactions, events) and **dimension tables** (products, customers, dates).
* How **relationships** connect tables in the model view.
* The basic structure of a DAX formula.

---

## References

* [Measures in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-measures)
* [Data Analysis Expressions (DAX) reference – Microsoft Learn](https://learn.microsoft.com/en-us/dax/)
* [Understand filter context in DAX – SQLBI](https://www.sqlbi.com/articles/filter-context-in-dax/)
