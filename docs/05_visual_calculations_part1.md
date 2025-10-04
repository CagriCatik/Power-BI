# Visual Calculations – Setup and Practical Usage

## Overview

Visual Calculations is a **preview feature** in Power BI Desktop that lets you create calculations directly inside a visual, without adding measures or columns to the data model. This chapter explains how to enable the feature, create basic calculations, format them, and manage their visibility within visuals. It also covers common calculation examples, such as differences, ratios, and averages.

---

## Enabling Visual Calculations

Before using Visual Calculations, the feature must be turned on in **Preview Features**:

1. Go to **File > Options and Settings > Options**.
2. Under **Preview Features**, locate **Visual Calculations**.
3. Check the box to enable it.
4. Click **OK**.
5. Save your report and restart Power BI Desktop if prompted.

Once enabled, a **New calculation** button will appear on the **Home** ribbon when working in a visual.

---

## Creating a Visual Calculation

1. Select a visual (e.g., a table).
2. Click **New calculation** from the **Home** ribbon.
3. A formula bar will appear (similar to Excel).
4. Define your calculation:

   * Assign a name to the field.
   * Use an equals sign `=` followed by your formula.
   * Reference existing fields in the visual by typing `[` to see a field list.
5. Press **Enter** or click the check mark to commit.

**Important:**

* Calculations created this way exist **only in the current visual**.
* They are **not added to the data model** and will not be available in other visuals.

---

## Example Calculations

### 1. Difference Between Sales and Profit

```DAX
Difference = [Sum of Sales] - [Sum of Profit]
```

* Select the table visual containing **Sales** and **Profit**.
* Click **New calculation** and enter the formula above.
* This creates a new column showing the difference between the two measures.

### 2. Profit Ratio (Profit ÷ Sales)

```DAX
Profit Ratio = DIVIDE([Sum of Profit], [Sum of Sales])
```

* `DIVIDE()` is safer than using the `/` operator because it avoids divide-by-zero errors by returning 0 instead.
* Note: **Percentage formatting is not fully supported** for Visual Calculations in preview. The result will appear as a decimal (e.g., 0.45 instead of 45%).

### 3. Average Sale per Product

Steps:

1. Add **Product Name** to the table.
2. Change **Product Name** aggregation to **Distinct count**.
3. Create a new calculation:

```DAX
Average Sale per Product = DIVIDE([Sum of Sales], [Count of Product Name])
```

* This calculates the average sales per unique product for each manufacturer.

---

## Formatting Visual Calculations

Visual Calculations can be formatted through the visual’s **Formatting pane**:

1. Select the visual.
2. Open the **Format pane**.
3. Go to **Specific columns**.
4. Select your calculated field.
5. Adjust:

   * **Display units** (e.g., None, Thousands, Millions).
   * **Decimal places**.

**Limitations:**

* Percentage formatting is currently not supported natively.
* Workarounds require DAX formatting, which is outside the Visual Calculations scope.

---

## Managing Calculations

* **Edit:** Click the calculation name in the field list and choose **Edit calculation** to modify the formula.
* **Hide:** Select the calculation and choose **Hide from visual** to remove it from display while keeping it available in the field list.
* **Reorder:** Change column positions directly in the visual if needed.

---

## Key Characteristics

* **Scope:** Calculations exist only in the visual where they are created.
* **Non-persistent:** They do not become part of the data model or reusable measures.
* **Fast iteration:** Ideal for quick, one-off insights without modifying the dataset.

---

## Best Practices

1. **Use Descriptive Names**
   Clearly label calculations (e.g., `Profit Ratio`, `Average Sale per Product`).

2. **Keep Visual-Specific**
   For metrics used across multiple visuals, create a DAX measure in the data model instead.

3. **Use Safe Functions**
   Prefer `DIVIDE()` to handle divide-by-zero errors gracefully.

4. **Validate Results**
   Compare with standard measures to ensure accuracy before sharing reports.

5. **Format Early**
   Apply formatting immediately for clarity, especially when sharing visuals.

---

## Limitations to Consider

* **Feature Stability:** Still in preview; functionality may change.
* **No Percentage Format:** Profit ratios and similar metrics display as decimals.
* **Visual Scope Only:** Calculations cannot be reused in other visuals or reports.
* **Advanced Formatting Requires DAX:** For percentage or custom formats, a traditional DAX measure is needed.

---

## Summary

Visual Calculations provide a lightweight, visual-level way to perform custom calculations directly in Power BI reports. They enable faster experimentation, reduce model complexity, and allow for simple but powerful metrics such as differences, ratios, and averages. However, they remain best suited for **visual-specific analysis** and **ad-hoc exploration**, while reusable or business-critical calculations should still be created as DAX measures in the data model.
