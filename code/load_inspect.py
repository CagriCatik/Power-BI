"""
Python-only ADR tutorial script (well-commented, warning-safe).

Run:
  python load_inspect.py

Prereqs:
  - adr_sample.csv in the same folder
  - pandas, numpy, matplotlib installed

Notes:
  - Uses .loc and .assign to avoid SettingWithCopyWarning.
  - Keeps each step explicit and composable.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# -----------------------------------------------------------------------------
# 0) Load
# -----------------------------------------------------------------------------
# Parse "date" as datetime on read to avoid later conversions.
CSV_PATH = Path("adr_sample.csv")
if not CSV_PATH.exists():
    raise FileNotFoundError(f"CSV not found: {CSV_PATH.resolve()}")

dataset = pd.read_csv(CSV_PATH, parse_dates=["date"])


# -----------------------------------------------------------------------------
# 1) Schema verification and basic hygiene
# -----------------------------------------------------------------------------
# Print schema to stdout for a quick check.
print("\n[INFO] Dataset schema:")
dataset.info()

print("\n[INFO] Head(5):")
print(dataset.head(5))

# Ensure required columns exist before proceeding.
required = {"date", "hotel_id", "adr", "rooms_sold", "revenue"}
missing = required - set(dataset.columns)
if missing:
    raise ValueError(f"Missing required columns: {sorted(missing)}")

# Enforce numeric types where appropriate. Coerce to NaN on bad values.
for col in ["adr", "rooms_sold", "revenue"]:
    dataset[col] = pd.to_numeric(dataset[col], errors="coerce")

# Optional: basic stats including non-numeric columns.
print("\n[INFO] describe(include='all'):")
print(dataset.describe(include="all"))

# Optional defensive checks.
if dataset[["adr", "rooms_sold", "revenue"]].isna().any().any():
    # [Inference] Real-world data may have NaNs after coercion.
    # Decide how to handle them (drop, fill). Here, we will drop for simplicity.
    print("\n[WARN] NaNs detected after type coercion. Dropping rows with NaNs in numeric fields.")
    dataset = dataset.dropna(subset=["adr", "rooms_sold", "revenue"]).reset_index(drop=True)


# -----------------------------------------------------------------------------
# 2) Column normalization (purely cosmetic; useful in notebooks)
# -----------------------------------------------------------------------------
# Keep a cleaned copy with normalized column names for downstream use.
df = dataset.copy()
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
df = df[["date", "hotel_id", "adr", "rooms_sold", "revenue"]]

print("\n[INFO] Normalized head(5):")
print(df.head(5))


# -----------------------------------------------------------------------------
# 3) Filters and derived columns (warning-safe)
# -----------------------------------------------------------------------------
# High revenue subset. Use .loc or .assign to avoid SettingWithCopyWarning.
high_rev = df.loc[df["revenue"] > 5000].copy()

# Bucket ADR into 3 segments. Using .assign writes on a definite copy.
high_rev = high_rev.assign(
    adr_bucket=pd.cut(
        high_rev["adr"],
        bins=[0, 80, 120, float("inf")],
        labels=["low", "mid", "high"],
        include_lowest=True,
        right=True,
        ordered=True,
    )
)

print("\n[INFO] High revenue with ADR buckets head(5):")
print(high_rev.head(5))


# -----------------------------------------------------------------------------
# 4) GroupBy and aggregation
# -----------------------------------------------------------------------------
# Per-hotel aggregates: distinct days, mean ADR, total rooms and revenue.
by_hotel = (
    df.groupby("hotel_id", as_index=False)
      .agg(
          days=("date", "nunique"),
          avg_adr=("adr", "mean"),
          rooms=("rooms_sold", "sum"),
          revenue=("revenue", "sum"),
      )
      .sort_values("revenue", ascending=False, kind="mergesort")  # stable sort
      .reset_index(drop=True)
)

print("\n[INFO] Per-hotel aggregates:")
print(by_hotel)


# -----------------------------------------------------------------------------
# 5) Pivot and tidy forms
# -----------------------------------------------------------------------------
# Wide: ADR by date x hotel. Tidy: long format for plotting or modeling.
daily_hotel = df.pivot_table(
    index="date",
    columns="hotel_id",
    values="adr",
    aggfunc="mean",
    observed=True,
)

tidy = (
    daily_hotel
    .reset_index()
    .melt(id_vars="date", var_name="hotel_id", value_name="adr")
    .dropna(subset=["adr"])
)

print("\n[INFO] Pivot head(3):")
print(daily_hotel.head(3))
print("\n[INFO] Tidy head(3):")
print(tidy.head(3))


# -----------------------------------------------------------------------------
# 6) Daily revenue series and plot
# -----------------------------------------------------------------------------
# Aggregate to daily total revenue and plot a line chart.
daily = (
    df.sort_values("date")
      .groupby("date", as_index=False)["revenue"]
      .sum()
)

plt.figure(figsize=(8, 4))
plt.plot(daily["date"], daily["revenue"])
plt.title("Total Revenue by Day")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()


# -----------------------------------------------------------------------------
# 7) Additional examples (optional): rolling stats and categorical scatter
# -----------------------------------------------------------------------------
# 7.1 Rolling ADR (7-day) per hotel for smoother trends.
df_roll = (
    df.sort_values(["hotel_id", "date"])
      .assign(
          adr_7d=lambda x: x.groupby("hotel_id")["adr"].transform(
              lambda s: s.rolling(7, min_periods=1).mean()
          )
      )
)

# 7.2 Scatter: ADR vs Rooms Sold by hotel (static segmentation).
plt.figure(figsize=(6, 4))
for h, g in df.groupby("hotel_id", observed=True):
    plt.scatter(g["rooms_sold"], g["adr"], label=h, alpha=0.6)
plt.title("ADR vs Rooms Sold")
plt.xlabel("Rooms Sold")
plt.ylabel("ADR")
plt.legend()
plt.tight_layout()
plt.show()


# -----------------------------------------------------------------------------
# 8) Save outputs (optional)
# -----------------------------------------------------------------------------
# Save artifacts if desired.
out_dir = Path("./_artifacts")
out_dir.mkdir(exist_ok=True)

by_hotel.to_csv(out_dir / "by_hotel_summary.csv", index=False)
high_rev.to_csv(out_dir / "high_revenue_bucketed.csv", index=False)
daily_hotel.to_csv(out_dir / "daily_hotel_adr_wide.csv")
tidy.to_csv(out_dir / "daily_hotel_adr_tidy.csv", index=False)

print("\n[INFO] Artifacts written to:", out_dir.resolve())
