# ============================================================
# RetentionAI — Central Configuration File
# All settings live here. Change once, works everywhere.
# ============================================================

import os

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_RAW_PATH = os.path.join(BASE_DIR, "data", "raw", "telco_churn.csv")
DATA_PROCESSED_PATH = os.path.join(BASE_DIR, "data", "processed", "telco_processed.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "final_pipeline.pkl")
FEATURES_PATH = os.path.join(BASE_DIR, "models", "feature_names.json")

# --- Model Settings ---
SEED = 42
TEST_SIZE = 0.2
TARGET_COLUMN = "Churn"

# --- Features ---
NUMERICAL_FEATURES = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges"
]

CATEGORICAL_FEATURES = [
    "gender",
    "Partner",
    "Dependents",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod"
]

DROP_COLUMNS = ["customerID"]

# --- Prediction Threshold ---
THRESHOLD = 0.5

# --- API Settings ---
API_HOST = "0.0.0.0"
API_PORT = 8000