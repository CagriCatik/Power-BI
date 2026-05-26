# Relationships and Data Modeling

## Overview

The **data model** in Power BI is the foundation that connects multiple tables and enables cross-table calculations. Relationships define how tables are joined — they allow DAX measures to traverse from a fact table to a dimension table, enable slicers to filter across tables, and make the entire model behave as a single integrated dataset.

> **Reference:** [Relationships in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-relationships-understand)

---

## What Is a Relationship?

A relationship is a link between two tables based on a common column (the key). When a relationship exists between `Sales[ProductID]` and `Products[ProductID]`, a filter applied on the Products table automatically propagates to the Sales table — allowing visuals to show sales broken down by product attributes.

Power BI uses the **VertiPaq** columnar engine to evaluate relationships at query time. Relationships are not physical joins (like SQL JOIN); they are virtual filter propagation paths.

---

## Section Contents

| Topic | Description |
| --- | --- |
| Creating and Managing Relationships | Relationship properties, cardinality, filter direction, Model view |
| Relationship Calculations | How DAX traverses relationships; RELATED, RELATEDTABLE, USERELATIONSHIP |
| Introduction to Power Query | The M formula language and query editor basics |
| Basic Transformations Part 1 | Renaming, data types, removing columns, filtering rows |
| Basic Transformations Part 2 | Merging, appending, pivot/unpivot, conditional columns |
| Summary Tables | SUMMARIZE, ADDCOLUMNS, GROUPBY — creating aggregated tables in DAX |

---

## Star Schema vs Flat Table

Power BI performs best with a **star schema** model — one or more fact tables surrounded by dimension tables:

| Design | Description | Performance |
| --- | --- | --- |
| Star schema | Fact tables relate to dimension tables via foreign keys | Best — optimized for VertiPaq |
| Snowflake schema | Dimensions further normalized into sub-dimensions | Acceptable with care |
| Flat / wide table | All columns in a single table, no relationships | Poor — duplicated data, slow compression |

Always prefer star schema. Flatten snowflake dimensions into single dimension tables where possible.

---

## Prerequisites

Before working through this section you should be familiar with:

* Power BI Desktop **Model view** (the diagram view showing tables and relationships).
* Basic DAX — measures, calculated columns, CALCULATE.
* The difference between fact tables and dimension tables.

---

## References

* [Relationships in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-relationships-understand)
* [Star schema guidance for Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)
* [Power Query overview – Microsoft Learn](https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query)
