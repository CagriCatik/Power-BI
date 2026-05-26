# Date Functions in DAX

## Overview

DAX includes a rich set of date and time functions for extracting date parts, calculating differences, constructing dates, and performing date arithmetic. These functions are used extensively in calculated columns (to extract year, month, weekday from a date field) and in measures (for time intelligence).

> **Reference:** [Date and time functions (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/date-and-time-functions-dax)

---

## Date Part Extraction Functions

These functions extract individual components from a date or datetime value:

| Function | Returns | Example |
| --- | --- | --- |
| `YEAR(date)` | Integer year | `YEAR(Sales[Order Date])` → 2024 |
| `MONTH(date)` | Integer month (1–12) | `MONTH(Sales[Order Date])` → 3 |
| `DAY(date)` | Integer day of month (1–31) | `DAY(Sales[Order Date])` → 15 |
| `HOUR(datetime)` | Integer hour (0–23) | `HOUR(Events[Start Time])` → 14 |
| `MINUTE(datetime)` | Integer minute (0–59) | `MINUTE(Events[Start Time])` → 30 |
| `SECOND(datetime)` | Integer second (0–59) | `SECOND(Events[Start Time])` → 0 |
| `WEEKDAY(date, [return_type])` | Integer weekday | `WEEKDAY(Sales[Order Date], 2)` → 1=Mon |
| `WEEKNUM(date, [return_type])` | Integer week number | `WEEKNUM(Sales[Order Date])` → 12 |

### Quarter from Month

DAX has no native `QUARTER()` function; derive it with:

```dax
Quarter = "Q" & INT((MONTH(Sales[Order Date]) + 2) / 3)
```

---

## DATE — Constructing a Date

`DATE(year, month, day)` constructs a date value from three integers:

```dax
Start of Year = DATE(YEAR(Sales[Order Date]), 1, 1)
End of Month = DATE(YEAR(Sales[Order Date]), MONTH(Sales[Order Date]) + 1, 0)
```

Passing `0` as the day returns the last day of the previous month — a useful trick for month-end calculations.

> **Reference:** [DATE function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/date-function-dax)

---

## TODAY and NOW

| Function | Returns |
| --- | --- |
| `TODAY()` | Current date (no time component) |
| `NOW()` | Current date and time |

These are useful in calculated columns for age or days-elapsed calculations:

```dax
Days Since Order = TODAY() - Sales[Order Date]
Customer Age (days) = TODAY() - Customers[Birth Date]
```

> **Note:** `TODAY()` and `NOW()` are volatile — they recalculate on every refresh and every time a report opens. Avoid using them inside complex calculated columns that are expensive to compute.

---

## DATEDIFF — Difference Between Two Dates

`DATEDIFF(start_date, end_date, interval)` returns the number of complete intervals between two dates:

```dax
Days to Ship = DATEDIFF(Sales[Order Date], Sales[Ship Date], DAY)
Months Active = DATEDIFF(Customers[Start Date], TODAY(), MONTH)
Years Employed = DATEDIFF(Employees[Hire Date], TODAY(), YEAR)
```

Valid interval values: `DAY`, `WEEK`, `MONTH`, `QUARTER`, `YEAR`, `HOUR`, `MINUTE`, `SECOND`.

> **Reference:** [DATEDIFF function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/datediff-function-dax)

---

## EDATE and EOMONTH

| Function | Description |
| --- | --- |
| `EDATE(start_date, months)` | Date that is exactly N months before or after start_date |
| `EOMONTH(start_date, months)` | Last day of the month that is N months before or after start_date |

```dax
Contract Expiry = EDATE(Contracts[Start Date], 12)
End of Current Month = EOMONTH(TODAY(), 0)
End of Next Month = EOMONTH(TODAY(), 1)
```

> **Reference:** [EDATE function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/edate-function-dax)

---

## DATEVALUE and TIMEVALUE

* `DATEVALUE(date_text)` — converts a date stored as text into a date value.
* `TIMEVALUE(time_text)` — converts a time stored as text into a time value.

These are useful when data arrives with dates as strings:

```dax
Parsed Date = DATEVALUE(Sales[Order Date Text])
```

---

## Combining Date and Time

`Sales[Order Date]` may be a date while `Sales[Order Time]` is a time. Combine them into a single datetime:

```dax
Order Datetime = Sales[Order Date] + Sales[Order Time]
```

DAX stores dates as integers (days since 30 December 1899) and times as decimals, so addition produces a valid datetime.

---

## Weekday Name as Text

To get a human-readable weekday name, use FORMAT():

```dax
Weekday Name = FORMAT(Sales[Order Date], "DDDD")
```

For abbreviated names:

```dax
Weekday Short = FORMAT(Sales[Order Date], "DDD")
```

---

## Practical Calculated Column Examples

### Age in Years

```dax
Age = DATEDIFF(Customers[Birth Date], TODAY(), YEAR)
```

### Order Year-Month Key (for sorting)

```dax
YearMonth = YEAR(Sales[Order Date]) * 100 + MONTH(Sales[Order Date])
```

This produces values like 202403, which sort chronologically as integers.

### Is Weekend Flag

```dax
Is Weekend = IF(WEEKDAY(Sales[Order Date], 2) >= 6, 1, 0)
```

`WEEKDAY(..., 2)` returns 1 = Monday through 7 = Sunday, so values 6 (Saturday) and 7 (Sunday) are weekends.

---

## Best Practices

* Extract `Year`, `Month Number`, `Month Name`, `Quarter`, and `Weekday` in your **Date table** — not as individual calculated columns on the fact table.
* Use a **Date table** (also called a calendar table) and relate it to fact tables by date key rather than duplicating date logic across multiple calculated columns.
* Sort `Month Name` by `Month Number` to ensure correct chronological ordering in visuals.

---

## References

* [Date and time functions (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/date-and-time-functions-dax)
* [DATE function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/date-function-dax)
* [DATEDIFF function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/datediff-function-dax)
* [EDATE function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/edate-function-dax)
* [TODAY function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/today-function-dax)
