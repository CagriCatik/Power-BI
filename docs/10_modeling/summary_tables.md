# Summary Tables in DAX

## Overview

**Summary tables** (also called aggregated calculated tables) are tables you create inside the DAX layer using functions like `SUMMARIZE`, `ADDCOLUMNS`, `SUMMARIZECOLUMNS`, or `GROUPBY`. They are used to pre-aggregate data for performance optimization, to create intermediate lookup tables, or to support specialized analysis patterns that require a tabular result.

> **Reference:** [SUMMARIZE function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/summarize-function-dax)

---

## Creating a Calculated Table

A **calculated table** is a table in the data model that is defined entirely by a DAX expression rather than loaded from a data source:

1. In Power BI Desktop, go to the **Modeling** ribbon tab.
2. Click **New table**.
3. Enter the table name and a DAX expression that returns a table:

```dax
Sales Summary = SUMMARIZE(
    Sales,
    'Date'[Year],
    Products[Category],
    "Total Revenue", SUM(Sales[Revenue]),
    "Order Count", DISTINCTCOUNT(Sales[OrderID])
)
```

4. Press **Enter**. The table is added to the model and can be related to other tables or used directly in visuals.

---

## SUMMARIZE

`SUMMARIZE(table, groupBy_column1, ..., [name, expression, ...])` groups a table by the specified columns and optionally adds aggregated measure expressions:

```dax
Category Summary = SUMMARIZE(
    Sales,
    Products[Category],
    "Revenue", SUM(Sales[Revenue]),
    "Units", SUM(Sales[Quantity])
)
```

> **Important:** Adding aggregation expressions directly in `SUMMARIZE` is deprecated in favor of using `ADDCOLUMNS` + `SUMMARIZE`. The pattern below is the recommended approach.

> **Reference:** [SUMMARIZE function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/summarize-function-dax)

---

## ADDCOLUMNS — Recommended Pattern

The recommended approach for adding measures to a grouped table:

```dax
Category Summary =
    ADDCOLUMNS(
        SUMMARIZE(Sales, Products[Category]),
        "Revenue", [Total Revenue],
        "Margin %", [Gross Margin %]
    )
```

`SUMMARIZE` provides the distinct group-by rows; `ADDCOLUMNS` evaluates each measure in the filter context defined by each row.

This pattern is preferred because measures computed via `ADDCOLUMNS` respect the proper filter context, while measures added directly inside `SUMMARIZE` may behave unexpectedly.

> **Reference:** [ADDCOLUMNS function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/addcolumns-function-dax)

---

## SUMMARIZECOLUMNS

`SUMMARIZECOLUMNS` is the most efficient function for building aggregated tables and is used internally by Power BI visuals:

```dax
Sales by Region Year =
    SUMMARIZECOLUMNS(
        Customers[Country],
        'Date'[Year],
        "Revenue", [Total Revenue],
        "Orders", [Order Count]
    )
```

It is equivalent to `ADDCOLUMNS(SUMMARIZE(...))` but optimized for tabular queries. Use it in **DAX Query View** for ad-hoc analysis; use `ADDCOLUMNS` + `SUMMARIZE` for calculated tables in the model (where `SUMMARIZECOLUMNS` has limitations).

> **Reference:** [SUMMARIZECOLUMNS function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/summarizecolumns-function-dax)

---

## GROUPBY

`GROUPBY` is similar to `SUMMARIZE` but uses `CURRENTGROUP()` and iterator functions for aggregation, allowing it to aggregate over a table that is itself a DAX expression (not just a physical model table):

```dax
Tier Summary =
    GROUPBY(
        ADDCOLUMNS(
            Customers,
            "Revenue Tier", IF(Customers[Lifetime Value] > 50000, "High", "Standard")
        ),
        [Revenue Tier],
        "Customer Count", COUNTX(CURRENTGROUP(), Customers[CustomerID])
    )
```

Use `GROUPBY` when the input is a computed table expression; use `SUMMARIZE` when working with physical model tables.

> **Reference:** [GROUPBY function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/groupby-function-dax)

---

## ROW — Single Row Table

`ROW(name, expression, ...)` creates a single-row table with named columns:

```dax
Model KPIs = ROW(
    "Total Revenue", [Total Revenue],
    "Gross Margin %", [Gross Margin %],
    "Customer Count", [Customer Count]
)
```

Useful in DAX Query View for validating measures. Less common as a calculated table in the model.

---

## UNION and INTERSECT

Combine or intersect two tables with the same schema:

```dax
All Products Table = UNION(
    SELECTCOLUMNS(ProductsA, "ProductID", ProductsA[ProductID], "Name", ProductsA[Name]),
    SELECTCOLUMNS(ProductsB, "ProductID", ProductsB[ProductID], "Name", ProductsB[Name])
)
```

```dax
Common Products = INTERSECT(
    SELECTCOLUMNS(ProductsA, "ProductID", ProductsA[ProductID]),
    SELECTCOLUMNS(ProductsB, "ProductID", ProductsB[ProductID])
)
```

`EXCEPT(table1, table2)` returns rows in table1 that are not in table2 — equivalent to SQL EXCEPT / MINUS.

---

## Use Cases for Calculated Tables

| Use case | Recommended function |
| --- | --- |
| Date dimension | `CALENDAR()` + calculated columns |
| Pre-aggregated summary for a specific visual | `ADDCOLUMNS(SUMMARIZE(...))` |
| Disconnected slicer (parameter table) | `DATATABLE()` or **What-if parameter** |
| Combining data from two sources | `UNION()` |
| Role-playing dimension lookup | `TREATAS()` in a measure |

---

## Best Practices

* Do not create summary tables to work around slow measures — fix the measure or model instead.
* Use `ADDCOLUMNS(SUMMARIZE(...))` rather than adding aggregations directly inside `SUMMARIZE`.
* Calculated tables are refreshed with the model — keep their DAX expressions efficient to avoid slow refresh times.
* Prefer building summary views in Power Query (GroupBy step) over DAX calculated tables when the summary is needed as a standalone dataset.

---

## References

* [SUMMARIZE function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/summarize-function-dax)
* [ADDCOLUMNS function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/addcolumns-function-dax)
* [SUMMARIZECOLUMNS function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/summarizecolumns-function-dax)
* [GROUPBY function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/groupby-function-dax)
* [Best practices for SUMMARIZE and ADDCOLUMNS – SQLBI](https://www.sqlbi.com/articles/best-practices-using-summarize-and-addcolumns/)
