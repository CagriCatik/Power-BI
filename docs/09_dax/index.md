# Introduction to Calculated Columns

## Overview

**Calculated columns** are a core feature of Power BI's data model. A calculated column is a new column you add to an existing table using a **DAX (Data Analysis Expressions)** formula. Unlike a column added during data import in Power Query, a calculated column is computed inside the data model at refresh time and stored in memory as part of the table.

> **Reference:** [Calculated columns in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-calculated-columns)

---

## Calculated Columns vs Measures

Understanding the distinction between calculated columns and measures is fundamental to DAX modeling:

| Property | Calculated Column | Measure |
| --- | --- | --- |
| Where stored | In the table (row-level) | Not stored — computed on the fly |
| Calculated when | At data refresh | At query time (when visual renders) |
| Row context | Yes — operates row by row | No (uses filter context instead) |
| Can be used as a slicer/filter | Yes | No |
| Memory usage | Consumes model memory | No additional memory cost |
| Best for | Row-level categorization, lookup values | Aggregations, KPIs, ratio calculations |

Use a **calculated column** when you need a row-level attribute to classify, categorize, or concatenate data. Use a **measure** when you need an aggregated value that responds to filters.

---

## When to Use Calculated Columns

Common scenarios where calculated columns are the right choice:

* **Concatenating fields** — combining first name and last name into a full name column.
* **Bucketing / banding** — categorizing sales amounts into "Low", "Medium", "High" tiers.
* **Date part extraction** — extracting the year, month name, or weekday from a date column.
* **Lookup values from another table** — using RELATED() to bring a column from a related table into the current table.
* **Flag columns** — adding a 0/1 binary flag for conditional logic (e.g., `IsHighValue = IF([Sales] > 10000, 1, 0)`).

---

## Section Contents

This section covers the following topics:

| Topic | Description |
| --- | --- |
| DAX Calculated Columns | Syntax, row context, RELATED(), and examples |
| Date Functions | DAX date functions: YEAR, MONTH, DAY, DATE, DATEDIFF |
| Formatting Dates | Format strings, FORMAT(), custom date display |
| Date Master Tables | Building a complete date dimension table using DAX |

---

## Prerequisites

Before working through this section you should be familiar with:

* The Power BI Desktop **Data** view and **Model** view.
* Basic DAX syntax — operators, IF(), and simple arithmetic.
* The concept of **relationships** between tables.

> **Reference:** [Data Analysis Expressions (DAX) reference – Microsoft Learn](https://learn.microsoft.com/en-us/dax/)

---

## References

* [Calculated columns in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-calculated-columns)
* [Data Analysis Expressions (DAX) reference – Microsoft Learn](https://learn.microsoft.com/en-us/dax/)
