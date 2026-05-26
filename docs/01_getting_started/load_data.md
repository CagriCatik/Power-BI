# Loading Excel Data and Building a Report

Comprehensive, step-by-step documentation to:

1. Create a semantic model (dataset) in Power BI Service from an Excel file.
2. Build a simple report using a table visual.
3. Save and locate artifacts in a workspace.
4. Apply operational best practices and troubleshooting.

No assumptions beyond the provided transcription. Where broader context is useful, it is labeled clearly.

---

## Terminology

* Semantic model: The data model stored in the Power BI Service. It backs reports and exposes tables, columns, and relationships.
* Dataset: Common term historically used for the model in the Service. In this document, "semantic model" is preferred.
* Report: A set of pages and visuals built on top of a semantic model.
* Workspace: A container in the Service holding semantic models, reports, dashboards, etc. "My Workspace" is your personal area.

---

## Prerequisites

* An Excel workbook containing tabular data. The transcription references a training file (single table on one sheet).
* Ability to use My Workspace or another workspace where you can create content.

If your Excel file is not already formatted as a table in Excel, the Service can still read a sheet, but tables are recommended for cleaner type inference and column detection.

---

## Data Preparation Checklist (Excel)

Recommended before upload:

* One header row with clear column names.
* No merged cells in the data region.
* Values typed consistently per column (dates as dates, numbers as numbers, text as text).
* If possible, format the data as an Excel Table (Insert > Table). Name it meaningfully (e.g., SalesData).
* Remove totals/subtotals from the data region. Keep the dataset row-level and add aggregations in Power BI.

---

## Workflow Overview

1. Open the Power BI Service and go to a workspace.
2. Create a new semantic model and choose Excel as the source.
3. Upload the Excel file (OneDrive recommended, local upload supported per transcription).
4. Authenticate if requested, then select the table or sheet from the workbook.
5. Create the semantic model and wait for the load to finish.
6. Build a simple report (table visual) using fields from the model.
7. Save the report and confirm both the semantic model and the report exist in the workspace.

---

## Detailed Steps

### Access the Service

1. Navigate to [https://app.powerbi.com](https://app.powerbi.com) and sign in.
2. Home page options:

   * New report (quick start), or
   * Create menu for more options.

The transcription proceeds via a workspace for clarity and control.

### Go to a Workspace

1. In the left navigation, select "Workspaces".
2. Choose "My Workspace".
3. Click "New item".

You will see options including "Semantic model" (data model), reports, and more.

### Create a Semantic Model

1. Select "Semantic model".
2. Choose the data source type. Options shown in the transcription:

   * Excel
   * CSV
   * Paste or manual entry
3. Select "Excel".

### Choose Storage and Upload

1. The Service offers to connect from online storage (OneDrive recommended in the transcription).
2. If your file is local, select "Upload file".
3. Use "Browse" and pick the Excel file (e.g., training_data.xlsx).
4. Confirm the selection. The Service uploads the file.
5. Wait for "Upload success".

Note: OneDrive is recommended in the transcription for easier refresh and updates. Local uploads are supported for this lesson.

### Authorize if Prompted

1. If "Next" is disabled, click "Sign in".
2. Authorize your account.
3. Once authorized, the "Next" button is enabled. Click "Next".

### Select Workbook Objects

1. The Service scans for:

   * Tables (preferred)
   * Sheets
2. Select the table if available. The transcription notes that the table and sheet contained the same data.
3. Review the preview:

   * Verify column names.
   * Confirm data types (dates show as date, numeric as decimal, text as text).
4. Click "Create".

### Load and Validate

1. The Service performs:

   * Preparing
   * Loading
   * Finishing
2. After completion:

   * Open the model-backed report canvas.
   * In the right pane, confirm the table (e.g., Data 1) and its fields are visible.
   * Visualizations and Filters panes are available.

---

## Build a Simple Report (Table)

### Insert a Table Visual

1. On the canvas, select the "Table" visual.
2. With the visual selected:

   * Click a categorical field (e.g., Manufacturer) to add it to the table.
   * Drag a numeric field (e.g., Sales) into the visual or into the "Values" well.

Result: Sales are aggregated by Manufacturer. The default aggregation for numeric fields is sum.

### Basic Formatting and Interaction (Optional)

* Sorting: Use the column header dropdown or sort icon on the visual.
* Aggregation: If a numeric column aggregates incorrectly, change it in the Values well (e.g., Sum, Average, Count) or set it to "Do not summarize" when appropriate.
* Resizing: Drag handles on the visual to resize. Expand the canvas region by minimizing the Filters pane for more space.

---

## Save and Locate Artifacts

### Save the Report

1. Click the disk icon.
2. Enter a name (e.g., "My Report").
3. Click "Save".

### Confirm in Workspace

1. Return to "My Workspace".
2. You should now see:

   * The semantic model (the uploaded and created model from Excel).
   * The report (the one you saved).
3. Open the report from the workspace. To edit, click "Edit" in the toolbar.

---

## Operational Guidance

### Storage Choice and Refresh

* OneDrive/SharePoint Online: Recommended in the transcription for simpler update cycles. Edits to the workbook can be surfaced with minimal effort.
* Local upload: Suitable for quick tests or static data. To update, repeat the upload or replace the file as applicable.

For routine updates, keep source files online (OneDrive/SharePoint). This reduces manual steps for data refresh in the Service.

### Workspace Organization

* Use clear, consistent names:

  * Semantic model: e.g., "TrainingData_SemanticModel"
  * Report: e.g., "TrainingData_Report"
* Add descriptions in workspace item settings to document source and purpose.
* Use folders or naming prefixes to distinguish environments (e.g., DEV_, TEST_, PROD_) if working outside "My Workspace".

### Data Types and Quality

* Verify that dates, numbers, and text appear as expected in the preview.
* If types are incorrect in the Service preview:

  * Adjust the source Excel types and re-upload, or
  * For complex transformations, prepare data with Power BI Desktop or dataflows before publishing to the Service.

### Visual Construction Tips

* Start with one visual to validate the model behaves as expected.
* Use fields with distinct roles:

  * Dimensions (e.g., Manufacturer) for grouping.
  * Measures or numeric columns (e.g., Sales) for aggregation.
* Add filters or slicers after validating the base table, if needed.

---

## Troubleshooting

### "Next" Button Disabled

* Cause: Not signed in for authorization.
* Action: Click "Sign in", authorize, retry.

### No Tables Found

* Cause: The workbook may not contain a defined table object; only a sheet is present.
* Action: Select the sheet. If the sheet preview looks incorrect, format the range as a table in Excel and re-upload.

### Data Types Misdetected

* Cause: Mixed or ambiguous values in a column.
* Action: Clean values in Excel, ensure consistent typing, then re-upload.

### Upload Dialog Off-Screen

* Cause: Screen capture or window sizing issue (noted in the transcription).
* Action: Use the system file picker, choose the file, confirm "Open".

### Fields Not Aggregating As Expected

* Cause: Default summarization may not match intent.
* Action: In the Values well, set aggregation explicitly (Sum, Average, Count, Do not summarize).

### Report Not Visible After Save

* Cause: Saved to another workspace or save failed.
* Action: Verify the current workspace, refresh the workspace list, confirm item names.

---

## Best Practices

### Before Upload

* Clean, typed columns in Excel.
* Use an Excel Table for the data region.
* Avoid calculated totals in the raw table.

### During Model Creation

* Prefer "Table" over "Sheet" when both exist.
* Verify previewed data types.

### After Model Creation

* Validate a simple table visual end-to-end.
* Name and save artifacts clearly.
* Keep source files in online storage for easier updates.

For advanced modeling, consider preparing the model in Power BI Desktop or using dataflows, then publishing to the Service.

---

## Quick Reference

* Create model: Workspace > New item > Semantic model > Excel.
* Upload: Upload file > Browse > Select workbook > Upload success.
* Authorize: Sign in if prompted > Next enabled.
* Select objects: Choose Table (preferred) or Sheet > Preview > Create.
* Build: Add Table visual > Add categorical field(s) + numeric field(s).
* Save: Disk icon > Name report > Save.
* Locate: Workspace shows both semantic model and report.

---

## Notes and Limits

* This document follows the exact flow in the transcription: semantic model creation from an Excel file in the Power BI Service, then a single table visual, and save.
* Capacity limits, licensing nuances, and refresh scheduling specifics are not included here. I do not have access to that information.
