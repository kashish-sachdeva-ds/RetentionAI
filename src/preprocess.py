import pandas as pd
import numpy as np

def clean_data(df):
    """Basic cleaning steps we found during EDA"""
    # TotalCharges fix
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'].fillna(0, inplace=True)
    
    # Drop unnecessary columns
    if 'customerID' in df.columns:
        df.drop('customerID', axis=1, inplace=True)
    
    return df

def encode_data(df):
    """Converting categorical text to numbers"""
    # Binary Mapping
    binary_cols = ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', 'Churn']
    for col in binary_cols:
        df[col] = df[col].map({'Yes': 1, 'No': 0})
    
    # One-Hot Encoding for multi-class
    df = pd.get_dummies(df, drop_first=True)
    
    return df