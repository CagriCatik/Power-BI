# DAX Measures — Completed Solutions

## Overview

This page provides full reference solutions for all six tasks in the DAX Measures Practical Activity, along with explanations of why each formula works and common mistakes to watch for.

---

## Task 1 — Basic Aggregations

### Solutions

```dax
Total Revenue = SUM(Sales[Revenue])
Total Cost = SUM(Sales[Cost])
Total Quantity = SUM(Sales[Quantity])
Order Count = DISTINCTCOUNT(Sales[OrderID])
Customer Count = DISTINCTCOUNT(Sales[CustomerID])
```

### Why DISTINCTCOUNT for Order Count?

`COUNT(Sales[OrderID])` would count every row, including duplicate order IDs if one order spans multiple rows (e.g., one row per line item). `DISTINCTCOUNT` counts unique order IDs, giving the true number of orders.

---

## Task 2 — Derived Measures

### Solutions

```dax
Gross Profit = [Total Revenue] - [Total Cost]
Gross Margin % = DIVIDE([Gross Profit], [Total Revenue], 0)
Average Order Value = DIVIDE([Total Revenue], [Order Count], 0)
Revenue per Customer = DIVIDE([Total Revenue], [Customer Count], 0)
```

### Why reference measures not columns?

`[Total Revenue]` references the explicit measure — it includes the current filter context. If you wrote `SUM(Sales[Revenue])` inline in `Gross Profit`, it would also work in this case, but referencing measures is cleaner and ensures consistent behavior when CALCULATE is added later.

### Why DIVIDE() not `/`?

If `[Order Count]` or `[Customer Count]` is zero (no data for the current filter), `/` produces an error. `DIVIDE([Total Revenue], [Order Count], 0)` returns 0 instead.

---

## Task 3 — Percentage of Total

### Solution

```dax
Revenue % of Total =
    DIVIDE(
        [Total Revenue],
        CALCULATE([Total Revenue], ALL(Products[Category])),
        0
    )
```

### How it works

* The numerator `[Total Revenue]` uses the current filter context — for a row showing "Electronics", it returns Electronics revenue.
* `CALCULATE([Total Revenue], ALL(Products[Category]))` removes the category filter, returning grand total revenue.
* `DIVIDE` produces the percentage.

### Common mistake

Using `ALL(Products)` instead of `ALL(Products[Category])` removes all filters from the Products table — including any product name or subcategory filters active in the report. Scope `ALL()` to the specific column you want to remove.

---

## Task 4 — Year-to-Date

### Solution

```dax
Revenue YTD = TOTALYTD([Total Revenue], 'Date'[Date])
```

### How it works

`TOTALYTD` is shorthand for:

```dax
Revenue YTD =
    CALCULATE(
        [Total Revenue],
        DATESYTD('Date'[Date])
    )
```

`DATESYTD` returns all dates from January 1st of the current year up to the current date in context. The result accumulates with each passing month.

### Fiscal Year YTD

If your fiscal year ends on 31 March, pass the year-end date as the third argument:

```dax
Revenue FY YTD = TOTALYTD([Total Revenue], 'Date'[Date], "03-31")
```

---

## Task 5 — Prior Year Comparison

### Solutions

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

### Why BLANK() for the alternate result?

For the earliest year in the data there is no prior year — `[Revenue Prior Year]` returns BLANK, making the denominator BLANK. Returning `BLANK()` instead of `0` causes the cell to appear empty in the visual, which is more honest than showing 0% growth.

### Debugging tip

If `[Revenue Prior Year]` returns BLANK for all years, check that:

1. The Date table is marked as a date table.
2. The relationship between the Date table and Sales is active and correctly set to Date type.

---

## Task 6 — Segment Analysis

### Solution

```dax
Corporate Revenue = CALCULATE(
    [Total Revenue],
    Customers[Segment] = "Corporate"
)
```

### How it works

`CALCULATE` applies the filter `Customers[Segment] = "Corporate"` on top of (or replacing) any existing filter context for `Customers[Segment]`. Even if the report has a slicer filtering to "Consumer", this measure always returns Corporate revenue.

### Extending the pattern

To make the filter additive rather than replacing, use `KEEPFILTERS`:

```dax
Corporate Revenue (Additive) = CALCULATE(
    [Total Revenue],
    KEEPFILTERS(Customers[Segment] = "Corporate")
)
```

With `KEEPFILTERS`, if a slicer selects "Consumer" and "Corporate" the measure will return Corporate revenue only (the intersection). Without it, the measure always returns Corporate regardless of slicers.

---

## Measure Formatting Reference

| Measure | Format | Decimal places |
| --- | --- | --- |
| Total Revenue | Currency | 0 |
| Total Cost | Currency | 0 |
| Gross Profit | Currency | 0 |
| Gross Margin % | Percentage | 1 |
| Average Order Value | Currency | 2 |
| Revenue per Customer | Currency | 2 |
| Order Count | Whole number | 0 |
| Customer Count | Whole number | 0 |
| Revenue YTD | Currency | 0 |
| Revenue Prior Year | Currency | 0 |
| YoY Revenue Growth % | Percentage | 1 |
| Corporate Revenue | Currency | 0 |

---

## References

* [Measures in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-measures)
* [TOTALYTD function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/totalytd-function-dax)
* [SAMEPERIODLASTYEAR function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/sameperiodlastyear-function-dax)
* [CALCULATE function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/calculate-function-dax)
* [ALL function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/all-function-dax)
