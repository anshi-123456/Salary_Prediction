import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load trained model
with open("salary_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load training feature columns
with open("model_columns.pkl", "rb") as file:
    model_columns = pickle.load(file)

st.title("🧠 Salary Prediction App")

# Input fields
age = st.number_input("Age", min_value=18, max_value=70)
gender = st.selectbox("Gender", ["Male", "Female"])
education = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
job_title = st.text_input("Job Title")
experience = st.number_input("Years of Experience", min_value=0, max_value=50)

# Predict button
if st.button("Predict Salary"):
    # Create a dataframe with the user input
    input_data = pd.DataFrame([{
        'Age': age,
        'Gender': gender,
        'Education Level': education,
        'Job Title': job_title,
        'Years of Experience': experience
    }])

    # Encode the input to match training
    input_encoded = pd.get_dummies(input_data)

    # Align the input to match model’s training columns
    input_aligned = input_encoded.reindex(columns=model_columns, fill_value=0)

    # Make prediction
    prediction = model.predict(input_aligned)
    st.success(f"💰 Predicted Salary: ₹{prediction[0]:,.2f}")
