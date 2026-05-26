# Methods of Aggregation — Challenge Completed

## Overview

This page provides the answers and explanations for the Methods of Aggregation Practical Activity.

---

## Task 1 — Sum

The Sales column aggregated as Sum shows total revenue per category. The category with the highest bar (or value) in the table is the top revenue contributor across all transactions.

Sum is appropriate here because **revenue is additive** — $10 from transaction A plus $20 from transaction B legitimately equals $30 total revenue for that category.

---

## Task 2 — Average

After switching to Average, the per-category values now represent the typical size of a single transaction within that category.

### Key insight

The category with the **highest average** is not necessarily the category with the **highest total**. A category with a small number of very large transactions can have a higher average than a high-volume, low-value category. Both views tell a different business story — use Sum for revenue analysis, Average for price point or deal-size analysis.

---

## Task 3 — Count vs Count (Distinct)

| Column | Aggregation | Meaning |
| --- | --- | --- |
| CustomerID (Count) | Counts rows | Number of orders per region |
| CustomerID (Count Distinct) | Counts unique IDs | Number of unique customers per region |

If **Count > Count (Distinct)** for a region, it means some customers placed more than one order in that region. The gap between the two numbers tells you the volume of repeat orders.

### When to use each

* **Count** — for measuring activity volume (how many transactions).
* **Count (Distinct)** — for measuring audience size (how many unique entities).

---

## Task 4 — Minimum and Maximum

The product with the greatest difference between Minimum and Maximum sale values has the highest **price range**. This could indicate:

* A product sold at wildly different quantities per transaction.
* Discounting applied inconsistently.
* Different product variants grouped under the same name.

```dax
Price Range = [Highest Sale] - [Lowest Sale]
```

You could create this as a DAX measure to show range directly:

```DAX
Sales Range = MAX(Sales[SalesAmount]) - MIN(Sales[SalesAmount])
```

---

## Task 5 — Don't Summarize

Numeric columns used as identifiers (OrderID, ProductID, CustomerID) should never be summed or averaged — those operations are meaningless. Setting **Don't summarize** makes the column behave like a text identifier in visuals.

If you forget to change this, a table visual will show the sum of all order IDs for a category — a large nonsensical number that will confuse report readers.

---

## Task 6 — Model-Level Default

Setting **Summarization = Don't summarize** at the model level is the best practice. It means every report author who uses this semantic model will get the correct default without needing to remember to change it per visual.

---

## Reflection Answers

### When would you use Median instead of Average?

When the distribution is **skewed** — for example, salary data where a few very high earners would inflate the average. The median represents the "middle" employee better than the average in that case.

### Why might Count (Distinct) be more useful than Count for customer analysis?

Count tells you how many orders occurred; Count (Distinct) on CustomerID tells you how many different people placed those orders. For a retention analysis, you want to know the number of unique customers, not the total number of orders.

### What is the risk of showing Don't summarize on a category column in a table?

If the table groups rows by category and the "Don't summarize" column has multiple different values per group, Power BI will display only one arbitrary value (or show an error/blank). Use Don't summarize only on columns that are unique per row in the context of the grouping.

---

## References

* [Aggregates in Power BI service – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/service-aggregates)
* [Using calculated columns in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-calculated-columns)
