# Using Custom Visualizations

## Overview

Beyond the built-in chart library, Power BI supports **custom visuals** — third-party or developer-built visualizations packaged as `.pbiviz` files. Thousands of custom visuals are available on **Microsoft AppSource**, covering specialised charts (bullet charts, Gantt charts, chord diagrams, word clouds, advanced maps, and more) that extend Power BI's out-of-the-box capabilities.

> **Reference:** [Main sources for acquiring Power BI custom visuals – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/developer/visuals/power-bi-custom-visuals)

---

## Sources of Custom Visuals

| Source | Description |
| --- | --- |
| **AppSource** | Microsoft-curated marketplace with certified and uncertified visuals |
| **Certified visuals** | Passed Microsoft security review; can be exported to PDF and PowerPoint |
| **Organizational visuals** | Uploaded by your Power BI Admin to your tenant's visual store |
| **Imported `.pbiviz` files** | Developer or community visuals uploaded directly from a file |

---

## Adding a Custom Visual from AppSource

1. In Power BI Desktop, click the **ellipsis (…)** in the Visualizations pane → **Get more visuals**.
2. The Power BI visuals marketplace opens.
3. Search for the visual (e.g., "Bullet Chart", "Gantt", "Word Cloud").
4. Click the visual → **Add**.
5. The visual icon appears in your Visualizations pane.

---

## Importing a `.pbiviz` File

For visuals not on AppSource or for offline environments:

1. Click the **ellipsis (…)** in the Visualizations pane → **Import a visual from a file**.
2. Navigate to the `.pbiviz` file.
3. Click **Open**.
4. Accept the security warning — custom visuals can execute code; only import from trusted sources.

---

## Organizational Visuals

Power BI Admins can upload approved visuals to the organisational store, making them available to all users in the tenant without requiring individual imports:

1. Admin portal → **Organizational visuals**.
2. Upload the `.pbiviz` file.
3. The visual appears in every Power BI Desktop and Service instance in the organisation under **My organization** in the visuals pane.

---

## Using a Custom Visual

Custom visuals work identically to built-in visuals:

1. Click the custom visual icon in the Visualizations pane.
2. Assign fields to the visual's wells (field names vary by visual).
3. Use the **Format visual** pane to style the visual according to its own formatting options.

Each custom visual defines its own field wells and formatting options — consult the visual's documentation on AppSource for specifics.

---

## Certified vs Uncertified Visuals

| Feature | Certified | Uncertified |
| --- | --- | --- |
| Passed Microsoft security review | Yes | No |
| Export to PDF/PowerPoint | Yes | No |
| Access to external resources | No | Yes (potential risk) |
| Recommended for enterprise use | Yes | Use with caution |

Filter for **Certified** visuals in the AppSource marketplace to ensure the visual meets Microsoft's security criteria.

> **Reference:** [Develop custom visuals in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/developer/visuals/develop-power-bi-visuals)

---

## Popular Custom Visual Categories

| Category | Example visuals |
| --- | --- |
| Advanced charts | Bullet chart, Sankey diagram, Box plot |
| Project management | Gantt chart, Timeline |
| Text analysis | Word cloud, Text filter |
| Geographic | Icon map, Flow map, Synoptic Panel |
| Statistical | Histogram, Violin plot, Correlation heatmap |
| KPI | Sparkline, Linear gauge, Tachometer |

---

## Developing Your Own Custom Visual

Organizations with specific needs can build custom visuals using the **Power BI Visuals SDK** (TypeScript/JavaScript):

1. Install Node.js and the `pbiviz` CLI tool.
2. Scaffold a new visual with `pbiviz new VisualName`.
3. Implement the visual logic in TypeScript.
4. Package with `pbiviz package` → produces a `.pbiviz` file.
5. Import into Power BI Desktop or submit to AppSource.

> **Reference:** [Develop custom visuals in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/developer/visuals/develop-power-bi-visuals)

---

## Best Practices

* Prefer **certified visuals** for enterprise reports — they are safer and support PDF/PowerPoint export.
* Use **organizational visuals** to standardise the visual library across your tenant.
* Test custom visuals with your actual data **before** using them in production reports.
* Monitor for **updates** — custom visuals receive patches for bugs and compatibility; update them regularly in Power BI Desktop.
* Do not use custom visuals that access **external URLs** unless your security team has approved them.

---

## References

* [Main sources for acquiring Power BI custom visuals – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/developer/visuals/power-bi-custom-visuals)
* [Develop custom visuals in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/developer/visuals/develop-power-bi-visuals)
* [Overview of visualizations in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualizations-overview)
