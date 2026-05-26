# Cards Visualization

## Overview

A **card visual** displays a single aggregated value prominently — ideal for KPIs, summary metrics, and headline numbers on a dashboard. Power BI offers a modern card visual with rich layout options including multiple values, reference labels, and conditional callout images.

> **Reference:** [Create a card visual in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-card-visual-new-format-settings)

---

## Card Visual Types

| Type | Description |
| --- | --- |
| **Card** | Single measure shown large and prominently |
| **Multi-row card** | Multiple measures stacked vertically |
| **New card visual** | Modern card with callout values, reference labels, and layout control |

The **new card visual** (enabled from late 2023 onwards) is the recommended option for new reports — it supports multiple data fields, categorization, and richer formatting than the legacy card.

---

## Adding a Card Visual

1. In the **Visualizations pane**, click the **Card** icon.
2. Drag a **measure** or **numeric column** into the **Fields** well (or the **Callout value** well in the new card).
3. The value appears large and centred on the visual.

---

## Card Fields (New Card Visual)

| Well | Purpose |
| --- | --- |
| **Callout value** | The primary large number displayed |
| **Category** | Groups cards side by side by a dimension |
| **Reference labels** | Additional small values shown below the callout |
| **Tooltips** | Values shown on hover |

By placing a dimension in **Category**, a single card visual renders one card per category value — effectively a small-multiples card layout.

---

## Formatting a Card

### Callout Value

Under **Format visual › Callout value**:

* **Display units** — Auto, None, Thousands (K), Millions (M), Billions (B).
* **Decimal places** — set the precision of the displayed number.
* **Font family, size, bold, italic** — control the large number's typography.
* **Font color** — set a fixed color or use conditional formatting.

### Reference Labels

Under **Format visual › Reference labels**:

* Add additional measures to show secondary context below the main value.
* Format independently with smaller font size and a different color.

### Card Layout

Under **Format visual › Card**:

* **Padding** — internal whitespace.
* **Background color** — card fill.
* **Border** — show/hide a border with custom color and width.
* **Shadow** — add a drop shadow for depth.

---

## Legacy Card (Single Value)

The original card visual has a simpler field well:

* **Fields** — one measure only.
* **Category label** — toggles the measure name below the value.

Formatting is in **Format visual**:

* **Data label** — font, size, color, display units, decimal places.
* **Category label** — toggle and format the label text below the number.

---

## KPI Visual vs Card

For trend-aware metrics, consider the **KPI visual** instead of a card:

| Feature | Card | KPI |
| --- | --- | --- |
| Shows trend over time | No | Yes (sparkline) |
| Compares to a target | No | Yes (target line) |
| Status icon (up/down) | No | Yes |
| Single large value | Yes | Yes |

> **Reference:** [Key Performance Indicator (KPI) visuals – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-kpi)

---

## Multi-Row Card

Displays several measures in a vertical list — useful for a quick summary panel on a dashboard sidebar.

1. Select the **Multi-row card** icon.
2. Add multiple measures to the **Fields** well.
3. Each measure appears as its own row with its label and value.

Formatting options include font color, background, border, and data label settings identical to the single card.

---

## Best Practices

* Use cards for **3–5 headline KPIs** at the top of a dashboard page.
* Show **context** next to a card value with a reference label (e.g., display this month's revenue alongside last month's revenue).
* Apply **conditional font color** to the callout value — green for on-target, red for below-target — so status is visible at a glance.
* Pair cards with a **slicer** so the headline numbers respond to time period or region selections.

---

## References

* [Create a card visual in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-card-visual-new-format-settings)
* [Key Performance Indicator (KPI) visuals – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-kpi)
* [Overview of visualizations in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualizations-overview)
