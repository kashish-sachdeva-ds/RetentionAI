import streamlit as st
import pandas as pd

st.set_page_config(page_title="RetentionAI", layout="wide")

st.title("🛡️ RetentionAI: Customer Churn Prediction System")
st.markdown("---")

# User Input Section
st.sidebar.header("Input Customer Details")

def user_input_features():
    tenure = st.sidebar.slider('Tenure (Months)', 0, 72, 12)
    monthly_charges = st.sidebar.number_input('Monthly Charges', 0, 150, 70)
    contract = st.sidebar.selectbox('Contract', ('Month-to-month', 'One year', 'Two year'))
    
    # Yahan baki features add karenge training ke baad
    data = {
        'tenure': tenure,
        'MonthlyCharges': monthly_charges,
        'Contract': contract
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

st.subheader('Customer Data for Prediction')
st.write(input_df)

st.warning("⚠️ Waiting for the trained model to start predicting...")