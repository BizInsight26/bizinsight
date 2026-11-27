import pandas as pd
import numpy as np

from src.preprocessing.data_validator import (
    validate_data,
    preprocess_data
)


def prepare_business_data(df):

    df = df.copy()

    df = df.rename(columns={
        "Transaction Date": "Date",
        "Sales Type": "SalesType",
        "Is Return": "IsReturn",
        "Product No": "ProductID",
        "Product Description": "ProductName",
        "Product Division": "Division",
        "Product Category": "Category",
        "Product Subcategory": "Subcategory",
        "Product Segment": "Segment",
        "Sales Channel": "SalesChannel",
        "Qty Sold": "QuantitySold",
        "Sales Amount": "Sales",
        "Cogs": "COGS",
        "Number of Transactions": "Transactions"
    })

    required_columns = [
        "Date",
        "Store",
        "ProductID",
        "Sales",
        "COGS",
        "QuantitySold",
        "IsReturn",
        "SalesType"
    ]

    df = validate_data(df, required_columns)
    df = preprocess_data(df)

    if df[required_columns].isna().any().any():
        raise ValueError("Required fields contain missing values.")

    numeric_columns = [
        "Sales", "COGS", "QuantitySold", "IsReturn"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column], errors="coerce"
        )

    if not np.isfinite(df[numeric_columns].to_numpy()).all():
        raise ValueError("Invalid numerical values detected.")

    if not df["IsReturn"].isin([0, 1]).all():
        raise ValueError("Invalid return indicator.")

    financial_columns = ["Sales", "COGS", "QuantitySold"]

    if (df.loc[df["IsReturn"] == 1, financial_columns] > 0).any().any():
        raise ValueError("Return records contain positive values.")

    if (df.loc[df["IsReturn"] == 0, financial_columns] < 0).any().any():
        raise ValueError("Purchase records contain negative values.")

    df["GrossProfit"] = df["Sales"] - df["COGS"]

    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month

    df["YearMonth"] = (
        df["Date"].dt.to_period("M").astype(str)
    )

    df["DayOfWeek"] = df["Date"].dt.day_name()

    return df


def calculate_business_kpis(df):

    purchases = df[df["IsReturn"] == 0]
    returns = df[df["IsReturn"] == 1]

    gross_sales = purchases["Sales"].sum()
    return_value = abs(returns["Sales"].sum())

    net_sales = df["Sales"].sum()
    total_cogs = df["COGS"].sum()
    gross_profit = df["GrossProfit"].sum()

    units_sold = purchases["QuantitySold"].sum()
    units_returned = abs(returns["QuantitySold"].sum())

    return {
        "GrossSales": gross_sales,
        "TotalReturnsValue": return_value,
        "NetSales": net_sales,
        "NetCOGS": total_cogs,
        "GrossProfit": gross_profit,
        "GrossMargin": (
            gross_profit / net_sales * 100
            if net_sales > 0 else None
        ),
        "UnitsSold": units_sold,
        "UnitsReturned": units_returned,
        "NetUnitsSold": units_sold - units_returned,
        "ReturnRate": (
            units_returned / units_sold * 100
            if units_sold > 0 else None
        ),
        "UniqueProducts": df["ProductID"].nunique(),
        "TotalStores": df["Store"].nunique(),
        "TotalSuppliers": (
            df["Supplier"].nunique()
            if "Supplier" in df.columns else None
        )
    }



def analyze_monthly_performance(df):

    monthly = df.groupby("YearMonth").agg(
        NetSales=("Sales", "sum"),
        COGS=("COGS", "sum"),
        GrossProfit=("GrossProfit", "sum"),
        NetUnitsSold=("QuantitySold", "sum"),
        DaysRecorded=("Date", "nunique")
    ).reset_index()

    monthly = monthly.rename(
        columns={"YearMonth": "Month"}
    )

    monthly["GrossMargin"] = np.where(
        monthly["NetSales"] > 0,
        monthly["GrossProfit"] / monthly["NetSales"] * 100,
        np.nan
    )

    monthly["CompleteMonth"] = (
        monthly["DaysRecorded"] ==
        pd.to_datetime(monthly["Month"]).dt.days_in_month
    )

    monthly["SalesGrowth"] = (
        monthly["NetSales"].pct_change() * 100
    )

    monthly["ProfitGrowth"] = (
        monthly["GrossProfit"].pct_change() * 100
    )

    comparable = (
        monthly["CompleteMonth"] &
        monthly["CompleteMonth"].shift(fill_value=False) &
        pd.to_datetime(monthly["Month"]).dt.to_period("M")
        .diff().apply(lambda x: getattr(x, "n", None) == 1)
    )

    monthly.loc[
        ~comparable, ["SalesGrowth", "ProfitGrowth"]
    ] = np.nan

    monthly.loc[
        monthly["NetSales"].shift() <= 0, "SalesGrowth"
    ] = np.nan

    monthly.loc[
        monthly["GrossProfit"].shift() <= 0, "ProfitGrowth"
    ] = np.nan

    return monthly.round(2)


def analyze_product_performance(df):

    products = df.groupby("ProductID").agg(
        NetSales=("Sales", "sum"),
        COGS=("COGS", "sum"),
        GrossProfit=("GrossProfit", "sum"),
        NetUnitsSold=("QuantitySold", "sum"),
        Records=("ProductID", "size")
    ).reset_index()

    products["GrossMargin"] = np.where(
        products["NetSales"] > 0,
        products["GrossProfit"] / products["NetSales"] * 100,
        np.nan
    )

    products = products.sort_values(
        "NetSales", ascending=False
    )
    return products.reset_index(drop=True)



def detect_popular_low_margin(products):

    eligible = products[
        (products["NetSales"] > 0) &
        (products["NetUnitsSold"] > 0) &
        (products["Records"] >= 10)
    ].copy()

    high_volume = eligible["NetUnitsSold"].quantile(0.75)
    low_margin = eligible["GrossMargin"].quantile(0.25)

    opportunities = eligible[
        (eligible["NetUnitsSold"] >= high_volume) &
        (eligible["GrossMargin"] <= low_margin)
    ]

    return opportunities.sort_values(
        "NetUnitsSold", ascending=False
    ).reset_index(drop=True)


def detect_hidden_high_margin(products):

    eligible = products[
        (products["NetSales"] > 0) &
        (products["NetUnitsSold"] > 0) &
        (products["Records"] >= 10)
    ].copy()

    low_volume = eligible["NetUnitsSold"].quantile(0.25)
    high_margin = eligible["GrossMargin"].quantile(0.75)

    opportunities = eligible[
        (eligible["NetUnitsSold"] <= low_volume) &
        (eligible["GrossMargin"] >= high_margin)
    ]

    return opportunities.sort_values(
        "GrossMargin", ascending=False
    ).reset_index(drop=True)



def detect_loss_making_products(products):

    opportunities = products[
        products["GrossProfit"] < 0
    ]

    return opportunities.sort_values(
        "GrossProfit", ascending=True
    ).reset_index(drop=True)



def analyze_store_performance(df):

    stores = df.groupby("Store").agg(
        NetSales=("Sales", "sum"),
        COGS=("COGS", "sum"),
        GrossProfit=("GrossProfit", "sum"),
        NetUnitsSold=("QuantitySold", "sum"),
        ActiveDays=("Date", "nunique")
    ).reset_index()

    stores["GrossMargin"] = np.where(
        stores["NetSales"] > 0,
        stores["GrossProfit"] / stores["NetSales"] * 100,
        np.nan
    )

    stores["AverageDailySales"] = (
        stores["NetSales"] / stores["ActiveDays"]
    )

    stores["AverageDailyProfit"] = (
        stores["GrossProfit"] / stores["ActiveDays"]
    )

    return stores.sort_values(
        "AverageDailyProfit", ascending=False
    ).reset_index(drop=True)



def analyze_promotion_performance(df):

    promotions = df.groupby("SalesType").agg(
        NetSales=("Sales", "sum"),
        COGS=("COGS", "sum"),
        GrossProfit=("GrossProfit", "sum"),
        NetUnitsSold=("QuantitySold", "sum"),
        Records=("SalesType", "size")
    ).reset_index()

    promotions["GrossMargin"] = np.where(
        promotions["NetSales"] > 0,
        promotions["GrossProfit"] / promotions["NetSales"] * 100,
        np.nan
    )

    promotions["ProfitPerUnit"] = np.where(
        promotions["NetUnitsSold"] > 0,
        promotions["GrossProfit"] / promotions["NetUnitsSold"],
        np.nan
    )

    return promotions.sort_values(
        "GrossProfit", ascending=False
    ).reset_index(drop=True)




def analyze_product_returns(df):

    purchases = df[df["IsReturn"] == 0]
    returns = df[df["IsReturn"] == 1]

    units_sold = purchases.groupby("ProductID").agg(
        UnitsSold=("QuantitySold", "sum")
    )

    returned = returns.groupby("ProductID").agg(
        UnitsReturned=("QuantitySold", "sum"),
        ReturnValue=("Sales", "sum")
    ).abs()

    result = units_sold.join(
        returned, how="outer"
    ).fillna(0).reset_index()

    result["ReturnRate"] = np.where(
        result["UnitsSold"] > 0,
        result["UnitsReturned"] / result["UnitsSold"] * 100,
        np.nan
    )

    return result.sort_values(
        "ReturnValue", ascending=False
    ).reset_index(drop=True)


def detect_high_return_products(return_analysis):

    high_returns = return_analysis[
        (return_analysis["UnitsSold"] >= 20) &
        (return_analysis["ReturnRate"] >= 10)
    ]

    return high_returns.sort_values(
        "ReturnValue", ascending=False
    ).reset_index(drop=True)




def analyze_daily_performance(df):

    daily = df.groupby("Date").agg(
        NetSales=("Sales", "sum"),
        GrossProfit=("GrossProfit", "sum")
    ).reset_index().sort_values("Date")

    daily["DayOfWeek"] = daily["Date"].dt.day_name()

    daily["ExpectedSales"] = (
        daily.groupby("DayOfWeek")["NetSales"]
        .transform(
            lambda x: x.shift(1).expanding(
                min_periods=4
            ).mean()
        )
    )

    daily["SalesDeviation"] = (
        (daily["NetSales"] - daily["ExpectedSales"])
        / daily["ExpectedSales"].where(
            daily["ExpectedSales"] > 0
        ) * 100
    )

    return daily.reset_index(drop=True)



def detect_sales_anomalies(daily):

    anomalies = daily[
        daily["SalesDeviation"].abs() >= 40
    ].copy()

    anomalies["AnomalyType"] = np.where(
        anomalies["SalesDeviation"] > 0,
        "Unusually High Sales",
        "Unusually Low Sales"
    )

    return anomalies.reset_index(drop=True)