import streamlit as st
import numpy as np


import pickle
with open('model.pkl', 'rb') as file:
 model = pickle.load(file)

# Title of the app
st.title('Diabetes Prediction App')

# Sidebar for user inputs
st.sidebar.header('Patient Data')

def user_input_features():
    pregnancies = st.sidebar.number_input('Number of times pregnant', min_value=0, max_value=20, value=1)
    glucose = st.sidebar.slider('Glucose', 0, 200, 100)
    blood_pressure = st.sidebar.slider('Blood Pressure', 0, 130, 70)
    skin_thickness = st.sidebar.slider('Skin Thickness', 0, 100, 20)
    insulin = st.sidebar.slider('Insulin', 0, 900, 30)
    bmi = st.sidebar.slider('BMI', 0.0, 70.0, 15.0)
    dpf = st.sidebar.slider('Diabetes Pedigree Function', 0.0, 2.5, 0.5)
    age = st.sidebar.slider('Age', 15, 100, 25)
    
    data = {'Pregnancies': pregnancies,
            'Glucose': glucose,
            'BloodPressure': blood_pressure,
            'SkinThickness': skin_thickness,
            'Insulin': insulin,
            'BMI': bmi,
            'DiabetesPedigreeFunction': dpf,
            'Age': age}
    
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Display user inputs
st.subheader('Patient Input Data')
st.write(input_df)

# Preprocess the input data
input_data_scaled = scaler.transform(input_df)

# Prediction
prediction = model.predict(input_data_scaled)
prediction_proba = model.predict_proba(input_data_scaled)

st.subheader('Prediction')
diabetes_status = 'Diabetic' if prediction[0] == 1 else 'Non-diabetic'
st.write(diabetes_status)

st.subheader('Prediction Probability')
st.write(f"Probability of being Diabetic: {prediction_proba[0][1]:.2f}")


