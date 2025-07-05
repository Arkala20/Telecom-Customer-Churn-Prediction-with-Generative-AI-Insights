# src/data_loader.py

import pandas as pd
from pathlib import Path

def load_data(filename="data/telco_churn.csv") -> pd.DataFrame:
    path = Path(filename)
    if not path.exists():
        raise FileNotFoundError(f"{filename} not found.")
    df = pd.read_csv(path)
    return df

if __name__ == "__main__":
    df = load_data()

    print("\n🔹 First 5 rows:")
    print(df.head())

    print("\n🔹 Data types:")
    print(df.dtypes)

    print("\n🔹 Null values per column:")
    print(df.isnull().sum())

    print("\n🔹 Dataset shape:", df.shape)
