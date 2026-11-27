import pandas as pd


def validate_data(df, required_columns):
    df = df.copy()

    if df.empty:
        raise ValueError("The dataset is empty.")

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    return df


def preprocess_data(df):
    df = df.copy()

    df.columns = df.columns.str.strip()

    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(
            df["Date"], errors="coerce"
        )

        if df["Date"].isna().any():
            raise ValueError(
                "The dataset contains invalid or missing dates."
            )

        df = df.sort_values("Date")

    return df.reset_index(drop=True)