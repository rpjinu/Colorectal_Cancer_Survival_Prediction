import streamlit as st
import joblib
import pandas as pd

# Load the trained model and encoder
model = joblib.load("model.pkl")
encoder = joblib.load("encoder.pkl")

# Streamlit UI
st.title("🏥 Colorectal Cancer Survival Prediction API")
st.write("Enter patient details to predict survival status.")

# User Inputs
age = st.number_input("Age", min_value=20, max_value=100, value=50)
bmi = st.number_input("BMI", min_value=10.0, max_value=40.0, value=25.0)
smoking = st.selectbox("Smoking Status", ["Never", "Former", "Current"])
alcohol = st.selectbox("Alcohol Consumption", ["Never", "Occasional", "Regular"])
chemotherapy = st.selectbox("Chemotherapy Received", ["Yes", "No"])

# Encode categorical features
input_data = pd.DataFrame([[age, bmi, smoking, alcohol, chemotherapy]], 
                          columns=["Age", "BMI", "Smoking_Status", "Alcohol_Consumption", "Chemotherapy_Received"])

input_data_encoded = encoder.transform(input_data)

# Make prediction
if st.button("Predict"):
    prediction = model.predict(input_data_encoded)
    result = "Survived" if prediction[0] == 1 else "Not Survived"
    st.success(f"Prediction: {result}")
