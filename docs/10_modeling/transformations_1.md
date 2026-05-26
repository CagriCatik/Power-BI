# Basic Transformations — Part 1

## Overview

This page covers the fundamental row and column transformations you will use in almost every Power Query pipeline: renaming, changing data types, removing unnecessary columns, filtering rows, replacing values, and splitting columns. These operations form the cleaning layer of your data preparation.

> **Reference:** [Shape and combine data in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-shape-and-combine-data)

---

## Renaming Columns

Consistent, descriptive column names are essential before the data enters the model:

1. Double-click a column header and type a new name.
2. Or right-click the column header → **Rename**.

In M:

```text
RenamedColumns = Table.RenameColumns(Source, {
    {"cust_id", "CustomerID"},
    {"rev", "Revenue"},
    {"ord_dt", "Order Date"}
})
```

---

## Changing Data Types

1. Click the **data type icon** on the left of the column header.
2. Select the target type.

Or select multiple columns → **Transform** ribbon → **Data Type** dropdown.

Common type mappings:

| Source data | Power Query type |
| --- | --- |
| Integers, IDs | Whole Number |
| Decimals, currency | Decimal Number |
| Date only | Date |
| Date and time | Date/Time |
| True/False | True/False (logical) |
| Product codes, names | Text |

> **Note:** Change types **before** using the column in other steps — a downstream step that expects a number will error if the column is Text.

---

## Removing Columns

Remove columns you do not need to reduce model size and improve refresh speed:

1. Select the column(s) to remove (hold Ctrl for multiple).
2. Right-click → **Remove columns**.

Or use **Choose columns** on the **Home** ribbon to select only the columns you want to keep (the inverse approach — useful when you want to keep a small subset of many columns).

---

## Filtering Rows

### Filter by a Column Value

1. Click the dropdown arrow on the column header.
2. Uncheck values to exclude or use the **Text filters** / **Number filters** / **Date filters** submenu for condition-based filtering.

### Remove Blank Rows

1. Click the dropdown on any column.
2. Uncheck the blank / null entry at the bottom of the list.

Or: **Home** ribbon → **Remove Rows** → **Remove Blank Rows**.

### Remove Top N Rows

**Home** → **Remove Rows** → **Remove Top Rows** → enter N. Useful when source files have metadata headers above the actual data.

### Remove Duplicate Rows

1. Select the column(s) that should be unique.
2. Right-click → **Remove Duplicates**.

This keeps the first occurrence of each duplicate combination.

---

## Replacing Values

Replace specific values in a column:

1. Select the column.
2. On the **Transform** ribbon, click **Replace Values**.
3. Enter the value to find and the replacement value.

Common uses:
* Replace `"N/A"`, `"-"`, `"null"` strings with blank (empty string) before changing the type to a number.
* Standardize inconsistent category names (`"USA"` / `"US"` / `"United States"` → `"United States"`).

---

## Splitting Columns

When a single column contains multiple pieces of information:

1. Select the column.
2. On the **Transform** ribbon, click **Split Column**.
3. Choose the split method: **By Delimiter**, **By Number of Characters**, **By Position**, **By Lowercase to Uppercase**, etc.

Example — splitting `"2024-03-15"` stored as text into Year, Month, Day:

1. Split by delimiter `-`.
2. Rename the three resulting columns.
3. Change type to Whole Number.

---

## Trimming and Cleaning Text

Text data from Excel or CSV files often contains leading/trailing spaces:

1. Select the text column.
2. **Transform** → **Format** → **Trim** (removes leading and trailing spaces).
3. **Transform** → **Format** → **Clean** (removes non-printable characters).

Also useful: **Transform** → **Format** → **UPPERCASE** / **lowercase** / **Capitalize Each Word** for standardizing text casing.

---

## Extracting Date Parts

When you have a Date column and need year, month, or day as separate integers:

1. Select the Date column.
2. On the **Add Column** ribbon, click **Date** → **Year**, **Month** → **Month**, etc.

This adds a new column. Power Query generates M like:

```text
AddedYear = Table.AddColumn(Source, "Year", each Date.Year([Order Date]), Int64.Type)
```

---

## Adding a Conditional Column

Equivalent to an IF statement — adds a new column with values based on conditions:

1. On the **Add Column** ribbon, click **Conditional Column**.
2. Build conditions with If / Else If / Else clauses using the UI.

For complex conditions, use a **Custom Column** instead (see Part 2).

---

## Promoting Headers

When the first data row contains column names (common in CSV files where the header was not read):

**Home** → **Use First Row as Headers**.

Or in M: `Table.PromoteHeaders(Source)`.

---

## Best Practices

* Perform type changes **after** renaming columns — steps are more readable when they reference descriptive names.
* Filter out rows you know are invalid (blanks, test records) **as early as possible** in the pipeline — it reduces the rows processed by all downstream steps.
* Use **Remove Other Columns** (keep only what you need) rather than **Remove Columns** (select what to drop) — it is more resilient to source schema changes adding new columns.
* Always trim and clean text columns before using them as merge keys — trailing spaces prevent matches.

---

## References

* [Shape and combine data in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-shape-and-combine-data)
* [Power Query M formula language – Microsoft Learn](https://learn.microsoft.com/en-us/powerquery-m/power-query-m-language-specification)
* [Common Power Query transformations – Microsoft Learn](https://learn.microsoft.com/en-us/power-query/power-query-common-issues)
