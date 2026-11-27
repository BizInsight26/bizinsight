from pathlib import Path

from src.preprocessing.data_loader import load_data
from src.analysis.business_analysis import (
    prepare_business_data,
    calculate_business_kpis
)

project_dir = Path(__file__).resolve().parent.parent

file_path = (
    project_dir / "data" / "recent_retail"
    / "retail_sales_ml_apl.csv"
)

# Test data loading
df = load_data(file_path)

print("Data loaded successfully.")
print("Records:", len(df))

# Test validation and preprocessing
business_df = prepare_business_data(df)

print("\nData preparation successful.")
print("Prepared records:", len(business_df))

# Test financial KPIs
kpis = calculate_business_kpis(business_df)

print("\nBusiness KPIs:")

for name, value in kpis.items():
    if value is not None:
        print(f"{name}: {value:,.2f}")
    else:
        print(f"{name}: N/A")





from src.analysis.business_analysis import (
    analyze_monthly_performance,
    analyze_product_performance
)

monthly = analyze_monthly_performance(business_df)

print("\nMonthly Performance:")
print(monthly.to_string(index=False))

products = analyze_product_performance(business_df)

print("\nProduct Performance:")
print(products.head(10).to_string(index=False))

print("\nTotal products analyzed:", len(products))



from src.analysis.business_analysis import (
    detect_popular_low_margin,
    detect_hidden_high_margin,
    detect_loss_making_products
)

popular_low_margin = detect_popular_low_margin(products)
hidden_high_margin = detect_hidden_high_margin(products)
loss_making = detect_loss_making_products(products)

print("\nPopular but Low Margin:")
print(popular_low_margin.head().to_string(index=False))
print("Total:", len(popular_low_margin))

print("\nHidden High Margin:")
print(hidden_high_margin.head().to_string(index=False))
print("Total:", len(hidden_high_margin))

print("\nLoss-Making Products:")
print(loss_making.head().to_string(index=False))
print("Total:", len(loss_making))


import pandas as pd

comparisons = {
    "popular_low_margin": popular_low_margin,
    "hidden_high_margin": hidden_high_margin,
    "loss_making_products": loss_making
}

for name, current in comparisons.items():

    original = pd.read_csv(
        project_dir / "results" / "business_analysis"
        / f"{name}.csv"
    )

    assert set(original["ProductID"]) == set(current["ProductID"]), (
        f"{name}: Product IDs do not match"
    )

    print(f"{name}: PASS")





from src.analysis.business_analysis import (
    analyze_store_performance
)

stores = analyze_store_performance(business_df)

print("\nTop 5 Stores:")
print(stores.head(5).round(2).to_string(index=False))

print("\nBottom 5 Stores:")
print(stores.tail(5).round(2).to_string(index=False))

print("\nTotal stores:", len(stores))

print(
    "Median daily profit:",
    round(stores["AverageDailyProfit"].median(), 2)
)




from src.analysis.business_analysis import (
    analyze_promotion_performance
)

promotions = analyze_promotion_performance(business_df)

print("\nPromotion Performance:")
print(promotions.round(2).to_string(index=False))


from src.analysis.business_analysis import (
    analyze_product_returns,
    detect_high_return_products
)

return_analysis = analyze_product_returns(business_df)

high_returns = detect_high_return_products(return_analysis)

print("\nProduct Return Analysis:")
print(return_analysis.head().round(2).to_string(index=False))

print("\nHigh Return Products:")
print(high_returns.head().round(2).to_string(index=False))

print("Total high return products:", len(high_returns))

original_returns = pd.read_csv(
    project_dir / "results" / "business_analysis"
    / "high_return_products.csv"
)

assert set(original_returns["ProductID"]) == set(
    high_returns["ProductID"]
), "High return product IDs do not match"

print("high_return_products: PASS")



from src.analysis.business_analysis import (
    analyze_daily_performance,
    detect_sales_anomalies
)

daily = analyze_daily_performance(business_df)

sales_anomalies = detect_sales_anomalies(daily)

print("\nDaily Performance:")
print(daily.tail().round(2).to_string(index=False))

print("\nSales Anomalies:")
print(sales_anomalies.head().round(2).to_string(index=False))

print("Total sales anomalies:", len(sales_anomalies))

original_anomalies = pd.read_csv(
    project_dir / "results" / "business_analysis"
    / "sales_anomalies.csv",
    parse_dates=["Date"]
)

assert len(original_anomalies) == len(sales_anomalies)

assert set(zip(
    original_anomalies["Date"],
    original_anomalies["AnomalyType"]
)) == set(zip(
    sales_anomalies["Date"],
    sales_anomalies["AnomalyType"]
)), "Sales anomalies do not match"

print("sales_anomalies: PASS")