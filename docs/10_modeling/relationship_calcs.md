# Relationship Calculations in DAX

## Overview

Relationships in the data model are not just for visual filtering — they also enable DAX to navigate between tables programmatically. Understanding how DAX traverses relationships allows you to write measures that aggregate across related tables, pull attributes from dimension tables, and handle complex multi-relationship scenarios.

> **Reference:** [Relationships in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-relationships-understand)

---

## How DAX Uses Relationships

When you write `SUM(Sales[Revenue])` in a measure and place it in a visual that has `Products[Category]` on the axis, Power BI automatically uses the relationship between `Sales` and `Products` to compute the sum for each category. You do not need to write a JOIN — the relationship does the filtering for you.

This is **automatic relationship traversal** — the active relationship between tables is used transparently whenever a filter flows from a dimension to a fact table.

---

## RELATED — Pull from One Side

`RELATED(column)` retrieves a value from the one-side of a relationship into a calculated column on the many-side:

```dax
Product Category = RELATED(Products[Category])
```

This adds the category name to every row in the Sales table by looking up the Product ID through the relationship.

### Requirements for RELATED

* Must be used in a **calculated column** (not a measure).
* Works from the **many side** (fact) to the **one side** (dimension).
* A valid active relationship must exist between the tables on the key columns.

> **Reference:** [RELATED function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/related-function-dax)

---

## RELATEDTABLE — Pull from Many Side

`RELATEDTABLE(table)` retrieves all rows from the many-side table that are related to the current row:

```dax
Orders Per Customer = COUNTROWS(RELATEDTABLE(Orders))
```

Used in a calculated column on the Customers table, this counts how many orders each customer has.

`RELATEDTABLE` works from the **one side** (dimension) to the **many side** (fact).

> **Reference:** [RELATEDTABLE function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/relatedtable-function-dax)

---

## USERELATIONSHIP — Activating Inactive Relationships

When a fact table has multiple date columns (Order Date, Ship Date, Due Date) that all relate to the Date table, only one relationship can be active. `USERELATIONSHIP` activates an inactive relationship within a specific measure:

```dax
Revenue by Ship Date = CALCULATE(
    [Total Revenue],
    USERELATIONSHIP(Sales[Ship Date], 'Date'[Date])
)
```

```dax
Revenue by Due Date = CALCULATE(
    [Total Revenue],
    USERELATIONSHIP(Sales[Due Date], 'Date'[Date])
)
```

Both measures can exist simultaneously in the same report. The active relationship (usually Order Date) is used by default; these measures override that for their specific context.

### Important: USERELATIONSHIP with time intelligence

When combining `USERELATIONSHIP` with time intelligence functions, both must be inside the same `CALCULATE`:

```dax
Shipped Revenue YTD = CALCULATE(
    [Total Revenue],
    DATESYTD('Date'[Date]),
    USERELATIONSHIP(Sales[Ship Date], 'Date'[Date])
)
```

> **Reference:** [USERELATIONSHIP function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/userelationship-function-dax)

---

## CROSSFILTER — Changing Filter Direction in a Measure

`CROSSFILTER` modifies the cross-filter direction of a relationship within a CALCULATE expression:

```dax
Products with Sales = CALCULATE(
    DISTINCTCOUNT(Products[ProductID]),
    CROSSFILTER(Sales[ProductID], Products[ProductID], BOTH)
)
```

This temporarily enables bidirectional filtering for the expression — counting only products that appear in the Sales table.

`CROSSFILTER(left_column, right_column, direction)` where direction is `NONE`, `ONEWAY`, `BOTH`, or `ONEWAY_RIGHTFILTERSLEFT`.

> **Reference:** [CROSSFILTER function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/crossfilter-function-dax)

---

## Relationship Calculations in Measures vs Columns

| Function | In Calculated Column | In Measure |
| --- | --- | --- |
| `RELATED()` | Yes — row context | No — no row context in measures |
| `RELATEDTABLE()` | Yes | Via CALCULATE with a table filter |
| `USERELATIONSHIP()` | No | Yes — inside CALCULATE |
| `CROSSFILTER()` | No | Yes — inside CALCULATE |

---

## Role-Playing Dimensions

A **role-playing dimension** is a single dimension table used in multiple roles via different relationships. The Date table is the classic example:

* `Sales[Order Date]` → `Date[Date]` (active)
* `Sales[Ship Date]` → `Date[Date]` (inactive)
* `Sales[Due Date]` → `Date[Date]` (inactive)

All three relationships point to the same Date table. Slicers on `Date[Year]` use the active relationship by default; `USERELATIONSHIP` enables the inactive ones in specific measures.

For reports that need to simultaneously filter by multiple date roles, create separate **view tables** using `TREATAS` or duplicate the Date table:

```dax
Ship Date = TREATAS(VALUES('Date'[Date]), Sales[Ship Date])
```

---

## Debugging Relationship Issues

When a measure returns unexpected blanks or incorrect totals, check:

1. **Is the relationship active?** — Check in Manage relationships.
2. **Is cardinality correct?** — A one-to-one set as many-to-one may silently miscalculate.
3. **Is cross-filter direction correct?** — Single direction only filters from dimension to fact.
4. **Are there unmatched keys?** — Use `ISBLANK(RELATED(...))` to identify orphaned fact rows.

```dax
Has Matching Product = NOT(ISBLANK(RELATED(Products[ProductID])))
```

Place this calculated column in the fact table to identify rows with no matching dimension record.

---

## Best Practices

* Keep relationships **active** for your primary date key and use `USERELATIONSHIP` for secondary keys.
* Avoid bidirectional relationships in the model settings — prefer `CROSSFILTER` in specific measures.
* Document all inactive relationships in your model documentation (what they represent, which measures use them).
* Use `RELATED` in calculated columns to **denormalize** key dimension attributes into fact tables when needed for slicers.

---

## References

* [Relationships in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-relationships-understand)
* [RELATED function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/related-function-dax)
* [RELATEDTABLE function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/relatedtable-function-dax)
* [USERELATIONSHIP function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/userelationship-function-dax)
* [CROSSFILTER function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/crossfilter-function-dax)
