import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("adr_sample.csv", parse_dates=["date"])  # test CSV

plt.figure(figsize=(6, 4))
for h, g in dataset.groupby("hotel_id"):
    plt.scatter(g["rooms_sold"], g["adr"], label=h, alpha=0.6)

plt.title("ADR vs Rooms Sold")
plt.xlabel("Rooms Sold")
plt.ylabel("ADR")
plt.legend()
plt.show()
