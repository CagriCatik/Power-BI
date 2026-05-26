# Overview of Power BI Desktop

## What is Power BI Desktop?

Power BI Desktop is the **Windows authoring tool** for building Power BI reports. It lets you connect to data sources, shape and transform data with Power Query, build a semantic model with DAX, and design interactive visuals — all before publishing to the Power BI Service for sharing.

> **Reference:** [Get started with Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-getting-started)

---

## Main Interface Areas

When you open a `.pbix` file, the Power BI Desktop window is divided into five key regions.

| Area | Location | Purpose |
| --- | --- | --- |
| **Ribbon** | Top | Commands grouped by tab (Home, Insert, Modeling, View, Help) |
| **View switcher** | Left sidebar | Toggle between Report, Data, and Model views |
| **Canvas** | Center | Where you design report pages and arrange visuals |
| **Visualizations pane** | Right | Choose visual types and map fields to them |
| **Fields pane** | Right (below Visualizations) | Browse tables and columns from your data model |

> **Reference:** [Use the ribbon in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-ribbon)

---

## The Three Views

### Report View

The default view. You build report pages here by dragging fields onto the canvas or selecting them in the Fields pane.

* Add pages with the **+** button at the bottom.
* Right-click a page tab to rename, duplicate, or hide it.
* The **Filters pane** (right) shows visual-, page-, and report-level filters.

### Data View

A tabular grid showing the data currently loaded in your model.

* Browse every table and its rows.
* Add calculated columns via the formula bar.
* Verify data types and values after a refresh.

### Model View (Relationship View)

A diagram showing all tables and the lines connecting them.

* Create, edit, or delete relationships by dragging columns between tables.
* Double-click a relationship line to adjust cardinality and cross-filter direction.
* Rearrange table cards for clarity.

> **Reference:** [Model view in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-relationship-view)

---

## The Ribbon in Detail

### Home Tab

| Group | Key Actions |
| --- | --- |
| Clipboard | Cut, Copy, Paste |
| Data | Get Data, Transform Data, Refresh |
| Queries | Edit Queries |
| Insert | New visual, Text box, Image, Buttons |
| Calculations | New measure, New column, New table |
| Share | Publish |

### Insert Tab

Add visuals, shapes, images, buttons, and bookmarks directly to the canvas.

### Modeling Tab

| Group | Key Actions |
| --- | --- |
| Calculations | New Measure, New Column, New Table |
| Relationships | Manage Relationships |
| Security | Row-Level Security |
| Q&A | Set up Q&A synonyms |

### View Tab

* Toggle **Gridlines** and **Snap to grid** for layout alignment.
* Switch between **Mobile layout** and **Desktop layout**.
* Open **Performance Analyzer** to measure visual query times.
* **Bookmarks** and **Selection pane** for layering visuals.

---

## The Visualizations Pane

The Visualizations pane has three sub-tabs:

1. **Build visual** — choose a chart type and drag fields into wells (Axis, Legend, Values, Tooltips).
2. **Format visual** — style the selected visual: colors, titles, borders, data labels.
3. **Analytics** — add reference lines, forecasts, and anomaly detection.

> **Reference:** [Tour the Power BI Report Editor – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/service-the-report-editor-take-a-tour)

---

## The Fields Pane

* Lists all tables and columns currently in the model.
* A **sigma (Σ)** icon denotes a numeric column that will auto-aggregate.
* A **calculator** icon marks a DAX measure.
* A **calendar** icon marks a date/time column.
* Expand a table to see its columns; drag any column onto the canvas.

---

## Power Query Editor

Open it via **Home › Transform data**. This is where you clean, reshape, and combine data before it loads into the model.

* **Applied Steps** panel (right) records every transformation as an M code step.
* **Query Settings** lets you rename queries.
* All changes happen in-memory and are applied when you click **Close & Apply**.

> **Reference:** [Query Overview in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-query-overview)

---

## Status Bar

At the bottom of the window the status bar shows:

* Number of rows returned by the last query.
* Current page name.
* Cross-report drill-through indicator.
* Language locale.

---

## Keyboard Shortcuts (Most Used)

| Shortcut | Action |
| --- | --- |
| `Ctrl + S` | Save |
| `Ctrl + Z` | Undo |
| `Ctrl + Shift + Z` | Redo |
| `Alt + F4` | Close Desktop |
| `Ctrl + M` | Open Power Query Editor |
| `F5` | Refresh all data |
| `Tab` | Move focus between visuals |
| `Esc` | Exit edit mode |

---

## References

* [Get started with Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-getting-started)
* [Use the ribbon in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-ribbon)
* [Tour the Report Editor – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/service-the-report-editor-take-a-tour)
* [Report View in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-format-pane)
* [Query Overview in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-query-overview)
* [Model view in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-relationship-view)
