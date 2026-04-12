# RetentionAI — Customer Churn Risk Scoring API

## Business Problem
A telecom company loses Rs 2.4 crore annually to preventable customer churn.
This system predicts which customers are at risk of leaving and explains exactly 
WHY — enabling the retention team to take targeted action before the customer leaves.

## What This System Does
- Predicts churn probability for any customer (0% to 100%)
- Explains the top reasons driving that prediction (SHAP values)
- Serves predictions via REST API in under 50ms
- Provides an interactive dashboard for non-technical stakeholders

## Tech Stack
| Layer | Technology |
|-------|-----------|
| Language | Python 3.10 |
| ML | Scikit-learn, XGBoost, SHAP |
| Imbalance Handling | imbalanced-learn (SMOTE) |
| API | FastAPI |
| UI | Streamlit |
| Experiment Tracking | MLflow |
| Deployment | Streamlit Cloud + Render |

## Model Results
| Model | F1 Macro | AUC-ROC |
|-------|----------|---------|
| Logistic Regression (baseline) | - | - |
| Random Forest | - | - |
| XGBoost (final) | - | - |

*(Results updated after training)*

## Project Structure

RetentionAI/
├── app/main.py          → Streamlit UI
├── api/main.py          → FastAPI REST endpoint
├── src/
│   ├── config.py        → All settings
│   ├── preprocess.py    → Data cleaning & feature engineering
│   ├── train.py         → Model training & evaluation
│   └── predict.py       → Load model & make predictions
├── models/              → Saved pipeline (not in GitHub)
├── data/                → Dataset (not in GitHub)
├── notebooks/           → EDA & training experiments
└── requirements.txt     → All dependencies

## Dataset
- Source: [Telco Customer Churn — Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- Version: 1 (downloaded April 2026)
- Size: 7,043 rows × 21 columns
- Download and place in `data/raw/telco_churn.csv`

## How to Run Locally
```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/RetentionAI.git
cd RetentionAI

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add dataset to data/raw/ folder

# 5. Train the model
python src/train.py

# 6. Run Streamlit app
streamlit run app/main.py

# 7. Run FastAPI (separate terminal)
uvicorn api.main:app --reload
```

## Live Demo
- Streamlit App: *(link added after deployment)*
- API Endpoint: *(link added after deployment)*

## Author
**Kashish Sachdeva**  
B.E. CSE AI/ML | Chitkara University | Batch 2027  
[GitHub](#) | [LinkedIn](#)