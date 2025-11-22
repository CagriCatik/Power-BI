import pandas as pd

df = pd.read_csv("adr_sample.csv", parse_dates=["date"])
df["adr"] = pd.to_numeric(df["adr"], errors="coerce")
df["rooms_sold"] = pd.to_numeric(df["rooms_sold"], errors="coerce")
df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")

summary = (
    df.groupby("hotel_id", as_index=False)
      .agg(days=("date", "nunique"),
           avg_adr=("adr", "mean"),
           total_rev=("revenue", "sum"))
      .sort_values("total_rev", ascending=False)
)
print(summary)
