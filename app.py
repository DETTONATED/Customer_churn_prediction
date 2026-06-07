import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("customer_churn_model.pkl")

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Customer Churn Prediction System")
st.markdown("Predict whether a customer is likely to churn or not.")

# Inputs
gender = st.selectbox("Gender", ["Female", "Male"])

senior_citizen = st.selectbox(
    "Senior Citizen",
    ["No", "Yes"]
)

partner = st.selectbox(
    "Partner",
    ["No", "Yes"]
)

dependents = st.selectbox(
    "Dependents",
    ["No", "Yes"]
)

tenure = st.slider(
    "Tenure (Months)",
    0,
    72,
    12
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=1000.0
)

contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

# Encoding Maps
gender_map = {
    "Female": 0,
    "Male": 1
}

yes_no_map = {
    "No": 0,
    "Yes": 1
}

contract_map = {
    "Month-to-month": 0,
    "One year": 1,
    "Two year": 2
}

if st.button("Predict Churn"):

    data = pd.DataFrame({
        "gender": [gender_map[gender]],
        "SeniorCitizen": [yes_no_map[senior_citizen]],
        "Partner": [yes_no_map[partner]],
        "Dependents": [yes_no_map[dependents]],
        "tenure": [tenure],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges],
        "Contract": [contract_map[contract]]
    })

    prediction = model.predict(data)[0]

    if prediction == 1:
        st.error("⚠️ Customer is likely to Churn")
    else:
        st.success("✅ Customer is likely to Stay")