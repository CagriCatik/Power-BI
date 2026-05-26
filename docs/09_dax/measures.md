# Introduction to DAX Measures

## Overview

A **measure** in Power BI is a named DAX formula that aggregates or calculates values dynamically in response to the active filter context. Measures power virtually every KPI card, chart value, and analytical calculation in a professional Power BI report.

> **Reference:** [Measures in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-measures)

---

## Creating a Measure

1. In Power BI Desktop, go to the **Modeling** ribbon tab.
2. Click **New measure**.
3. The formula bar opens with a default name: `Measure =`
4. Type the measure name and formula, for example:

```dax
Total Sales = SUM(Sales[Revenue])
```

5. Press **Enter** to commit.

The measure appears in the Fields pane under the selected table with a calculator icon.

### Alternative: Right-Click

Right-click any table in the Fields pane → **New measure**. This creates the measure in that table's namespace.

---

## Core Aggregation Functions

These are the most commonly used measure functions:

| Function | Description | Example |
| --- | --- | --- |
| `SUM(column)` | Sum of all values in a column | `SUM(Sales[Revenue])` |
| `COUNT(column)` | Count of non-blank values | `COUNT(Orders[OrderID])` |
| `COUNTA(column)` | Count including text values | `COUNTA(Customers[Name])` |
| `COUNTROWS(table)` | Count of rows in a table | `COUNTROWS(Orders)` |
| `AVERAGE(column)` | Average of values | `AVERAGE(Sales[Revenue])` |
| `MIN(column)` | Minimum value | `MIN(Sales[Order Date])` |
| `MAX(column)` | Maximum value | `MAX(Sales[Revenue])` |
| `DISTINCTCOUNT(column)` | Count of unique values | `DISTINCTCOUNT(Customers[CustomerID])` |

---

## DIVIDE — Safe Division

Avoid the `/` operator for division in measures. Use `DIVIDE()` instead to handle divide-by-zero gracefully:

```dax
Profit Margin % = DIVIDE(SUM(Sales[Profit]), SUM(Sales[Revenue]), 0)
```

The third argument is the alternate result when the denominator is zero (defaults to BLANK if omitted).

> **Reference:** [DIVIDE function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/divide-function-dax)

---

## Measure Tables

As a best practice, store all measures in a **dedicated measure table** rather than scattering them across fact tables:

1. In the **Modeling** ribbon, click **Enter data**.
2. Create a table with a single blank row and name it `_Measures` (the underscore keeps it at the top of the Fields pane).
3. Click **Load**.
4. When creating new measures, select `_Measures` as the target table.

This keeps the Fields pane organized and makes it easy to find all business logic in one place.

---

## Formatting a Measure

After creating a measure:

1. Select the measure in the Fields pane.
2. In the **Measure tools** ribbon, set the format: Currency, Percentage, Decimal, Whole number, etc.
3. Set the number of decimal places.
4. Set a Home table if needed.

Formatted measures display consistently across all visuals without per-visual number formatting.

---

## Common Measure Patterns

### Total with a fixed filter

```dax
Online Sales = CALCULATE(SUM(Sales[Revenue]), Sales[Channel] = "Online")
```

### Percentage of total

```dax
Sales % of Total =
    DIVIDE(
        SUM(Sales[Revenue]),
        CALCULATE(SUM(Sales[Revenue]), ALL(Sales))
    )
```

### Running total

```dax
Running Total Sales =
    CALCULATE(
        SUM(Sales[Revenue]),
        FILTER(
            ALL('Date'[Date]),
            'Date'[Date] <= MAX('Date'[Date])
        )
    )
```

### Year-to-date

```dax
Sales YTD = TOTALYTD(SUM(Sales[Revenue]), 'Date'[Date])
```

### Prior year comparison

```dax
Sales Prior Year = CALCULATE(
    SUM(Sales[Revenue]),
    SAMEPERIODLASTYEAR('Date'[Date])
)
```

```dax
YoY Growth % = DIVIDE(
    [Total Sales] - [Sales Prior Year],
    [Sales Prior Year]
)
```

---

## Referencing Measures in Other Measures

Measures can reference other measures — enclose the measure name in square brackets:

```dax
Gross Profit = [Total Sales] - [Total Cost]
Net Margin % = DIVIDE([Gross Profit], [Total Sales])
```

This builds a hierarchy of reusable calculations rather than duplicating formula logic.

---

## Naming Conventions

Consistent naming makes reports maintainable:

| Pattern | Example | Use |
| --- | --- | --- |
| Noun + Metric | `Total Sales`, `Avg Order Value` | Standard aggregation measures |
| Noun + Period | `Sales YTD`, `Sales Prior Year` | Time intelligence measures |
| Noun + %` | `Margin %`, `Sales % of Total` | Ratio/percentage measures |
| `_` prefix | `_Base Revenue` | Intermediate helper measures (hidden from consumers) |

---

## Best Practices

* Write measures as **explicit named measures** rather than relying on implicit aggregations in visuals.
* Use **DIVIDE()** instead of `/` for all division.
* Store measures in a **dedicated measure table** (`_Measures`).
* Format each measure appropriately in **Measure tools** — not in per-visual format settings.
* Use the **Description** field (right-click measure → Properties) to document what the measure calculates.

---

## References

* [Measures in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-measures)
* [DIVIDE function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/divide-function-dax)
* [DAX function reference – Microsoft Learn](https://learn.microsoft.com/en-us/dax/dax-function-reference)
* [Best practices for DAX – SQLBI](https://www.sqlbi.com/articles/best-practices-using-summarize-and-addcolumns/)
