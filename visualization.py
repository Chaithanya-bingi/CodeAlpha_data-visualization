import pandas as pd
import matplotlib.pyplot as plt
import os

# Load cleaned dataset
df = pd.read_csv("data/processed/cleaned_dataset.csv")

# Create visualizations folder if it doesn't exist
os.makedirs("visualizations", exist_ok=True)

# ---- Chart 1: Sales by Category ----
sales_by_category = df.groupby("Category")["Sales"].sum()

sales_by_category.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.savefig("visualizations/sales_by_category.png")
plt.close()

# ---- Chart 2: Profit by Region ----
profit_by_region = df.groupby("Region")["Profit"].sum()

profit_by_region.plot(kind="bar")
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")

plt.savefig("visualizations/profit_by_region.png")
plt.close()

# ---- Chart 3: Sales by Segment ----
sales_by_segment = df.groupby("Segment")["Sales"].sum()

sales_by_segment.plot(kind="bar")
plt.title("Sales by Segment")
plt.xlabel("Segment")
plt.ylabel("Total Sales")

plt.savefig("visualizations/sales_by_segment.png")
plt.close()

print("Charts saved successfully in the visualizations folder.")