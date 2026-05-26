# Options and Settings in Power BI Desktop

## Overview

Power BI Desktop ships with a wide range of configuration knobs that let you adapt the tool to your workflow, your organization's policies, and experimental features you want to try. All of them live under **File › Options and settings** — either in the global **Options** dialog or in **Data source settings**.

> **Reference:** [Enabling Preview Features in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/archive/blogs/samlester/enabling-preview-features-in-power-bi-desktop)

---

## Navigating to Options

1. Open Power BI Desktop.
2. Click **File** in the top-left corner.
3. Select **Options and settings**.
4. Choose **Options**.

The Options dialog is split into two groups:

| Group | Scope |
| --- | --- |
| **GLOBAL** | Applies to every Power BI Desktop file you open |
| **CURRENT FILE** | Applies only to the `.pbix` you have open right now |

---

## Key Settings Categories

### Data Load

Located under **GLOBAL › Data Load**.

| Setting | Default | Effect |
| --- | --- | --- |
| Import relationships from data sources on first load | On | Auto-detects FK–PK relationships |
| Update or delete relationships when refreshing data | On | Keeps the model in sync with source changes |
| Autodetect new relationships after data is loaded | On | Runs relationship detection after each load |
| Background data | Off | Allows data preview to download in the background while you continue working |
| Time intelligence | Auto | Controls how auto date/time hierarchies are generated |

> To allow data preview to download in the background, select **File › Options and settings › Options › Data Load**, and turn on *Allow data preview to download in the background*.

---

### Query Editor

Controls the behavior of Power Query Editor.

* **Display the Query Editor in a separate window** — opens the editor as its own application window.
* **Enable/Disable parallel query loading** — runs multiple queries simultaneously for faster refresh.
* **Formula bar** — shows or hides the M formula bar.

---

### Preview Features

New capabilities shipped in preview so users can provide feedback before general availability.

**How to enable:**

1. Go to **File › Options and settings › Options**.
2. Under **GLOBAL**, select **Preview features**.
3. Tick the feature checkbox.
4. Click **OK** and **restart Power BI Desktop** when prompted.

Common preview features include:

| Feature | Description |
| --- | --- |
| Visual calculations | Perform calculations directly inside a visual |
| New Power Query experience | Updated M editor UI |
| Power BI Project (PBIP) save option | Save reports as open folder format |
| Shape map visual | Choropleth maps for custom regions |
| On-object interaction | Click to format visuals inline |

> **Reference:** [Use on-object interaction with visuals (preview) – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-on-object-interaction)

---

### Security

Controls trusted locations, certificate handling, and web-content rendering:

* **Use a secure connection (HTTPS)** — forces encrypted connections to web data sources.
* **Certification Revocation** — validates SSL certificates from data sources.
* **Custom Visuals** — decides whether unverified AppSource visuals can load.

---

### Privacy

Sets the Privacy Level used when combining data from multiple sources. Power Query uses privacy levels to prevent accidental data leakage across organizational boundaries.

| Level | Behavior |
| --- | --- |
| Public | Data can be combined freely |
| Organizational | Combines only with other organizational sources |
| Private | Never combined automatically |

---

### Regional Settings

Controls **locale** used when interpreting data types (dates, numbers, currencies). Setting the locale to match your data source avoids misdetected column types during import.

---

### CURRENT FILE — Report Settings

| Setting | What It Does |
| --- | --- |
| Persistent filters | Saves user slicer/filter state between sessions |
| Cross-report drill-through | Enables users to drill from one report to another |
| Spotlight | Allows users to spotlight a visual (dims others) |

---

### CURRENT FILE — Data Load

* **Evaluation configuration** — controls whether Power BI evaluates DirectQuery in the canvas or submits queries on demand.
* **Calculation groups** — enables creation of calculation groups in the Tabular model.

> **Reference:** [Evaluation configuration settings for Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-evaluation-configuration)

---

## Data Source Settings

Accessed via **File › Options and settings › Data source settings**.

* Lists every data source the current file (or globally) connects to.
* Allows you to **edit credentials**, change authentication methods, or **clear cached permissions**.
* Use this when you need to reconnect to a renamed server or rotate an API key.

---

## Best Practices

1. **Enable background data preview** — speeds up the Query Editor experience.
2. **Set Privacy Levels explicitly** — prevents unexpected errors when combining public and private data.
3. **Enable only the preview features you need** — preview features may change between updates.
4. **Match locale to source** — avoid type-mismatch errors on international datasets.
5. **Keep autodetect relationships on** — saves model-building time and catches obvious relationships automatically.

---

## References

* [Data sources in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-data-sources)
* [Evaluation configuration settings – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-evaluation-configuration)
* [Enabling Preview Features – Microsoft Learn](https://learn.microsoft.com/en-us/archive/blogs/samlester/enabling-preview-features-in-power-bi-desktop)
* [Power BI Desktop projects (PBIP) – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview)
