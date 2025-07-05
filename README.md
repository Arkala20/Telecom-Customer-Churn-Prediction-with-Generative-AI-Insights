# Customer Churn Prediction with Generative AI Insights

This project demonstrates an end-to-end workflow for predicting customer churn in the telecom industry **and** generating human-readable retention strategies using Generative AI.

## Key Features
- Clean, modular Python code organized in the `src/` folder.
- Reproducible training pipeline using XGBoost.
- Command-line inference script with flexible input.
- Exported datasets ready for visualization tools like Power BI or Tableau.
- Initial Generative AI integration for retention strategy suggestions (OpenAI API placeholder).

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Place the Telco churn CSV dataset inside the data/ folder
#    Example dataset: https://www.kaggle.com/blastchar/telco-customer-churn
#    Rename downloaded file to: data/telco_churn.csv
mv ~/Downloads/Telco-Customer-Churn.csv data/telco_churn.csv

# 3. Train the churn prediction model
python -m src.model

# 4. Run inference and generate retention suggestions
python -m src.inference --input_csv data/telco_churn.csv

#Repository Layout

churn_prediction_project/
├── data/                # Raw input CSV dataset(s)
├── models/              # Saved trained models (.pkl files)
├── reports/             # Output reports, prediction CSVs, figures
├── src/                 # Source code modules
│   ├── data_loader.py       # Data loading utilities
│   ├── preprocessing.py     # Data cleaning and feature engineering
│   ├── model.py             # Model training and evaluation
│   ├── inference.py         # Churn prediction and AI strategy generation
│   ├── genai_helper.py      # Generative AI retention strategy helper
│   └── config.py            # Configuration and constants
├── requirements.txt     # Python dependencies
└── README.md            # Project overview and instructions

Next Steps
Connect exported predictions to Power BI or Tableau for interactive dashboards.

Extend genai_helper.py to generate personalized retention emails or chatbot responses.

Containerize the project with Docker for easier deployment and scalability.

Integrate real OpenAI API keys and handle usage quotas for production-grade AI assistance.


## Power BI Dashboard

The Power BI dashboard file is saved at: `reports/churn_dashboard.pbix`

Open this file in Power BI Desktop to explore churn risk, customer segments, and retention strategy visualizations.

You can refresh the dataset in Power BI by loading updated CSV prediction files exported from the `reports/` folder.
