# src/preprocessing.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def clean_and_preprocess(df: pd.DataFrame):
    # Fix TotalCharges: convert to numeric, coerce errors to NaN
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # Fill missing TotalCharges (if any) with 0 or median
    df['TotalCharges'] = df['TotalCharges'].fillna(0)


    # Encode target variable: 'Churn' (Yes/No) to 1/0
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    # Identify categorical columns (excluding customerID and target)
    cat_cols = df.select_dtypes(include='object').columns.tolist()
    cat_cols = [col for col in cat_cols if col not in ['customerID', 'Churn']]

    # Encode categorical columns with LabelEncoder (you can change to OneHotEncoder if preferred)
    le = LabelEncoder()
    for col in cat_cols:
        df[col] = le.fit_transform(df[col])

    # Drop customerID as it's an identifier, not useful for modeling
    df.drop('customerID', axis=1, inplace=True)

    # Split into features and target
    X = df.drop('Churn', axis=1)
    y = df['Churn']

    # Split into train and test sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    from data_loader import load_data

    df = load_data()
    X_train, X_test, y_train, y_test = clean_and_preprocess(df)

    print(f"Train shape: {X_train.shape}, Test shape: {X_test.shape}")
    print(f"Sample features:\n{X_train.head()}")
