import streamlit as st
import pickle

with open('model3.pkl', 'rb') as file:
    model = pickle.load(file)


st.title("diabetes patient")

Pregnancies = st.number_input('Pregnancies' , min_value=0.0 , max_value=20.0,value=1.0)
Glucose = st.number_input('Glucose' , min_value=0.0 , max_value=220.0,value=1.0)
blood_pressure =st.number_input('blood_pressure' , min_value=0.0 , max_value=150.0,value=1.0)
skin_thickness =st.number_input('skin_thickness' , min_value=0.0 , max_value=100.0,value=1.0)
Insulin =  st.number_input('Insulin' , min_value=0.0 , max_value=900.0,value=1.0)
BMI =  st.number_input('BMI' , min_value=0.0 , max_value=100.0,value=1.0)
DiabetesPedigreeFunction =  st.number_input('DiabetesPedigreeFunction' , min_value=0.0 , max_value=4.0,value=1.0)
Age =  st.number_input('Age' , min_value=0.0 , max_value=100.0,value=1.0)

output = model.predict([[Pregnancies,Glucose,blood_pressure,skin_thickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

st.write("diabetes patient : ",round(output[0],2))
