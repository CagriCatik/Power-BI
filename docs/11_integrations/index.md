# Power BI and Microsoft 365 Integrations

## Overview

Power BI does not exist in isolation — it is deeply integrated with the broader **Microsoft 365** ecosystem. Reports and semantic models connect to Excel, SharePoint, Teams, PowerPoint, and Azure services. Understanding these integrations allows you to build workflows where Power BI serves as the analytical engine while other Microsoft tools serve as the consumption and collaboration layer.

> **Reference:** [Power BI and Microsoft 365 integration – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-share-dashboards)

---

## Integration Overview

| Microsoft 365 Tool | Integration Type | Description |
| --- | --- | --- |
| **Excel** | Analyze in Excel; import Excel files | Browse Power BI datasets from Excel using PivotTables |
| **PowerPoint** | Power BI add-in; export to PPT | Embed live Power BI visuals in presentations |
| **Teams** | Power BI app in Teams | View and discuss reports within Teams channels |
| **SharePoint Online** | Embed web part | Embed a Power BI report on a SharePoint page |
| **OneDrive / SharePoint** | Automatic data refresh | Excel or CSV files stored on OneDrive refresh automatically |
| **Azure Synapse / Fabric** | DirectLake mode; pipelines | Query large datasets directly; orchestrate data pipelines |

---

## Section Contents

| Topic | Description |
| --- | --- |
| Power BI and Excel | Connecting Excel to Power BI; Analyze in Excel; importing Excel data |
| Power BI and PowerPoint | Embedding visuals in presentations; Power BI add-in; exporting slides |

---

## Common Integration Scenarios

* **Finance teams** maintain Excel models and want Power BI dashboards that automatically reflect those files — store the Excel file on SharePoint/OneDrive and connect Power BI to it.
* **Executives** want to see live Power BI data in their regular PowerPoint board decks — use the Power BI add-in for PowerPoint.
* **Analysts** want to do ad-hoc pivoting and slicing of a shared semantic model — use Analyze in Excel to connect a PivotTable to the Power BI dataset without downloading raw data.

---

## References

* [Power BI and Microsoft 365 integration – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-share-dashboards)
* [Power BI and Excel – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-analyze-in-excel)
* [Power BI in Microsoft Teams – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-collaborate-microsoft-teams)
