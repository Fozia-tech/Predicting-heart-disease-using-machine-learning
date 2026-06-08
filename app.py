import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("heart_model.pkl", "rb"))

st.title("Heart Disease Prediction")

age = st.number_input("Age", 1, 120)
sex = st.selectbox("Sex (0=Female, 1=Male)", [0, 1])
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure")
chol = st.number_input("Cholesterol")
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting ECG Results", [0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved")
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("Oldpeak", format="%.1f")
slope = st.selectbox("Slope", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (ca)", [0, 1, 2, 3, 4])
thal = st.selectbox("Thal", [0, 1, 2, 3])

if st.button("Predict"):
    features = np.array([[age, sex, cp, trestbps, chol,
                          fbs, restecg, thalach,
                          exang, oldpeak, slope,
                          ca, thal]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠️ Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease Detected")