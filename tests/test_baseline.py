
# BizInsight - Week 2 Baseline Tests

import pandas as pd


def validate_data(df):
    required = ["Store", "Date", "Sales", "Customers", "Open"]

    if df[required].isna().any().any():
        raise ValueError("Dataset contains missing values")

    if df.duplicated(subset=["Store", "Date"]).any():
        raise ValueError("Duplicate store/date records found")

    if (df["Sales"] < 0).any():
        raise ValueError("Sales cannot be negative")

    if (~df["Open"].isin([0, 1])).any():
        raise ValueError("Open must be 0 or 1")


def predict_sales(df):
    validate_data(df)

    valid = df[df["Open"] == 1]

    return valid.groupby("Store")["Sales"].mean()


def make_data(sales, open_values=None):
    if open_values is None:
        open_values = [1] * len(sales)

    return pd.DataFrame({
        "Store": [1] * len(sales),
        "Date": pd.date_range("2026-11-01", periods=len(sales)),
        "Sales": sales,
        "Customers": [10] * len(sales),
        "Open": open_values
    })


# Test 1: Normal case
data = make_data([100, 200, 300])
result = predict_sales(data)[1]
assert result == 200
print("Test 1 - Normal data: PASS")


# Test 2: Missing data
data = make_data([100, None, 300])

try:
    predict_sales(data)
    print("Test 2 - Missing data: FAIL")
except ValueError:
    print("Test 2 - Missing data: PASS")


# Test 3: Duplicate data
data = make_data([100, 200, 300])
data = pd.concat([data, data.iloc[[0]]], ignore_index=True)

try:
    predict_sales(data)
    print("Test 3 - Duplicate data: FAIL")
except ValueError:
    print("Test 3 - Duplicate data: PASS")


# Test 4: Closed store / zero sales
data = make_data(
    [100, 0, 300],
    [1, 0, 1]
)

result = predict_sales(data)[1]
assert result == 200
print("Test 4 - Closed store: PASS")
