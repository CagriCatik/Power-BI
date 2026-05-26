# Date Master Tables (Date Dimension)

## Overview

A **Date table** (also called a calendar table or date dimension) is a standalone table in your data model that contains one row per calendar day and a full set of date attributes — year, quarter, month, week, weekday, and so on. Every time intelligence function in DAX requires a properly marked Date table. Without one, DAX time intelligence functions (`TOTALYTD`, `SAMEPERIODLASTYEAR`, `DATEADD`, etc.) will not work correctly.

> **Reference:** [Create date tables in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/guidance/model-date-tables)

---

## Why a Dedicated Date Table?

| Benefit | Explanation |
| --- | --- |
| Time intelligence support | DAX time intelligence functions require a contiguous Date table marked as such |
| Consistent date attributes | One place to define Month Name, Quarter, Fiscal Year — no duplication across tables |
| Sorting control | Sort Month Name by Month Number once in the Date table — all visuals inherit it |
| Multiple date roles | One Date table can be related to multiple date columns (Order Date, Ship Date, Due Date) via role-playing relationships |
| Fiscal year support | Define fiscal quarters/years independently of calendar year |

---

## Building a Date Table with DAX

Use `CALENDAR()` or `CALENDARAUTO()` to generate the date spine, then add columns:

### Step 1 — Create the Table

In Power BI Desktop, go to the **Modeling** tab → **New table**:

```dax
Date = CALENDAR(DATE(2018, 1, 1), DATE(2030, 12, 31))
```

`CALENDAR(start, end)` returns a single-column table named `[Date]` with one row per day between the two dates (inclusive).

Alternatively, use `CALENDARAUTO()` to automatically determine the date range from all date columns in the model:

```dax
Date = CALENDARAUTO()
```

> **Reference:** [CALENDAR function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/calendar-function-dax)

### Step 2 — Add Date Attribute Columns

With the Date table created, add calculated columns to it using the **New column** button on the **Table tools** ribbon:

```dax
Year = YEAR('Date'[Date])
```

```dax
Month Number = MONTH('Date'[Date])
```

```dax
Month Name = FORMAT('Date'[Date], "MMMM")
```

```dax
Month Short = FORMAT('Date'[Date], "MMM")
```

```dax
Quarter Number = INT((MONTH('Date'[Date]) + 2) / 3)
```

```dax
Quarter Label = "Q" & INT((MONTH('Date'[Date]) + 2) / 3)
```

```dax
Year Quarter = YEAR('Date'[Date]) & " Q" & INT((MONTH('Date'[Date]) + 2) / 3)
```

```dax
Weekday Number = WEEKDAY('Date'[Date], 2)
```

```dax
Weekday Name = FORMAT('Date'[Date], "DDDD")
```

```dax
Is Weekend = IF(WEEKDAY('Date'[Date], 2) >= 6, 1, 0)
```

```dax
Week Number = WEEKNUM('Date'[Date], 2)
```

```dax
Year Month Key = YEAR('Date'[Date]) * 100 + MONTH('Date'[Date])
```

---

## Adding a Fiscal Year

If your organization uses a fiscal year that starts in a different month (e.g., April = FY start):

```dax
Fiscal Year = IF(
    MONTH('Date'[Date]) >= 4,
    "FY" & YEAR('Date'[Date]) & "/" & RIGHT(YEAR('Date'[Date]) + 1, 2),
    "FY" & YEAR('Date'[Date]) - 1 & "/" & RIGHT(YEAR('Date'[Date]), 2)
)
```

```dax
Fiscal Quarter = "Q" & INT((MOD(MONTH('Date'[Date]) - 4 + 12, 12)) / 3) + 1
```

Adjust the offset (`4` in the examples above) to match your fiscal year start month.

---

## Sorting Text Date Columns

After creating text columns (Month Name, Quarter Label, Weekday Name), apply Sort by Column:

1. Select `Month Name` → **Column tools** → **Sort by column** → `Month Number`.
2. Select `Month Short` → **Column tools** → **Sort by column** → `Month Number`.
3. Select `Weekday Name` → **Column tools** → **Sort by column** → `Weekday Number`.
4. Select `Year Quarter` → **Column tools** → **Sort by column** → `Year Month Key` (or a fiscal equivalent).

---

## Marking as a Date Table

DAX time intelligence functions require the Date table to be explicitly marked:

1. In **Data** view, select any cell in the Date table.
2. On the **Table tools** ribbon, click **Mark as date table**.
3. Select the `Date` column as the date column.
4. Power BI validates that the column is of Date type, has no blanks, and has no duplicates.

> **Reference:** [Set and use date tables in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-date-tables)

---

## Relating the Date Table to Fact Tables

Create relationships between the Date table and each fact table's date column:

1. Go to the **Model** view.
2. Drag `Date[Date]` onto `Sales[Order Date]` to create a relationship.
3. Repeat for any other date columns (Ship Date, Due Date) — these become **inactive relationships** by default.
4. Use `USERELATIONSHIP()` in measures to activate an inactive relationship:

```dax
Sales by Ship Date = CALCULATE(
    [Total Sales],
    USERELATIONSHIP('Date'[Date], Sales[Ship Date])
)
```

---

## Complete Date Table Reference

Below is a consolidated set of columns a production Date table typically contains:

| Column | DAX Formula | Type |
| --- | --- | --- |
| Date | (from CALENDAR) | Date |
| Year | `YEAR('Date'[Date])` | Integer |
| Quarter Number | `INT((MONTH(...)+2)/3)` | Integer |
| Quarter Label | `"Q" & QuarterNumber` | Text |
| Month Number | `MONTH('Date'[Date])` | Integer |
| Month Name | `FORMAT(..., "MMMM")` | Text |
| Month Short | `FORMAT(..., "MMM")` | Text |
| Year Month Key | `Year * 100 + MonthNumber` | Integer |
| Week Number | `WEEKNUM('Date'[Date], 2)` | Integer |
| Weekday Number | `WEEKDAY('Date'[Date], 2)` | Integer |
| Weekday Name | `FORMAT(..., "DDDD")` | Text |
| Is Weekend | `IF(WeekdayNumber >= 6, 1, 0)` | Integer |
| Fiscal Year | See formula above | Text |

---

## Best Practices

* Always use a **single Date table** for all date relationships — do not use multiple Date tables.
* Set the Date table range to **span several years beyond today** — refreshing data that extends past the table range will break time intelligence silently.
* **Mark the Date table** explicitly — Power BI's auto date/time feature creates hidden Date tables per column which conflict with explicit Date tables; disable auto date/time in **File → Options → Data Load**.
* Sort all text columns by their numeric counterparts before publishing.

---

## References

* [Create date tables in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/guidance/model-date-tables)
* [CALENDAR function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/calendar-function-dax)
* [Set and use date tables in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-date-tables)
* [Mark a table as a date table in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-date-tables)
