# Basic Transformations — Part 2

## Overview

Part 2 covers more advanced Power Query transformations: merging queries (joining tables), appending queries (stacking tables), pivoting and unpivoting, grouping rows, and adding custom columns with M expressions. These operations complete the toolkit for most data preparation scenarios.

> **Reference:** [Combine data from multiple sources – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-shape-and-combine-data)

---

## Merging Queries (Join)

A **merge** combines two queries horizontally — matching rows from one query to rows from another based on key columns. This is equivalent to a SQL JOIN.

1. In Power Query Editor, on the **Home** ribbon, click **Merge Queries** → **Merge Queries** (merges into the current query) or **Merge Queries as New** (creates a new query).
2. Select the key column in the current (left) query.
3. Select the second (right) query from the dropdown.
4. Select the matching key column in the right query.
5. Choose the **Join Kind**.
6. Click **OK**.

A new column containing the merged (right) table appears. Click the **expand icon** on that column header to select which columns to bring in.

### Join Kinds

| Join Kind | Rows returned |
| --- | --- |
| Left Outer | All rows from left; matching rows from right (null if no match) |
| Right Outer | All rows from right; matching rows from left |
| Full Outer | All rows from both; nulls where no match |
| Inner | Only rows with matches in both tables |
| Left Anti | Rows from left that have no match in right |
| Right Anti | Rows from right that have no match in left |

**Left Outer** is the most common — it keeps all fact rows and enriches with dimension attributes where available.

> **Reference:** [Merge queries overview – Microsoft Learn](https://learn.microsoft.com/en-us/power-query/merge-queries-overview)

---

## Appending Queries (Union)

An **append** stacks two or more queries vertically — combining rows from multiple tables with the same schema. Equivalent to SQL UNION ALL.

1. **Home** → **Append Queries** → **Append Queries** (appends into current) or **Append Queries as New**.
2. Select **Two tables** or **Three or more tables**.
3. Add the queries to combine.
4. Click **OK**.

Columns are matched by name — if a column exists in one table but not another, the missing values become null. This behavior allows appending tables with slightly different schemas (e.g., sales data from different years with extra columns added over time).

---

## Grouping Rows (Aggregate)

Grouping collapses multiple rows into summary rows based on key columns:

1. Select the column(s) to group by.
2. **Transform** → **Group By**.
3. Define the grouping columns and the aggregation(s): Sum, Count, Average, Min, Max, All Rows.

Example — summarizing sales by month and category:

1. Group by `Year`, `Month Number`, `Category`.
2. Add aggregation: `Total Revenue` = Sum of `Revenue`.

The result is a compact summary table.

> **Reference:** [Group or summarize rows – Microsoft Learn](https://learn.microsoft.com/en-us/power-query/group-by)

---

## Pivot Columns

**Pivot** converts distinct values from a column into new columns — rotating a long table to a wide table:

1. Select the column whose distinct values will become new column headers.
2. **Transform** → **Pivot Column**.
3. Choose the **Values Column** (the column whose values fill the new columns).
4. Choose the aggregation (Sum, Count, Average, Min, Max, Don't Aggregate).

Example: a table with rows for each channel ("Online", "In-Store", "Wholesale") pivoted on "Channel" with "Revenue" as values produces columns `Online`, `In-Store`, `Wholesale`.

---

## Unpivot Columns

**Unpivot** converts multiple columns into rows — rotating a wide table to a long table. This is one of the most important transformations for normalizing data from Excel-style "matrix" formats.

1. Select the columns you want to unpivot.
2. **Transform** → **Unpivot Columns** (unpivots selected columns) or **Unpivot Other Columns** (unpivots everything except the selected columns).

The result produces two new columns: **Attribute** (original column headers) and **Value** (original values).

Example: a table with columns `Jan`, `Feb`, `Mar`, `Apr` containing monthly revenue values is unpivoted into rows with `Month` and `Revenue` columns — one row per month per product.

> **Reference:** [Unpivot columns – Microsoft Learn](https://learn.microsoft.com/en-us/power-query/unpivot-column)

---

## Custom Columns

**Custom Columns** let you write any M expression to compute a new column:

1. **Add Column** → **Custom Column**.
2. Enter a column name and the M formula.

Examples:

```text
Profit = [Revenue] - [Cost]
```

```text
Category Label = if [Revenue] > 10000 then "High" else if [Revenue] > 5000 then "Medium" else "Low"
```

```text
Full Name = [First Name] & " " & [Last Name]
```

Custom Column is the Power Query equivalent of a DAX calculated column — use it for row-level transformations that are easier expressed in M than DAX, or that are needed at the staging layer before the data enters the model.

---

## Index Column

Adds a sequential integer index column — useful when a table lacks a natural primary key:

**Add Column** → **Index Column** → **From 0** / **From 1** / **Custom**.

---

## Handling Errors

After type changes or custom expressions, rows with conversion errors appear as `Error` cells:

* **Keep Errors** — **Home** → **Keep Rows** → **Keep Errors** (isolate problematic rows for investigation).
* **Remove Errors** — **Home** → **Remove Rows** → **Remove Errors** (drop rows with any error).
* **Replace Errors** — select the column → **Transform** → **Replace Errors** → enter a fallback value.

---

## Best Practices

* Prefer **Merge** over DAX `RELATED()` for lookups that only depend on a single key — it is more performant to resolve the lookup at import time.
* Use **Unpivot Other Columns** rather than **Unpivot Columns** when the number of value columns may change — it is schema-resilient.
* After a **Merge**, **expand only the columns you need** — expanding all columns imports unnecessary data.
* Rename the steps that result from Merge and Append operations — the auto-generated names ("Merged Queries", "Appended Query") are not descriptive.

---

## References

* [Combine data from multiple sources – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-shape-and-combine-data)
* [Merge queries overview – Microsoft Learn](https://learn.microsoft.com/en-us/power-query/merge-queries-overview)
* [Group or summarize rows – Microsoft Learn](https://learn.microsoft.com/en-us/power-query/group-by)
* [Unpivot columns – Microsoft Learn](https://learn.microsoft.com/en-us/power-query/unpivot-column)
