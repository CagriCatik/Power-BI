# DAX Calculated Columns

## Overview

A **DAX calculated column** is added to a table in the data model using a formula written in DAX. The formula is evaluated once per row at refresh time, and the result is stored in the model. Calculated columns are visible in the Fields pane and can be used like any imported column — as a slicer, in a visual's axis, or as a filter.

> **Reference:** [Calculated columns in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-calculated-columns)

---

## Creating a Calculated Column

1. In Power BI Desktop, switch to the **Data** view (table icon in the left nav).
2. Select the table where you want to add the column in the Fields pane.
3. On the **Table tools** ribbon, click **New column**.
4. The formula bar appears with a default name: `Column =`
5. Replace the default with your DAX expression, for example:

```dax
Full Name = Customers[First Name] & " " & Customers[Last Name]
```

6. Press **Enter** or click the checkmark to commit.

The new column appears immediately in the table and in the Fields pane under the correct table.

---

## DAX Syntax for Calculated Columns

### Basic Structure

```dax
ColumnName = <DAX expression>
```

The expression runs in **row context** — it has access to the current row's values via `TableName[ColumnName]` references.

### Arithmetic

```dax
Profit = Sales[Revenue] - Sales[Cost]
Margin % = DIVIDE(Sales[Profit], Sales[Revenue])
```

### Conditional Logic with IF

```dax
Sales Tier =
    IF(Sales[Revenue] >= 10000, "High",
        IF(Sales[Revenue] >= 5000, "Medium", "Low"))
```

### SWITCH for Multi-Branch Logic

```dax
Region Label =
    SWITCH(Customers[Region Code],
        "N", "North",
        "S", "South",
        "E", "East",
        "W", "West",
        "Unknown")
```

### String Functions

```dax
Email Domain = RIGHT(Customers[Email], LEN(Customers[Email]) - FIND("@", Customers[Email]))
```

---

## Row Context

Calculated columns always execute in **row context** — the DAX engine iterates over every row of the table and evaluates the formula for that row. This means:

* You reference the current row's values directly: `Sales[Revenue]` gives the Revenue value for the current row.
* You do not need SUMX or other iterator functions — the iteration is implicit.
* Row context does **not** automatically follow relationships — use RELATED() for that.

---

## RELATED — Accessing Related Table Columns

When two tables have a relationship, you can pull a column from the related (one-side) table into the many-side table using `RELATED()`:

```dax
Product Category = RELATED(Products[Category])
```

This adds a column to the sales table with the category name of the product sold in each row, sourced from the Products table via the relationship.

`RELATED()` only works from the **many** side to the **one** side of a relationship.

For the reverse direction (one to many), use `RELATEDTABLE()` to retrieve a table of matching rows, typically wrapped in an aggregation:

```dax
Orders Per Customer = COUNTROWS(RELATEDTABLE(Orders))
```

> **Reference:** [RELATED function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/related-function-dax)

---

## Practical Examples

### Bucketing and Banding

```dax
Age Band =
    IF(Customers[Age] < 25, "18–24",
        IF(Customers[Age] < 35, "25–34",
            IF(Customers[Age] < 45, "35–44",
                IF(Customers[Age] < 55, "45–54", "55+"))))
```

### Concatenation

```dax
City State = Customers[City] & ", " & Customers[State]
```

### Binary Flag

```dax
Is High Value = IF(Customers[Lifetime Value] > 50000, 1, 0)
```

### Date Part Extraction

```dax
Order Year = YEAR(Sales[Order Date])
Order Month Number = MONTH(Sales[Order Date])
Order Month Name = FORMAT(Sales[Order Date], "MMMM")
```

---

## Calculated Columns vs Measures

| Use calculated columns when… | Use measures when… |
| --- | --- |
| You need a row-level label to filter or group by | You need an aggregate (SUM, COUNT, AVERAGE) |
| You want a column in a slicer or axis | The calculation depends on the current filter context |
| You are using RELATED() to denormalize | You need time intelligence (YoY, running total) |

---

## Common Mistakes

* **Using a calculated column for aggregations** — avoid `Total = SUM(Sales[Revenue])` as a calculated column; this repeats the grand total in every row. Use a measure instead.
* **Circular references** — a calculated column cannot reference itself.
* **Referencing a measure inside a calculated column** — measures respond to filter context while columns are computed at refresh; mixing the two leads to unexpected results.

---

## Best Practices

* Use descriptive names: `Order Year` is clearer than `Col1`.
* Prefix flag columns with `Is` or `Has` (e.g., `IsActive`, `HasDiscount`).
* Prefer Power Query transformations over calculated columns for performance-critical models — Power Query transformations run before import and are not stored as DAX-computed in-memory data.
* Use `DIVIDE(numerator, denominator, [alternateResult])` instead of `/` to handle divide-by-zero gracefully.

---

## References

* [Calculated columns in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-calculated-columns)
* [RELATED function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/related-function-dax)
* [IF function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/if-function-dax)
* [SWITCH function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/switch-function-dax)
