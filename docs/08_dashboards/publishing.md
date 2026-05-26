# Publishing Reports to the Power BI Service

## Overview

After building a report in Power BI Desktop, you **publish** it to the Power BI Service (cloud) to share it with colleagues, embed it in Teams or SharePoint, schedule data refreshes, and create dashboards. Publishing uploads both the report and its semantic model (dataset) to a workspace.

> **Reference:** [Publish semantic models and reports from Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-upload-desktop-files)

---

## Prerequisites

* A valid Power BI account (work or school email, Pro or Premium Per User license for sharing).
* Power BI Desktop with a saved `.pbix` file.
* A workspace in the Power BI Service (My Workspace works for personal use; a shared workspace for team collaboration).

---

## How to Publish

1. In Power BI Desktop, click **Home › Publish** (or press `Ctrl + Shift + P`).
2. Sign in if prompted.
3. Select the **destination workspace** from the list.
4. Click **Select**.
5. Power BI Desktop uploads the file. A success dialog appears with a link to the published report.

---

## What Gets Published

| Item | Published as |
| --- | --- |
| Report pages and visuals | Report artifact in the workspace |
| Data model (tables, relationships, measures) | Semantic model artifact |
| Report theme | Embedded in the report |
| Bookmarks and drill-through | Embedded in the report |
| Data itself (Import mode) | Embedded in the semantic model |
| DirectQuery / Live connection | Only metadata; data stays at source |

---

## After Publishing

### Open the Report in the Service

Click **Open \[filename\] in Power BI** in the success dialog, or navigate to the workspace in a browser and click the report name.

### Schedule Data Refresh

If the semantic model uses imported data, schedule automatic refresh:

1. In the workspace, click the ellipsis **(…)** next to the semantic model.
2. Select **Settings**.
3. Under **Scheduled refresh**, configure:
   * **Refresh frequency**: Daily, Weekly.
   * **Time slots**: up to 8 refreshes per day on Pro, 48 on Premium.
   * **Credentials**: set data source credentials if prompted.

### Re-publishing

When you update the report in Desktop and re-publish to the same workspace and report name, Power BI **overwrites** the existing report and semantic model. Consumer views of the report reflect the new version.

---

## Publishing to a Different Workspace

Each publish targets **one workspace** at a time. To publish to multiple workspaces (e.g., Dev → Test → Production), either:

* Publish manually to each workspace by changing the destination.
* Use **Power BI Deployment Pipelines** to automate promotion through environments.

---

## Workspace Roles and Visibility

| Role | Can publish | Can view | Can edit |
| --- | --- | --- | --- |
| **Admin** | Yes | Yes | Yes |
| **Member** | Yes | Yes | Yes |
| **Contributor** | Yes | Yes | No (app) |
| **Viewer** | No | Yes | No |

Only Admin, Member, and Contributor roles can publish content to a workspace.

---

## Overwrite Confirmation

If a report with the same name already exists in the workspace, Power BI asks for confirmation before overwriting. The confirmation dialog lists the report name — verify you are overwriting the correct report before proceeding.

---

## Best Practices

* **Save the `.pbix` file** before publishing to ensure the latest version is uploaded.
* Use **meaningful workspace names** that reflect the team or project (e.g., "Finance – Production").
* Publish to a **Development workspace** first, test, then promote to Production using Deployment Pipelines.
* **Set data source credentials** immediately after publishing — scheduled refreshes fail without them.
* Avoid publishing directly to **My Workspace** for content meant to be shared — use a team workspace instead.

---

## References

* [Publish semantic models and reports from Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-upload-desktop-files)
* [Share and Collaborate on Power BI Reports and Dashboards – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-share-dashboards)
* [Publish an app in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-create-distribute-apps)
