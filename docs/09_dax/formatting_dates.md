# Formatting Dates in Power BI

## Overview

Controlling how dates are displayed is essential for building readable, professional reports. Power BI provides several mechanisms for date formatting: the **Format** property in the Data pane, the `FORMAT()` DAX function for calculated columns and measures, and the **Sort by Column** feature to control ordering of month names and other text-based date values.

> **Reference:** [Format strings in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-custom-format-strings)

---

## Setting Date Format in the Data Pane

The simplest way to control how a date column is displayed in all visuals:

1. In Power BI Desktop, switch to the **Data** view.
2. Select the date column in the table.
3. In the **Column tools** ribbon, find the **Format** dropdown.
4. Select a built-in format (e.g., Short date, Long date) or type a custom format string.

This format applies globally to that column in all visuals without requiring a formula.

---

## Common Date Format Strings

Format strings follow .NET conventions. Use these in the **Format** dropdown or inside `FORMAT()`:

| Format string | Example output | Description |
| --- | --- | --- |
| `d` | 15/03/2024 | Short date (locale-sensitive) |
| `D` | 15 March 2024 | Long date |
| `dd/MM/yyyy` | 15/03/2024 | Fixed day/month/year |
| `MM/dd/yyyy` | 03/15/2024 | US month/day/year |
| `yyyy-MM-dd` | 2024-03-15 | ISO 8601 format |
| `MMMM yyyy` | March 2024 | Full month name + year |
| `MMM yyyy` | Mar 2024 | Short month name + year |
| `MMMM` | March | Full month name only |
| `MMM` | Mar | Short month name only |
| `dddd` | Friday | Full weekday name |
| `ddd` | Fri | Short weekday name |
| `Q\Q` | Q1 | Quarter label (literal Q + quarter) |
| `yyyy` | 2024 | Year only |

---

## FORMAT() Function in DAX

`FORMAT(value, format_string)` converts a date, number, or text to a formatted string:

```dax
Month Label = FORMAT(Sales[Order Date], "MMMM yyyy")
```

This produces values like "March 2024" that can be used as an axis label.

### Returning Month Short Name

```dax
Month Short = FORMAT(Sales[Order Date], "MMM")
```

Produces "Jan", "Feb", "Mar", etc.

### ISO Date String

```dax
Date ISO = FORMAT(Sales[Order Date], "yyyy-MM-dd")
```

> **Important:** `FORMAT()` returns **text**, not a date. The resulting column cannot be used in date calculations or time intelligence functions. Use it only for display labels.

**Reference:** [FORMAT function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/format-function-dax)

---

## Sort by Column — Fixing Month Name Order

When you add a `Month Name` column (e.g., "January", "February", …), Power BI sorts it alphabetically by default — April comes before January. To sort chronologically:

1. In **Data** view, select the `Month Name` column.
2. On the **Column tools** ribbon, click **Sort by column**.
3. Select `Month Number` (the integer 1–12 column).

Now in visuals, months display as text but sort numerically.

This technique applies to any text column that needs non-alphabetical ordering — weekday names, quarter labels, etc.

> **Reference:** [Sort by column in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-sort-by-column)

---

## Date Hierarchy Display

When you add a date column to a visual, Power BI creates an automatic hierarchy: **Year › Quarter › Month › Day**. The labels at each level use the format configured on the date column.

To control the display format for each level:

1. Expand the date hierarchy in the Fields pane.
2. Select the level field (e.g., Month).
3. In **Column tools**, adjust the Format property.

---

## Displaying Relative Date Labels

For KPI cards or titles, you may want dynamic text showing "As of March 2024":

```dax
Report As Of = "As of " & FORMAT(MAX(Sales[Order Date]), "MMMM yyyy")
```

This measure returns a string with the latest date in the current filter context, useful in report headers via a card visual.

---

## Custom Format Strings for Numbers Formatted as Dates

Sometimes a date key column stores dates as integers (e.g., 20240315 for 15 March 2024). You cannot apply a date format string to an integer directly — convert it first:

```dax
Parsed Date = DATE(
    INT(Sales[DateKey] / 10000),
    INT(MOD(Sales[DateKey], 10000) / 100),
    MOD(Sales[DateKey], 100)
)
```

Then format the resulting date column normally.

---

## Best Practices

* Use `yyyy-MM-dd` format strings for date columns that are used in sorting or as axis values — ISO format sorts correctly as text.
* Always set up **Sort by Column** for any text month or weekday column.
* Do not use `FORMAT()` as a substitute for a proper date dimension — build a Date table instead.
* Keep `FORMAT()` output columns clearly named as labels (e.g., `Month Label`) so they are distinguished from the source date column.

---

## References

* [Format strings in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-custom-format-strings)
* [FORMAT function (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/format-function-dax)
* [Sort by column in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-sort-by-column)
