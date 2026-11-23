
# BizInsight - Week 2: Non-AI Sales Baseline

from pathlib import Path
import pandas as pd

# Find the dataset
project_root = Path(__file__).resolve().parents[1]
data_path = project_root / "data" / "synthetic_sales.csv"

# Load synthetic sales data
df = pd.read_csv(data_path)
df["Date"] = pd.to_datetime(df["Date"])

# Basic validation
required = ["Store", "Date", "Sales", "Customers", "Open"]

if df[required].isna().any().any():
    raise ValueError("Dataset contains missing values")

if df.duplicated(subset=["Store", "Date"]).any():
    raise ValueError("Duplicate store/date records found")

if (df["Sales"] < 0).any():
    raise ValueError("Sales cannot be negative")

if (~df["Open"].isin([0, 1])).any():
    raise ValueError("Open must be 0 or 1")

# Only use valid, open-store records
valid_sales = df[
    (df["Open"] == 1) &
    (df["Sales"] >= 0)
].copy()

# Calculate average sales per store
store_averages = valid_sales.groupby("Store")["Sales"].mean()

# Display predictions
print("BizInsight - Non-AI Baseline")
print("----------------------------")

for store, average in store_averages.items():
    print(f"Store {store}: Predicted next-day sales = {average:.2f}")

print("\nBaseline completed successfully!")
