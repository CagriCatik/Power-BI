# Visual Calculations – Built-in Functions

## Overview

Power BI’s **Visual Calculations** feature includes several **built-in functions** that simplify creating common analytical metrics directly within a visual. These functions allow report builders to quickly calculate percentages, running totals, and comparisons (e.g., difference from previous value) without creating DAX measures in the data model.

This chapter explains how to use these built-in functions, customize their names, and format their results.

---

## Accessing Built-in Functions

1. Select a visual (e.g., table) containing fields to analyze.
2. Click **New calculation** on the **Home** ribbon.
3. In the formula bar, click the **Functions** dropdown (fx icon).
4. A list of available built-in functions will appear (e.g., **Percentage of Grand Total**, **Running Sum**, **Versus Previous**).

You can rename the resulting calculation by editing its field name before or after committing.

---

## Example Built-in Functions

### 1. Percentage of Grand Total

Calculates each row’s value as a percentage of the total.

```DAX
Percent Sales = DIVIDE([Sum of Sales], COLLAPSEALL([Sum of Sales]), ROWS)
```

* **`DIVIDE()`** performs safe division (avoiding divide-by-zero errors).
* **`COLLAPSEALL()`** gets the overall total regardless of filters applied to rows.
* **`ROWS`** indicates the calculation is across the table rows.

**Notes:**

* Output will be decimal values (e.g., 0.45 for 45%) since percentage formatting is not currently supported in Visual Calculations.
* You can rename the calculation to something descriptive, such as `Percent Sales`.

---

### 2. Running Total

Cumulatively adds the values down the rows.

```DAX
Running Total = RUNNINGSUM([Sum of Sales])
```

* Useful for tracking cumulative sales, revenue, or similar metrics.
* Apply formatting (e.g., no decimal places) via **Format pane > Specific columns**.

---

### 3. Difference from Previous

Calculates the change between the current row and the previous row.

```DAX
Diff Previous = VERSUSPREVIOUS([Sum of Sales])
```

* Returns the current value minus the previous value in the sequence.
* Ideal for trend analysis or detecting step changes in data.

Other available variations:

* **Versus Next** – compares against the next row.
* **Versus First** – compares against the first row.
* **Versus Last** – compares against the last row.

---

## Formatting Results

1. Select the visual.
2. Open the **Format pane**.
3. Under **Specific columns**, choose the calculated field.
4. Adjust:

   * **Display units** (e.g., None, Thousands).
   * **Decimal places**.

**Limitations:**

* No native percentage symbol for percentage-based calculations.
* Decimal display is the default for percentage outputs.

---

## Managing Calculations

* **Rename:** Change the calculation name when creating or by editing later.
* **Edit:** Click the calculation field and select **Edit calculation** to modify the formula.
* **Hide:** Use the **Hide from visual** option if you want to remove it from the table but keep it available in the field list.

---

## Best Practices

1. **Use Built-in Functions When Possible**
   Simplify analysis by leveraging ready-made functions like `Running Sum` or `Versus Previous` before writing custom DAX.

2. **Rename Clearly**
   Provide meaningful names (e.g., `Percent Sales`, `Sales Change vs Previous`) for clarity.

3. **Format for Readability**
   Always adjust display units and decimal places to improve report presentation.

4. **Experiment**
   Built-in functions are great for rapid testing and iterative exploration.

---

## Limitations

* **Preview Feature:** Stability and supported functions may change over time.
* **No Percentage Formatting:** Percentage outputs are decimals by default.
* **Visual Scope Only:** Functions are tied to the visual and not reusable elsewhere.
* **Advanced Metrics Require DAX:** For custom or complex formatting/logic, create standard DAX measures.

---

## Summary

Power BI’s Visual Calculations include **built-in functions** that allow quick, no-code analytics inside visuals. Common options like **Percentage of Grand Total**, **Running Total**, and **Difference from Previous** make it easy to analyze data trends and context without touching the data model. While flexible and fast for **visual-specific insights**, these calculations remain limited in formatting and reusability compared to full DAX measures.
