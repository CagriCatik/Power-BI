# Changing the Method of Aggregation

## Overview

When you drag a numeric column into a visual, Power BI applies a default aggregation — usually **Sum**. But many analytical questions require a different function: an average order value, a distinct count of customers, the maximum temperature recorded, or no aggregation at all for ID columns. Understanding how to change and control aggregation is fundamental to building accurate reports.

> **Reference:** [Aggregates in Power BI service – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/service-aggregates)

---

## Default Aggregation Behaviour

Power BI assigns a default aggregation to every numeric column based on the column's data type and the **Summarize by** property set in the data model:

| Symbol in Fields pane | Meaning |
| --- | --- |
| Σ (sigma) | Numeric column — will be aggregated |
| No symbol | Text or date column — will be grouped |
| Calculator icon | DAX measure — aggregation defined in formula |

---

## Changing Aggregation in a Visual

### Method 1 — Via the Field Well

1. In the **Visualizations pane**, find the field in its well (e.g., **Columns**, **Values**, **Y-axis**).
2. Click the **chevron (∨)** or right-click the field name.
3. Hover over **Summarize** (or the current aggregation label shown).
4. Select from the available options.

### Method 2 — Via the Fields Pane

Right-click a numeric column directly in the **Fields pane**:

1. Right-click the column name.
2. Select **Default summarization**.
3. Choose a summarization method.

This changes the model-level default — the column will use this aggregation everywhere it is added to a new visual.

---

## Available Aggregation Methods

| Method | Description | Typical Use |
| --- | --- | --- |
| **Sum** | Adds all values | Revenue, cost, quantity |
| **Average** | Arithmetic mean | Order value, rating, temperature |
| **Minimum** | Smallest value | Lowest price, earliest date |
| **Maximum** | Largest value | Peak sales, highest score |
| **Count** | Number of rows (including nulls) | Row count, transaction count |
| **Count (Distinct)** | Number of unique non-null values | Unique customers, distinct products |
| **Standard deviation** | Population or sample standard deviation | Statistical spread analysis |
| **Variance** | Variance of values | Statistical dispersion |
| **Median** | Middle value in sorted list | Salary distribution, response time |
| **Don't summarize** | Shows raw values (no aggregation) | IDs, codes, keys |

---

## "Don't Summarize" — When to Use It

Selecting **Don't summarize** means Power BI will display the raw value from each row without any calculation. Use this for:

* Product codes or IDs that happen to be numeric.
* Rank or order columns that should not be added.
* Any field where summation is meaningless.

> **Warning:** Adding a non-summarized numeric column to a visual that groups data may produce unexpected results — each group will show one arbitrary value unless the column is unique per group.

---

## Changing Aggregation for a DAX Measure

DAX measures always define their own aggregation in the formula. You cannot change the aggregation of a measure via the field well — the DAX expression *is* the aggregation.

To use a different aggregation, create a new measure:

```DAX
Average Sales = AVERAGE(Sales[SalesAmount])
Max Sales     = MAX(Sales[SalesAmount])
Distinct Customers = DISTINCTCOUNT(Sales[CustomerID])
```

---

## Model-Level Default: "Summarize by"

The **Summarize by** property in the data model sets the default aggregation for a column and is visible to every report that uses that model.

To change it:

1. Go to **Data View** or **Model View**.
2. Select the column.
3. In the **Column tools** ribbon, click **Summarization** and choose the desired default.

Setting this correctly at the model level saves individual report authors from having to change it every time.

---

## Best Practices

* Set the correct **Summarize by** on all numeric columns at the model level — especially setting ID and code columns to **Don't summarize**.
* Use **DAX measures** for any calculation that requires filters, time intelligence, or conditional logic rather than relying on the visual-level aggregation.
* Always double-check totals rows — a `Count` column will show a grand count of rows, not a sum of counts, which can confuse viewers.

---

## References

* [Aggregates in Power BI service – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/service-aggregates)
* [Create and Format Table Visualizations – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-tables)
