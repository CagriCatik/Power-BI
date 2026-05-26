# Power BI and Excel

## Overview

Power BI and Excel have a bidirectional relationship. You can import Excel files into Power BI as data sources, and you can connect Excel to Power BI semantic models for live PivotTable analysis. Together, they cover both structured modeling (Power BI) and flexible ad-hoc analysis (Excel).

> **Reference:** [Analyze in Excel for Power BI service – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-analyze-in-excel)

---

## Importing Excel Data into Power BI

Excel workbooks are one of the most common data sources in Power BI:

1. In Power BI Desktop, click **Get data** → **Excel workbook**.
2. Navigate to the `.xlsx` or `.xls` file.
3. The **Navigator** dialog opens, listing all sheets and named tables in the workbook.
4. Select the sheets or tables to import.
5. Click **Transform Data** to open Power Query, or **Load** to import directly.

### Connecting to OneDrive or SharePoint

For automatic refresh in the Power BI Service, store the Excel file on OneDrive for Business or SharePoint Online:

1. In Power BI Desktop, use **Get data** → **SharePoint folder** or **SharePoint Online List**.
2. Enter the SharePoint site URL.
3. Select the file.
4. When published to the Service, the dataset refreshes from the live SharePoint/OneDrive path — no gateway required for files stored in the cloud.

> **Reference:** [Import data from Excel workbooks – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/connect-data/service-excel-workbook-files)

---

## Analyze in Excel

**Analyze in Excel** lets authorized users connect directly to a Power BI semantic model from Excel, building PivotTables, PivotCharts, and using Cube functions — all reading live data from the published model without downloading the underlying data.

### Starting Analyze in Excel

1. In the **Power BI Service**, find the semantic model in a workspace.
2. Click the ellipsis **(…)** next to the dataset → **Analyze in Excel**.
3. An `.odc` file (Office Data Connection) downloads.
4. Open it in Excel — Excel connects to the Power BI semantic model.
5. A PivotTable connected to the model opens, ready to use.

### Using the PivotTable

* **Rows, Columns, Values, Filters** in the PivotTable Fields pane correspond to dimensions and measures in the Power BI model.
* Drag measures from the model into **Values**.
* Drag dimension columns into **Rows** or **Columns**.
* Use **Filters** or **Slicers** for context filtering.

All calculations use the Power BI model's DAX measures — including CALCULATE, time intelligence, and security filters (Row-Level Security is enforced).

### Requirements

* The user must have **Build** permission on the semantic model (or be at least a Contributor in the workspace).
* Excel 2016 or later (Microsoft 365 Excel recommended).
* Internet connectivity to the Power BI Service.

---

## Excel Cube Functions

Analyze in Excel also exposes **Cube functions** for cell-level access to model data:

```text
=CUBEVALUE("ThisWorkbookDataModel", "[Measures].[Total Revenue]", "[Products].[Category].[Electronics]")
```

Cube functions provide more flexibility than PivotTables for building custom Excel report layouts, but they require knowing the DAX member syntax.

---

## Live Connection vs Import

| Mode | Description | Use case |
| --- | --- | --- |
| Import | Data copied into Power BI at refresh time | Fastest performance; works offline |
| Live Connection (Analyze in Excel) | Excel reads from Power BI model in real time | Ad-hoc analysis; always current |
| DirectQuery | Power BI queries source on demand | Large or real-time data sources |

For most Analyze in Excel scenarios the mode is effectively a **live connection** — every PivotTable update sends a query to the Power BI model.

---

## Exporting Data from Power BI to Excel

Report consumers can export underlying visual data to Excel from any Power BI report:

1. Click the ellipsis **(…)** on a visual → **Export data**.
2. Choose **Summarized data** (aggregated, as displayed) or **Underlying data** (raw rows, if permitted).
3. Select format: `.xlsx` or `.csv`.
4. Click **Export**.

Admins can restrict this feature in the Power BI tenant settings.

---

## Featured Tables in Excel

Power BI **featured tables** (defined in Power BI Desktop) expose semantic model tables as Excel data types:

1. In Power BI Desktop, open the Model view, select a table, and in **Properties** enable **Featured table**.
2. After publishing, Excel users on Microsoft 365 can use the table as an **Excel data type** — linking Excel cells to rows in the Power BI table (similar to Stocks or Geography data types).

This enables look-up enrichment in Excel backed by the Power BI model.

> **Reference:** [Create featured tables in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-excel-featured-tables)

---

## Best Practices

* Store Excel source files on **OneDrive for Business or SharePoint** — not on local drives — for reliable scheduled refresh.
* Use **named tables** (Ctrl+T in Excel) rather than raw sheet ranges — named tables are more resilient to row additions and column reordering.
* For large datasets, avoid importing from Excel; instead use Excel as a lightweight lookup table and keep large transactional data in a proper database.
* Use **Analyze in Excel** for self-service analysis rather than building one-off reports in Power BI Desktop for every analyst request.

---

## References

* [Analyze in Excel for Power BI service – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-analyze-in-excel)
* [Import data from Excel workbooks – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/connect-data/service-excel-workbook-files)
* [Create featured tables in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-excel-featured-tables)
* [Connect Excel to Power BI datasets – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-connect-excel-power-bi-datasets)
