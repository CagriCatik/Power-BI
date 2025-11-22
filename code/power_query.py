import pandas as pd

dataset = pd.read_csv("adr_sample.csv", parse_dates=["date"])  # test CSV

# enforce schema
df["date"] = pd.to_datetime(df["date"])
for c in ["adr", "rooms_sold", "revenue"]:
    df[c] = pd.to_numeric(df[c], errors="coerce")

# example transforms
df["adr_bucket"] = pd.cut(df["adr"], bins=[0, 80, 120, float("inf")], labels=["low", "mid", "high"])

# group and return
result = (df.groupby(["hotel_id", "adr_bucket"], as_index=False)
            .agg(n_days=("date", "nunique"),
                 avg_adr=("adr", "mean"),
                 revenue=("revenue", "sum")))
