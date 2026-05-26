# Power BI and PowerPoint

## Overview

Power BI integrates with PowerPoint through the **Power BI add-in for PowerPoint**, which embeds live, interactive Power BI report pages directly into PowerPoint slides. Unlike static screenshots, embedded visuals update when the underlying data changes and remain interactive — viewers can filter and slice data from within the presentation.

> **Reference:** [Embed a Power BI report page in PowerPoint – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-power-bi-powerpoint-add-in-about)

---

## The Power BI Add-in for PowerPoint

### Installing the Add-in

The add-in is available from the Microsoft 365 store:

1. In PowerPoint, go to **Insert** → **Get Add-ins**.
2. Search for **Microsoft Power BI**.
3. Click **Add**.

The Power BI icon appears in the Insert ribbon.

### Embedding a Report Page

1. In PowerPoint, open the slide where you want to embed the report.
2. Click **Insert** → **Power BI**.
3. A placeholder appears with a URL entry field.
4. In the **Power BI Service**, open the report page you want to embed.
5. Copy the URL from the browser address bar.
6. Paste it into the add-in placeholder in PowerPoint.
7. The report renders live on the slide.

The viewer must have Power BI access to the report — the add-in respects all Power BI permissions, including Row-Level Security.

> **Reference:** [Use the Power BI add-in for PowerPoint – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-power-bi-powerpoint-add-in-install)

---

## Live vs Snapshot Mode

| Mode | Description | Use case |
| --- | --- | --- |
| **Live** (default) | Queries the Power BI model in real time when the slide is viewed | Always shows current data; requires internet and Power BI access |
| **Snapshot** | Takes a static image of the current state | For distributing to people without Power BI access; data is fixed at capture time |

Switch between modes in the add-in sidebar when the embed is selected on the slide.

---

## Exporting a Power BI Report to PowerPoint

For a static export of all report pages as slide images:

1. In the **Power BI Service**, open the report.
2. Click **Export** → **PowerPoint**.
3. Choose to export **Current values** (data as of now, respecting current filters) or **Default values** (report defaults without personal filters).
4. Click **Export**.

A `.pptx` file downloads with one slide per report page. Visuals are high-resolution images — not live embeds. This is useful for distributing reports to recipients without Power BI licenses.

> **Reference:** [Export reports to PowerPoint – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/end-user-powerpoint)

---

## Exporting from Power BI Desktop

From Power BI Desktop you can also export to PowerPoint:

1. **File** → **Export** → **Export to PowerPoint**.
2. All pages in the report are exported as static slide images.

---

## Storytelling with Power BI in PowerPoint

The Power BI add-in is designed for **data storytelling** — combining narrative slides with live data:

* Introduce context on a plain text slide.
* Follow with a live Power BI slide showing supporting data.
* Annotate with PowerPoint shapes and arrows overlaid on the embedded visual.
* Use the embedded visual's built-in filters during the presentation to answer audience questions live.

---

## Interactivity in Presentations

When presenting with the Power BI add-in:

* **Cross-filter** — clicking a data point on one chart cross-filters others on the same report page.
* **Slicers** — visible slicers on the embedded page are interactive during the slideshow.
* **Drill-down** — drill-down enabled visuals can be drilled during the presentation.
* **Bookmarks** — if the report has bookmarks, they can be navigated within the embed.

---

## Requirements and Limitations

* The **Power BI add-in** requires Microsoft 365 (PowerPoint for Windows or Web) and Power BI Pro or Premium per user license for the viewer.
* **Static export** (File → Export → PowerPoint) works for any report and produces a `.pptx` with image slides that do not require Power BI access to view.
* **Certified custom visuals** render in exports; uncertified custom visuals may not render correctly.
* Very large reports (many pages, many visuals) may time out during static export.

---

## Best Practices

* Use the **live add-in embed** for internal presentations where all attendees have Power BI access — it stays current without re-exporting.
* Use **static export** for board packs, external stakeholder decks, or archived snapshots.
* Design the report page to be **presentation-ready**: large fonts, high-contrast colors, no dense tables — it renders at slide dimensions.
* Set a **specific bookmark** as the default state of the embedded page so it opens to the right view during the presentation.

---

## References

* [Embed a Power BI report page in PowerPoint – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-power-bi-powerpoint-add-in-about)
* [Use the Power BI add-in for PowerPoint – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-power-bi-powerpoint-add-in-install)
* [Export reports to PowerPoint – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/end-user-powerpoint)
