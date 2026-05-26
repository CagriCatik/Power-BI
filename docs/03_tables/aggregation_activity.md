# Methods of Aggregation — Practical Activity

## Objective

Practice changing aggregation methods on a table visual and observe how each method changes the displayed values. By the end you will understand which aggregation is appropriate for different analytical scenarios.

---

## Setup

Open the Power BI Desktop file with the training dataset. Add a new report page named **"Aggregation Activity"**.

---

## Tasks

### Task 1 — Sum (Default)

1. Add a **Table visual** with fields: **Category** and **Sales**.
2. Confirm that **Sales** is aggregated as **Sum** (check the chevron in the Values well).
3. Note the total at the bottom of the table — it is the grand sum of all sales.

**Question:** Which category has the highest total sales?

---

### Task 2 — Average

1. Click the **chevron (∨)** next to **Sales** in the Values well.
2. Change aggregation to **Average**.
3. Observe how the values change.

**Question:** Which category has the highest average sales per transaction? Is it the same category as the highest total sales?

---

### Task 3 — Count vs Count (Distinct)

1. Add a second table visual on the same page.
2. Add fields: **Region** and **CustomerID** (or an order ID column).
3. Change the **CustomerID** aggregation to **Count** — this counts the number of rows per region.
4. Duplicate the CustomerID column in the Values well by adding it a second time.
5. Change the second instance to **Count (Distinct)** — this counts unique customer IDs.

**Question:** For any region where Count and Count (Distinct) differ — what does that tell you?

---

### Task 4 — Minimum and Maximum

1. Add a third table visual with: **Product** and **Sales**.
2. Add **Sales** twice to the Values well.
3. Set the first to **Minimum** and rename it "Lowest Sale".
4. Set the second to **Maximum** and rename it "Highest Sale".

**Question:** Which product has the widest range between its minimum and maximum sale values?

---

### Task 5 — Don't Summarize

1. If your dataset has a numeric ID column (e.g., OrderID, ProductID), add it to a table.
2. Observe that by default it shows a Sum — a meaningless number for an ID.
3. Change aggregation to **Don't summarize**.
4. Note that the column now shows the raw value per row.

---

### Task 6 — Model-Level Default

1. Go to **Data View**.
2. Select the OrderID column (or equivalent).
3. In the **Column tools** ribbon, change **Summarization** to **Don't summarize**.
4. Return to Report View.
5. Add the column to a new visual — confirm it no longer defaults to Sum.

---

## Reflection Questions

* When would you use **Median** instead of **Average**?
* Why might **Count (Distinct)** be more useful than **Count** for a customer analysis?
* What is the risk of showing **Don't summarize** on a category column in a table that groups rows?

---

## Reference

* [Aggregates in Power BI service – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/service-aggregates)
