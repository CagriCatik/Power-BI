# Load Data into the Power BI Service

## Overview

The **Power BI Service** allows you to upload data directly to the cloud, build reports, and share them without using Power BI Desktop. This chapter explains how to upload an Excel dataset into the Power BI Service, create a **semantic model** (data model), and build a simple table report. It provides a step-by-step guide from data upload to report saving and managing content in **My Workspace**.

---

## Steps to Upload Data into Power BI Service

### 1. Navigate to Your Workspace

1. From the **Home page**, click on **Workspaces** in the left-hand navigation panel.
2. Select **My Workspace** (your personal storage area in Power BI Service).

> **Note:** My Workspace is available to all users, even on the free license. However, reports created in the free license cannot be shared with other users.

---

### 2. Create a New Semantic Model

1. In **My Workspace**, click **New** (or **New item**).
2. Select **Semantic Model**.

   * A **semantic model** is the dataset that stores your uploaded data and supports your report visuals.
3. Choose the data source type:

   * **Excel**
   * CSV
   * Paste or manually enter data

For this example, select **Excel**.

---

### 3. Upload Your Excel File

1. Power BI will prompt for a file location.

   * If possible, store your files on **OneDrive** for easier refresh and updates.
   * For local files, select **Upload File** and browse to the location of your Excel file.
2. Select the file and click **Open**.
3. If prompted, sign in to your account to authorize the upload.

Once uploaded successfully, click **Next**.

---

### 4. Select Data from the Workbook

* Power BI scans the workbook and detects **tables** and **sheets**.
* Choose the **table** (recommended) or sheet you want to load.
* Preview the data to confirm:

  * Correct column headers
  * Accurate data types (e.g., dates, numbers, text)

Click **Create** to load the selected data into the Power BI Service.

---

## Creating a Quick Report

### 1. Explore the Report Canvas

Once the data is loaded:

* The **Data Pane** (right side) lists your dataset and fields.
* The **Visualizations Pane** shows available chart types and visual elements.
* The **Filters Pane** lets you apply filters to visuals or pages.

### 2. Add a Table Visual

1. Click on the **Table** icon from the Visualizations pane to create a table placeholder on the canvas.
2. Add fields to the table:

   * Click a field (e.g., `Manufacturer`) to add it automatically.
   * Drag fields (e.g., `Sales`) and drop them into the table visual or onto the visual’s **Values** area.
3. Power BI will automatically **aggregate numerical fields** (e.g., summing sales).

### 3. Save the Report

1. Click the **Save** (disk) icon in the top menu.
2. Enter a name for your report (e.g., *My Report*).
3. Click **Save**.

Your report and its dataset (semantic model) are now stored in **My Workspace**.

---

## Managing Uploaded Data and Reports

* **Datasets:** Your uploaded Excel file becomes a **semantic model** that can be reused for new reports.
* **Reports:** The report you created appears under **My Workspace** and can be opened or edited later.
* **Edit Reports:** Open the report, click **Edit**, and modify visuals or fields as needed.

---

## Best Practices

1. **Use OneDrive or SharePoint:** Storing source files online makes refreshes easier and keeps data up to date.
2. **Name Models Clearly:** Use descriptive names for semantic models and reports to keep content organized.
3. **Start Simple:** Use table visuals to verify data before building advanced visuals.
4. **Manage Access Early:** Remember, free accounts cannot share reports. Upgrade to **Pro** or **Premium Per User** if collaboration is required.

---

## Summary

Uploading data to the **Power BI Service** is straightforward and lets you build reports without Power BI Desktop. By creating a **semantic model** from an Excel file, you can quickly explore your data using the report canvas, add visuals such as tables, and save the report to **My Workspace**. These steps form the foundation for working entirely in the cloud and enable faster sharing and collaboration when combined with appropriate licensing.
