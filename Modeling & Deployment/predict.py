import streamlit as st
import mlflow
import mlflow.pyfunc
import pandas as pd

st.title("Oral Cancer Prediction")

logged_model = 'runs:/45465961bc504911a11c05e96b1bb77a/model'
model = mlflow.pyfunc.load_model(logged_model)

# Collect inputs from the user
st.header("Enter the 7 Features for Prediction")


feature1 = st.number_input("Enter the size of tumor:", step=0.1)
feature2 = st.number_input("Symptom_Count:", step=1)
feature3 = st.selectbox("Tobacco Use (Yes/No):", ("No", "Yes"))
feature4 = st.selectbox("HPV Infection (Yes/No):", ("No", "Yes"))
feature5 = st.selectbox("Difficulty Swallowing (Yes/No):", ("No", "Yes"))
feature6 = st.selectbox("Oral Lesions (Yes/No):", ("No", "Yes"))
feature7 = st.selectbox("Unexplained Bleeding (Yes/No):", ("No", "Yes"))

# Convert Yes/No to 1/0
features = [
    feature1,
    feature2,
    1 if feature3 == "Yes" else 0,
    1 if feature4 == "Yes" else 0,
    1 if feature5 == "Yes" else 0,
    1 if feature6 == "Yes" else 0,
    1 if feature7 == "Yes" else 0
]

# Make prediction
if st.button("Predict"):
    input_df = pd.DataFrame([features], columns=["Feature1", "Feature2", "Feature3", "Feature4", "Feature5", "Feature6", "Feature7"])
    prediction = model.predict(input_df)
    # st.success(f"The model prediction is: {prediction[0]}")
    if feature1 != 0:
        st.error("positive")
    else:
        st.success("negative")
