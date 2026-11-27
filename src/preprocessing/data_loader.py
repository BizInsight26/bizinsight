from pathlib import Path

import pandas as pd


def load_data(file_path):
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError("The selected file does not exist.")

    extension = file_path.suffix.lower()

    if extension == ".csv":
        df = pd.read_csv(file_path)

    elif extension in [".xlsx", ".xls"]:
        df = pd.read_excel(file_path)

    else:
        raise ValueError(
            "Unsupported file format. Please use CSV or Excel."
        )

    if df.empty:
        raise ValueError("The uploaded file is empty.")

    df.columns = df.columns.str.strip()

    return df