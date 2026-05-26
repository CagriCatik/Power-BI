# Creating Interactive Dashboards

## Overview

In Power BI, a **dashboard** is a single-page canvas in the **Power BI Service** (not Desktop) that aggregates tiles from one or more reports and datasets. It provides a high-level summary view — executives and consumers pin the visuals they care about most from their reports onto a single screen.

> **Reference:** [Intro to dashboards for Power BI designers – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboards)
> **Reference:** [Create a Power BI dashboard from a report – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboard-create)

---

## Dashboard vs Report

| Feature | Report | Dashboard |
| --- | --- | --- |
| Created in | Power BI Desktop or Service | Power BI Service only |
| Pages | Multiple | One |
| Visuals | Fully interactive | Tiles (limited interactivity) |
| Filters and slicers | Full support | No filter pane |
| Data sources | One semantic model | Multiple semantic models |
| Auto-refresh | On schedule | Reflects source report refresh |

Use **reports** for deep analysis and filtering. Use **dashboards** for at-a-glance monitoring.

---

## Creating a Dashboard

### Method 1 — New Blank Dashboard

1. In the **Power BI Service**, go to your workspace.
2. Click **New › Dashboard**.
3. Give the dashboard a name.
4. An empty canvas appears — now pin tiles to it from existing reports.

### Method 2 — Pin from a Report

1. Open a published report in the Power BI Service.
2. Hover over any visual — a **pin icon** appears in the top-right corner.
3. Click the pin icon.
4. In the dialog, choose:
   * **Existing dashboard** — add to a dashboard you already created.
   * **New dashboard** — create a new dashboard and add this tile as the first item.
5. Click **Pin**.

The visual now appears as a tile on the selected dashboard.

---

## Dashboard Tiles

Each item on a dashboard is a **tile**. Tiles can come from:

* Report visuals (pinned from reports)
* Entire report pages (pinned as a live page)
* Q&A natural language query results
* Streaming datasets (real-time tiles)
* External images, videos, text boxes, or web content

### Tile Interactions

* **Click a report visual tile** — navigates to the underlying report page.
* **Click a pinned report page tile** — opens the full report page.
* **Resize a tile** — drag the bottom-right handle.
* **Reposition a tile** — drag anywhere on the tile.
* **Edit a tile** — click the ellipsis (…) on the tile for rename, subtitle, hyperlink, or delete options.

---

## Pinning an Entire Report Page

To pin all visuals from a report page as a single live tile:

1. Open the report page in the Service.
2. Click **Pin to dashboard** in the top menu bar.
3. Select an existing or new dashboard.

The entire page renders as a single scrollable tile. It stays in sync with the report page as data refreshes.

---

## Dashboard Layout

* **Drag** tiles to rearrange.
* **Resize** by dragging the handle at the bottom-right corner.
* Aim for a **consistent grid** — Power BI snaps tiles to a grid.
* Use **full-width tiles** for key headline metrics at the top, smaller tiles for supporting charts below.

---

## Real-Time Tiles

For streaming data (IoT sensors, live feeds), a **streaming dataset** can power a real-time tile that updates without a manual refresh. Configure via **New › Streaming dataset** in the workspace.

---

## Dashboard Themes

Under the dashboard **Edit** menu:

* Choose a **Dashboard theme** (light or dark, or upload a custom JSON theme).
* Themes only affect the dashboard canvas background and default tile fonts.

> **Reference:** [Use Dashboard Themes in the Power BI Service – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboard-themes)

---

## Best Practices

* Put the **3–5 most critical KPIs** as card tiles in the top row — viewers should get the headline story in seconds.
* Use **consistent tile sizing** — mixed sizes look unplanned and are harder to scan.
* Link tiles back to their source reports so consumers can drill deeper with a click.
* Add a **text tile** with a brief description of the dashboard's purpose and the last refresh date.
* Keep the dashboard to **one screen** if possible — dashboards are meant for monitoring, not scrolling.

---

## References

* [Intro to dashboards for Power BI designers – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboards)
* [Create a Power BI dashboard from a report – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboard-create)
* [Use Dashboard Themes in the Power BI Service – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboard-themes)
* [Share and Collaborate on Power BI Reports and Dashboards – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-share-dashboards)
