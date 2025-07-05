"""config.py
Centralized configuration.
"""
from pathlib import Path
from dotenv import load_dotenv
import os

ENV = Path(__file__).resolve().parents[1] / ".env"
if ENV.exists():
    load_dotenv(ENV)

# Example: database connection string
DB_URL = os.getenv("DB_URL", "sqlite:///churn.db")
