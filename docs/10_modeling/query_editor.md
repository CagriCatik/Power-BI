# Introduction to Power Query Editor

## Overview

**Power Query Editor** (also called the **Query Editor**) is the data transformation layer in Power BI. It is where you connect to data sources, clean and reshape data, and define the steps that produce the tables loaded into your data model. Power Query uses a functional language called **M** under the hood, but the UI generates M code for you as you click through transformation steps.

> **Reference:** [Power Query overview – Microsoft Learn](https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query)

---

## Accessing Power Query Editor

1. In Power BI Desktop, click **Transform data** on the **Home** ribbon.
2. The Power Query Editor window opens in a separate interface.
3. Close it by clicking **Close & Apply** (to apply changes and return to Desktop) or **Close** (to discard unsaved changes).

---

## Power Query Editor Interface

| Area | Description |
| --- | --- |
| **Queries pane** (left) | Lists all queries (tables) loaded or defined in the model |
| **Formula bar** | Shows the M expression for the currently selected Applied Step |
| **Data preview** (center) | Shows a sample of the data after the selected step |
| **Applied Steps** (right) | Lists every transformation step in order for the selected query |
| **Query Settings** (right) | Name of the query and the Applied Steps panel |

---

## Applied Steps

Every transformation you perform in Power Query is recorded as a step in the **Applied Steps** list. Steps execute in order from top to bottom. You can:

* Click any step to preview the data at that point in the pipeline.
* Rename a step by double-clicking it.
* Delete a step by clicking the `×` next to it (removes that transformation).
* Insert a step by selecting a prior step and then performing the action — the new step is inserted after the selected one.
* Drag steps to reorder (with caution — steps can depend on each other).

Applied Steps are the M code of your query made visual. Each step is a call to an M function stored in the `let` expression.

---

## The M Formula Language

Every transformation in Power Query generates M code. To view the full M code of a query:

1. In Power Query Editor, click **Advanced Editor** on the **View** ribbon (or Home ribbon).
2. The full M `let … in` expression appears.

A typical M query looks like:

```text
let
    Source = Csv.Document(File.Contents("C:\data\sales.csv"), [Delimiter=","]),
    PromotedHeaders = Table.PromoteHeaders(Source),
    ChangedTypes = Table.TransformColumnTypes(PromotedHeaders, {
        {"OrderID", Int64.Type},
        {"Revenue", type number},
        {"Order Date", type date}
    }),
    FilteredRows = Table.SelectRows(ChangedTypes, each [Revenue] > 0)
in
    FilteredRows
```

Each step is a variable assigned the result of an M function applied to the previous step's result.

> **Reference:** [M formula language reference – Microsoft Learn](https://learn.microsoft.com/en-us/powerquery-m/power-query-m-language-specification)

---

## Data Types

Setting correct data types is the most critical step in Power Query. Incorrect types cause silent errors in DAX (numbers treated as text, dates treated as strings).

In Power Query Editor:

1. Click the **data type icon** on the left side of each column header.
2. Select the correct type: Whole Number, Decimal Number, Text, Date, Date/Time, True/False, etc.

Or select multiple columns, right-click → **Change Type**.

Common type mistakes:

* Date columns loaded as Text — use **Date** or **Date/Time** type.
* Integer IDs loaded as Decimal — use **Whole Number**.
* Revenue with currency symbols loaded as Text — use **Decimal Number** after removing the symbol.

---

## Query Groups

As the number of queries grows, organize them in folders using **groups**:

1. Right-click a query in the Queries pane → **Move to group** → **New group**.
2. Name the group (e.g., "Staging", "Dimension Tables", "Fact Tables").

Staging queries (raw source with no transformations) should be separate from dimension and fact queries that reference them.

---

## Enable Load vs Reference

* **Enable Load** (on by default) — the query result is loaded into the model.
* Disable load for **staging queries** that are referenced by other queries but should not themselves add a table to the model: right-click query → **Enable load** (uncheck).

---

## Referencing vs Duplicating Queries

| Action | Result |
| --- | --- |
| **Reference** | New query starts from the output of the source query — inherits all its steps |
| **Duplicate** | New query is a full independent copy — changes do not affect the original |

Use **Reference** when building a transformation pipeline (staging → clean → final). Use **Duplicate** when you need a parallel version with different transformations applied to the same source.

---

## Best Practices

* **Rename every query** — "Query1" is unhelpful; "Sales_Raw", "dim_Product", "fact_Sales" are clear.
* **Set data types explicitly** — do not rely on the auto-detected types from the Source step.
* **Disable load for staging queries** — they add memory overhead without value.
* **Use descriptive step names** — rename "Changed Type1" to "Set Revenue to Decimal".
* **Minimize steps that buffer large tables** — sorting and grouping operations on large sources can be slow; push filters as early as possible.

---

## References

* [Power Query overview – Microsoft Learn](https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query)
* [M formula language reference – Microsoft Learn](https://learn.microsoft.com/en-us/powerquery-m/power-query-m-language-specification)
* [Get data in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-getting-started)
* [Shape and combine data in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-shape-and-combine-data)
