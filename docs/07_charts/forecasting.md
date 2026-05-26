# Trends and Forecasting

## Overview

Power BI's **Analytics pane** includes a built-in forecasting engine for line charts. It projects future values based on historical patterns using exponential smoothing, and can display confidence intervals to communicate the uncertainty of the prediction.

> **Reference:** [Use the Analytics pane in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-analytics-pane)

---

## Requirements for Forecasting

Before adding a forecast, the line chart must meet these conditions:

* **Single series** — only one measure in the Values well (no Legend field splitting into multiple lines).
* **Continuous X-axis** — a date or numeric column set to continuous type (not categorical).
* **Sufficient data** — at least a few dozen data points for a meaningful forecast.

---

## Adding a Forecast

1. Select the line chart.
2. Open the **Analytics** tab (magnifying glass icon) in the Visualizations pane.
3. Expand **Forecast**.
4. Click **Add**.
5. Configure:

| Setting | Description |
| --- | --- |
| **Forecast length** | How many future periods to project (e.g., 6 months) |
| **Ignore last** | Exclude the most recent N periods from model fitting (useful when recent data is incomplete) |
| **Confidence interval** | Percentage confidence band shown around the forecast (e.g., 95%) |
| **Seasonality** | Auto-detect or set manually (e.g., 12 for monthly data with annual seasonality) |
| **Color** | Line color for the forecast projection |

1. Click **Apply**.

The chart now extends into future time periods with a projected line and a shaded confidence band.

---

## Confidence Intervals

The shaded band around the forecast represents the range within which the actual future value is expected to fall with the specified confidence level:

* **95% confidence interval** — the true value is expected to fall within the band 95% of the time.
* A wider band means less certainty (more volatile historical data or fewer data points).
* A narrower band indicates more stable, predictable data.

To show or hide the confidence interval, toggle **Confidence interval** on or off in the Forecast settings.

---

## Seasonality Settings

| Setting | When to use |
| --- | --- |
| **Auto-detect** | Let Power BI determine the seasonal cycle |
| **Custom (N points)** | Set manually — e.g., 12 for monthly data with annual seasonality, 7 for daily with weekly patterns |
| **None** | No seasonal adjustment |

Setting seasonality correctly is the most important tuning parameter. If your monthly revenue has clear holiday peaks every December, set seasonality to 12.

---

## Forecast Limitations

* Forecasting is **not available** when a **Legend** field is set (removes multi-series requirement).
* Forecasting is **not available** on categorical X-axes — switch to continuous under **Format visual › X-axis › Type = Continuous**.
* The forecast uses **exponential smoothing** — it does not incorporate external variables (causal forecasting requires DAX or Python/R integration).
* Forecasts are for **exploration and communication**, not certified predictions for financial planning.

---

## Trend Line vs Forecast

| Feature | Trend line | Forecast |
| --- | --- | --- |
| Shows | Direction of existing data | Projected future values |
| Extends beyond data | No | Yes |
| Confidence band | No | Yes (optional) |
| Seasonality support | No | Yes |
| Requires single series | Yes | Yes |

Use a **trend line** when communicating the direction of historical data. Use a **forecast** when projecting into the future.

---

## Practical Example

A line chart shows monthly website sessions for the past 24 months. Adding a forecast:

1. Seasonality: 12 (annual pattern — traffic spikes every summer).
2. Forecast length: 6 months (project the next half year).
3. Confidence interval: 95%.

The chart extends 6 months past the last data point with a shaded band. Leadership can see whether the projected trend is positive, negative, or flat — and how much uncertainty exists.

---

## Best Practices

* Set seasonality **manually** when you know the data's seasonal cycle — auto-detect can be unreliable with short time series.
* Use **Ignore last** when the most recent period is incomplete (e.g., the current month only has 2 weeks of data and skews the fit).
* Label the forecast line clearly so consumers do not mistake projected values for actuals.
* Pair the forecast with **reference lines** (e.g., target line) so viewers can see whether the projection reaches the goal.
* Always state the forecast model's limitations in report documentation.

---

## References

* [Use the Analytics pane in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-analytics-pane)
* [Line Charts in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-line-chart)
* [Time intelligence functions (DAX) – Microsoft Learn](https://learn.microsoft.com/en-us/dax/time-intelligence-functions-dax)
