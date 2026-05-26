# Pinning Visualizations to Dashboards

## Overview

**Pinning** is the act of copying a visual from a report into a dashboard tile. The tile stays linked to the underlying report and refreshes when the semantic model refreshes. Pinning is the primary way to build a Power BI dashboard from existing reports.

> **Reference:** [Pin an Entire Report Page to a Power BI Dashboard – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboard-pin-live-tile-from-report)

---

## Pinning a Single Visual

1. Open a published report in the **Power BI Service**.
2. Hover over the visual you want to pin — a toolbar appears in the top-right corner of the visual.
3. Click the **pin icon** (thumbtack).
4. In the **Pin to dashboard** dialog:
   * Select **Existing dashboard** (choose a dashboard from the list), or
   * Select **New dashboard** (type a name to create one).
5. Click **Pin**.

The visual now appears as a tile on the selected dashboard.

---

## Pinning an Entire Report Page

1. Open a published report page.
2. In the top menu bar, click **Pin to dashboard**.
3. Select **Existing** or **New dashboard**.
4. Click **Pin live page**.

The entire page renders as a single **live tile**. It retains all the page layout, visuals, and interactions — clicking any visual on the live tile navigates into the full report.

---

## Tile Behaviour After Pinning

| Action | Behaviour |
| --- | --- |
| Click a single-visual tile | Opens the underlying report at the page where the visual lives |
| Click a live page tile | Opens the full report page |
| Data refresh | Tile updates automatically when the semantic model refreshes |
| Cross-filter | Not available on dashboard tiles; full interactivity requires opening the report |

---

## Editing a Pinned Tile

On the dashboard, click the **ellipsis (…)** on a tile to access:

* **Edit details** — change the tile title, subtitle, and add a custom hyperlink.
* **Open in focus mode** — expand the tile to full-screen.
* **Delete tile** — removes the tile from the dashboard (does not affect the source report).
* **Go to report** — navigates to the source report.

---

## Pinning from Q&A

Results from a **Q&A** natural language query can also be pinned:

1. On a dashboard, click the **Ask a question about your data** box.
2. Type a query (e.g., "total sales by region this year").
3. Power BI generates a chart.
4. Click the **pin icon** to save it as a tile.

---

## Pinning Tiles from Other Dashboards

You can reuse tiles from one dashboard on another:

1. On a dashboard, click the ellipsis **(…)** on a tile.
2. Select **Pin tile**.
3. Choose the destination dashboard.

---

## Refreshing Pinned Tiles

* Tiles backed by **scheduled refresh** datasets update on the refresh schedule.
* **Real-time streaming tiles** update continuously.
* To force an immediate refresh: in the workspace, click the **Refresh now** button on the semantic model.

---

## Best Practices

* Pin **card and KPI tiles** at the top of the dashboard for a headline summary.
* Pin **chart tiles** at a meaningful size — a line chart pinned too small is unreadable.
* Use **custom tile subtitles** to explain what the tile shows and the data's time scope.
* Add a **hyperlink** to tiles so consumers can navigate directly to the relevant report page for details.
* Avoid pinning the same visual from multiple report versions — keep one canonical report as the tile source.

---

## References

* [Create a Power BI dashboard from a report – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboard-create)
* [Pin an Entire Report Page to a Power BI Dashboard – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboard-pin-live-tile-from-report)
* [Intro to dashboards for Power BI designers – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboards)
