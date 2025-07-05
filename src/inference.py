# src/inference.py

import joblib
import pandas as pd
from genai_helper import suggest_retention_strategy

def load_model(model_path="models/xgboost_model.pkl"):
    return joblib.load(model_path)

def predict_churn(model, input_df: pd.DataFrame):
    predictions = model.predict(input_df)
    probabilities = model.predict_proba(input_df)[:, 1]
    return predictions, probabilities

if __name__ == "__main__":
    from data_loader import load_data
    from preprocessing import clean_and_preprocess

    # Load and preprocess data
    df = load_data()
    X_train, X_test, y_train, y_test = clean_and_preprocess(df)

    # Load model and predict
    model = load_model()
    preds, probs = predict_churn(model, X_test)

    # Prepare result DataFrame
    result_df = X_test.copy()
    result_df["Churn_Prediction"] = preds
    result_df["Churn_Probability"] = probs

    # Add contract and internet fields back (needed for rule engine)
    result_df["Contract"] = df.loc[X_test.index, "Contract"]
    result_df["InternetService"] = df.loc[X_test.index, "InternetService"]

    # Add suggestions
    print("Generating suggestions...")
    result_df["Retention_Strategy"] = [
        suggest_retention_strategy(row._asdict(), prob)
        for row, prob in zip(result_df.itertuples(index=False), probs)
    ]

    # Save to CSV
    output_path = "reports/predictions_with_suggestions.csv"
    result_df.to_csv(output_path, index=False)
    print(f"\n✅ Done! Results saved to {output_path}")
