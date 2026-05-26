# Using Themes in Power BI

## Overview

**Themes** in Power BI allow you to apply a consistent set of colors, fonts, and formatting defaults across an entire report in a single action. A theme defines the palette, text styles, visual backgrounds, and structural defaults so that every visual you add automatically matches your organization's branding — without having to format each visual manually.

> **Reference:** [Use report themes in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-report-themes)

---

## Built-in Themes

Power BI Desktop ships with a library of built-in themes:

1. In Power BI Desktop, go to the **View** ribbon tab.
2. In the **Themes** group, open the theme gallery dropdown.
3. Hover over any theme to preview it on the canvas.
4. Click a theme to apply it immediately.

All built-in themes are professionally designed and cover a range of color palettes from neutral corporate to high-contrast accessibility themes.

---

## Customizing a Theme

You can adjust a built-in theme or build one from scratch via the **Customize current theme** dialog:

1. On the **View** tab → **Themes** → **Customize current theme**.
2. The dialog has four sections:

### Name and Colors

* Set the theme **Name**.
* Define up to **eight theme colors** — these drive all default data colors in charts.
* Set **Sentiment colors**: Good (green), Neutral (yellow), Bad (red) — used by KPI visuals.
* Set **Divergent colors** for heatmaps and conditional formatting gradients.

### Text

* Set default font families, sizes, and colors for **Title**, **Header**, **Label**, and **Callout** text classes.
* These classes map to specific text elements across visuals — for example, **Label** drives axis tick labels.

### Visuals

* Set default **Background**, **Border**, **Shadow**, and **Header** settings for all visuals.
* These apply as defaults — individual visuals can override them in the Format pane.

### Page and Filter Pane

* Set the **report page background** color and image.
* Set the **filter pane** background, font color, and icon color.

1. Click **Apply** to apply the customized theme.

---

## Exporting a Theme

After customizing, export the theme as a `.json` file for reuse:

1. **View** → **Themes** → **Save current theme**.
2. Choose a location and file name.
3. The theme is saved as a JSON file that can be shared with colleagues or stored in version control.

---

## Importing a Theme File

To apply a saved or externally sourced theme:

1. **View** → **Themes** → **Browse for themes**.
2. Select the `.json` theme file.
3. Click **Open** — the theme applies immediately.

This is the recommended workflow for distributing a corporate theme — your Power BI Center of Excellence creates and exports the file once, then all report authors import it.

---

## Theme JSON Structure

A Power BI theme file is a JSON document. A minimal example:

```json
{
  "name": "Corporate Blue",
  "dataColors": [
    "#003087", "#005EB8", "#0072CE",
    "#41B6E6", "#00B5E2", "#00A499",
    "#78BE20", "#FFB81C"
  ],
  "background": "#FFFFFF",
  "foreground": "#003087",
  "tableAccent": "#005EB8",
  "visualStyles": {
    "*": {
      "*": {
        "fontFamily": [{ "value": "Segoe UI" }]
      }
    }
  }
}
```

The `visualStyles` section allows granular control over individual visual types and their specific formatting properties — overriding defaults for every instance of that visual type across the report.

> **Reference:** [Power BI report theme JSON format reference – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-report-themes#report-theme-json-file-format)

---

## Applying Themes in Power BI Service

In the Power BI Service report editor:

1. Open a report in **Edit mode**.
2. Click the **Format** menu in the top bar → **Theme**.
3. Select a built-in theme or upload a `.json` file.

Note: Theme changes made in the Service are saved with the report but are separate from the Desktop file until the report is re-published.

---

## Theme Precedence and Overrides

| Level | Scope | Overrides |
| --- | --- | --- |
| Theme default | All visuals in report | None — lowest priority |
| Visual-level format | Single visual | Overrides theme for that visual |
| Conditional formatting | Individual data points | Overrides visual format |

When you manually format a visual (e.g., change a bar color), that override persists even after applying a new theme. To reset a visual to theme defaults, click **Revert to default** in the Format pane for that property.

---

## Best Practices

* Define a **corporate theme JSON** once and distribute it — avoids inconsistent branding across reports.
* Limit the theme to **8 data colors** — more than 8 categories on the same chart is usually a sign the visual needs redesign.
* Test your theme against **all visual types** used in your reports — colors that work on bar charts may not work on maps or scatter plots.
* Store theme `.json` files in a **shared repository** (e.g., SharePoint, GitHub) with versioning.
* Use the **accessibility theme** options (high contrast) when building reports for diverse audiences.

---

## References

* [Use report themes in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-report-themes)
* [Power BI report theme JSON format reference – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-report-themes#report-theme-json-file-format)
* [Customize current theme – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-report-themes#customize-report-themes)
