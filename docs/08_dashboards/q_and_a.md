# Q&A — Natural Language Queries

## Overview

**Power BI Q&A** lets users ask questions about their data in plain language and receive instant visual answers. Type "total sales by region last quarter" and Power BI generates a chart automatically. Q&A is available on dashboards and as a dedicated visual in reports.

> **Reference:** [Explore and create visuals using Power BI Q&A – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/natural-language/power-bi-tutorial-q-and-a)
> **Reference:** [Q&A for Power BI business users – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/consumer/end-user-q-and-a)

---

## Where Q&A Is Available

| Location | How to access |
| --- | --- |
| **Dashboard** | Click "Ask a question about your data" at the top |
| **Report (Q&A visual)** | Add the Q&A visual from the Visualizations pane |
| **Power BI Mobile** | Tap the microphone icon and speak a question |

---

## Using Q&A on a Dashboard

1. Open a dashboard in the Power BI Service.
2. Click the **Ask a question about your data** box at the top.
3. Type a natural language question (e.g., "What are total sales by product category?").
4. Power BI interprets the question and shows a visual.
5. Refine the question by modifying the text until the visual answers your question.
6. Click the **pin icon** to save the result as a dashboard tile.

---

## Using the Q&A Visual in a Report

1. In Power BI Desktop, click the **Q&A** visual icon in the Visualizations pane.
2. Place it on the report canvas.
3. The visual shows a question input box.
4. In **edit mode**, you can pre-populate a question or configure suggested questions.
5. Report consumers type their own questions when viewing the report.

---

## Writing Effective Q&A Questions

Q&A understands natural language but works best with specific phrasing:

| Good question | What it does |
| --- | --- |
| `total sales by region` | Column chart of sales per region |
| `sales last year as a line chart` | Line chart of annual sales |
| `top 10 products by revenue` | Bar chart, top 10 products |
| `average order value by month this year` | Line chart for current year |
| `count of customers where region is North` | Card showing a single count |

Use field names from your data model for best results — Q&A learns synonyms from your model's column and table names.

---

## Q&A Setup and Synonyms

To improve Q&A accuracy, define synonyms for field and table names:

1. In the Power BI Service, go to the workspace containing the semantic model.
2. Click the ellipsis **(…)** next to the semantic model → **Settings › Q&A**.
3. Under **Q&A field synonyms**, add alternative names (e.g., "revenue" as a synonym for "SalesAmount").

In Power BI Desktop:

1. Go to the **Modeling** tab → **Q&A Setup**.
2. Review suggested synonyms and approve or add new ones.

---

## Configuring Suggested Questions

For the Q&A visual in a report, you can pre-define example questions consumers can click:

1. Select the Q&A visual.
2. Under **Format visual › Q&A setup**, add suggested question strings.
3. These appear as clickable chips below the input box when the visual is empty.

---

## Converting Q&A to a Standard Visual

Once a Q&A visual shows a satisfying result:

1. Click the **Turn this Q&A result into a standard visual** icon (chart icon) in the Q&A visual toolbar.
2. The visual converts to a regular Power BI visual (bar chart, card, etc.) that can be fully formatted.

This is a useful workflow for rapidly prototyping a visual by typing a question, then converting it to a proper formatted chart.

---

## Limitations

* Q&A requires the semantic model to have clear, well-named columns and tables.
* It works best with **Import mode** models — DirectQuery models may have slower Q&A response times.
* Q&A does not support all visual types — complex visuals (maps, custom visuals) may not be generated.
* Q&A experiences in dashboards are scheduled to retire in **December 2026** — Microsoft recommends Copilot for Power BI as the successor.

> **Reference:** [Learn how to use natural language to explore data with Power BI Q&A – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/natural-language/q-and-a-intro)

---

## Best Practices

* Name columns and tables clearly in the semantic model — Q&A parses these names to interpret questions.
* Add **synonyms** for domain-specific terms that your consumers commonly use.
* Pre-populate **suggested questions** in the Q&A visual to guide less experienced users.
* Use Q&A for **ad-hoc exploration** pages, not primary dashboards — for defined KPIs, build standard visuals.

---

## References

* [Explore and create visuals using Power BI Q&A – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/natural-language/power-bi-tutorial-q-and-a)
* [Create a Q&A Visual in a Report – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-q-and-a)
* [Q&A for Power BI business users – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/consumer/end-user-q-and-a)
* [Q&A tutorial for Power BI dashboards – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/natural-language/end-user-q-and-a-tutorial)
