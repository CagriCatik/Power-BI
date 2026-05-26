# Mobile Reports

## Overview

Power BI provides a dedicated **mobile layout view** in Power BI Desktop that lets you design a phone-optimised version of any report page. The Power BI Mobile app (iOS and Android) automatically detects and uses this layout when the report is opened on a phone.

> **Reference:** [Power BI Mobile Layout View: Create Optimized Reports – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-create-mobile-optimized-report-mobile-layout-view)
> **Reference:** [Explore Reports in the Power BI Mobile Apps – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/explore-reports/mobile/mobile-reports-in-the-mobile-apps)

---

## Why Create a Mobile Layout?

By default, Power BI Mobile renders the full desktop report and lets users pinch-and-zoom. A **mobile-optimised layout** provides:

* Vertically stacked visuals sized for a portrait screen.
* Larger text and simpler charts that are readable on a small screen.
* Focused content — only the most critical visuals, not the full report.
* A professional first impression for mobile consumers.

---

## Switching to Mobile Layout View

In Power BI Desktop:

1. Go to the **View** ribbon tab.
2. Click **Mobile layout**.
3. A phone-shaped canvas appears with a panel on the right showing all page visuals.

The mobile layout is per report page. You can create a mobile layout for some pages and leave others desktop-only.

---

## Adding Visuals to the Mobile Canvas

1. In the **Mobile layout view**, the right panel lists all visuals on the current page.
2. Drag a visual from the panel onto the phone canvas.
3. Resize and reposition the visual on the canvas.
4. Repeat for each visual you want to include on mobile.

You do not need to include every visual — select only the ones that are most important on a small screen.

---

## Tips for Mobile Layout Design

* **Use full-width cards** for KPI metrics at the top — they read clearly on any screen size.
* **Stack charts vertically** — one chart per row in the portrait layout.
* **Avoid tables with many columns** on mobile — they require horizontal scrolling, which is awkward. Prefer cards or single-metric charts.
* **Use large fonts** — set font sizes 2–4 pts larger than the desktop layout.
* **Simplify charts** — remove legends if they clutter a small chart; use clear titles instead.
* **Slicers** work on mobile — include the most important one or two slicers, styled as dropdowns to save space.

---

## Previewing the Mobile Layout

1. In **Mobile layout view**, click **Preview** (if available) or publish the report to the Service.
2. Open the Power BI Mobile app and navigate to the report.
3. The app detects the mobile layout and renders it automatically in portrait mode.
4. Rotate the device to landscape — the app switches to the desktop layout.

---

## Power BI Mobile App Features

| Feature | Availability |
| --- | --- |
| View reports and dashboards | Yes |
| Cross-filter visuals | Yes |
| Slicer interaction | Yes |
| Annotate and share screenshots | Yes |
| Set up data alerts on dashboard tiles | Yes |
| Create or edit reports | No (view only) |
| Offline access | Limited (cached data) |

---

## Dashboard Mobile View

Dashboards in the Power BI Service automatically adapt to mobile screens — tiles reflow into a single column. You can also customise the phone dashboard layout:

1. Open the dashboard in the Power BI Service on a browser.
2. Click **Edit › Phone view**.
3. Rearrange tiles for the phone layout independently of the desktop dashboard.

---

## Best Practices

* Design mobile layouts **after** the desktop report is complete — it is an enhancement, not a starting point.
* Prioritise the **top 3–5 most-checked metrics** for the mobile layout — operational KPIs executives check on the go.
* Test the mobile layout on a **real device** before publishing — the emulator in Desktop does not catch all display issues.
* Keep the mobile page to **one scroll length** — consuming data on mobile should require minimal scrolling.

---

## References

* [Power BI Mobile Layout View – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-create-mobile-optimized-report-mobile-layout-view)
* [Explore Reports in the Power BI Mobile Apps – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/explore-reports/mobile/mobile-reports-in-the-mobile-apps)
