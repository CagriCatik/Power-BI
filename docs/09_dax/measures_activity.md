# DAX Measures — Practical Activity

## Overview

This activity builds a set of core business measures for a retail sales dataset. You will practice the most common DAX aggregation and ratio patterns, apply safe division, and verify your measures behave correctly across different filter contexts.

---

## Dataset Assumption

The activity assumes a model with the following tables:

| Table | Key columns |
| --- | --- |
| `Sales` | `OrderID`, `CustomerID`, `ProductID`, `OrderDate`, `Revenue`, `Cost`, `Quantity` |
| `Products` | `ProductID`, `ProductName`, `Category`, `SubCategory` |
| `Customers` | `CustomerID`, `CustomerName`, `Country`, `Segment` |
| `Date` | `Date`, `Year`, `Month Number`, `Month Name`, `Quarter Label` |

All tables are related through their key columns and the `Date` table is marked as a date table.

---

## Task 1 — Basic Aggregations

Create the following measures in a `_Measures` table:

1. **Total Revenue** — sum of all revenue.
2. **Total Cost** — sum of all cost.
3. **Total Quantity** — sum of all units sold.
4. **Order Count** — count of distinct order IDs.
5. **Customer Count** — count of distinct customers who placed at least one order.

Expected formulas:

```dax
Total Revenue = SUM(Sales[Revenue])
Total Cost = SUM(Sales[Cost])
Total Quantity = SUM(Sales[Quantity])
Order Count = DISTINCTCOUNT(Sales[OrderID])
Customer Count = DISTINCTCOUNT(Sales[CustomerID])
```

**Verify:** Place all five measures in a table visual with no filters. The numbers should match your source data totals.

---

## Task 2 — Derived Measures

Using the measures from Task 1 as building blocks, create:

1. **Gross Profit** — revenue minus cost.
2. **Gross Margin %** — gross profit as a percentage of revenue (use DIVIDE).
3. **Average Order Value** — total revenue divided by order count (use DIVIDE).
4. **Revenue per Customer** — total revenue divided by customer count (use DIVIDE).

```dax
Gross Profit = [Total Revenue] - [Total Cost]
```

```dax
Gross Margin % = DIVIDE([Gross Profit], [Total Revenue], 0)
```

```dax
Average Order Value = DIVIDE([Total Revenue], [Order Count], 0)
```

```dax
Revenue per Customer = DIVIDE([Total Revenue], [Customer Count], 0)
```

**Verify:** Add a slicer for `Products[Category]`. All measures should update correctly for each category selection.

---

## Task 3 — Percentage of Total

Create a measure that shows each category's revenue as a percentage of the grand total, regardless of what category is selected:

```dax
Revenue % of Total =
    DIVIDE(
        [Total Revenue],
        CALCULATE([Total Revenue], ALL(Products[Category])),
        0
    )
```

**Verify:** In a matrix with `Products[Category]` on rows and `Revenue % of Total` as values, the percentages should sum to 100%.

---

## Task 4 — Year-to-Date

Create a YTD revenue measure using the Date table:

```dax
Revenue YTD = TOTALYTD([Total Revenue], 'Date'[Date])
```

**Verify:** In a line chart with `Date[Month Name]` on the axis and both `[Total Revenue]` and `[Revenue YTD]` as values, the YTD line should continuously increase across months within each year and reset at the start of the next year.

---

## Task 5 — Prior Year Comparison

1. Create a **Revenue Prior Year** measure.
2. Create a **YoY Revenue Growth %** measure.

```dax
Revenue Prior Year = CALCULATE(
    [Total Revenue],
    SAMEPERIODLASTYEAR('Date'[Date])
)
```

```dax
YoY Revenue Growth % = DIVIDE(
    [Total Revenue] - [Revenue Prior Year],
    [Revenue Prior Year],
    BLANK()
)
```

**Verify:** In a table with `Date[Year]` on rows, `[Total Revenue]`, `[Revenue Prior Year]`, and `[YoY Revenue Growth %]` as columns, the first year should show BLANK for prior year (no data before it) and subsequent years should show valid growth percentages.

---

## Task 6 — Segment Analysis

Create a measure that calculates revenue only for the "Corporate" customer segment, regardless of any segment filter applied to the report:

```dax
Corporate Revenue = CALCULATE(
    [Total Revenue],
    Customers[Segment] = "Corporate"
)
```

**Verify:** In a card visual, this measure should always show the same value regardless of what slicer selections are active for `Customers[Segment]`.

---

## Checklist

* [ ] All five basic aggregation measures created and verified
* [ ] All four derived measures created and verified
* [ ] Revenue % of Total sums to 100% across categories
* [ ] YTD measure resets at the start of each year
* [ ] Prior year measure returns BLANK for the earliest year
* [ ] Corporate Revenue measure is unaffected by segment slicers
* [ ] All measures formatted (currency, percentage, or integer as appropriate)
* [ ] Measures stored in a dedicated `_Measures` table

---

## References

* [Measures in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-measures)
* [TOTALYTD function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/totalytd-function-dax)
* [SAMEPERIODLASTYEAR function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/sameperiodlastyear-function-dax)
* [CALCULATE function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/calculate-function-dax)
