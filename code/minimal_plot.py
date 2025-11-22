import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("adr_sample.csv", parse_dates=["date"])
daily = (df.groupby("date", as_index=False)["revenue"].sum())

plt.figure(figsize=(8, 4))
plt.plot(daily["date"], daily["revenue"])
plt.title("Total Revenue by Day")
plt.xlabel("Date")
plt.ylabel("Revenue")
