import streamlit as st
import pickle

with open('model3.pkl', 'rb') as file:
    model = pickle.load(file)


st.title("diabetes patient")

Pregnancies = st.sidebar.number_input('Pregnancies' , min_value=0.0 , max_value=20.0,value=1.0)
Glucose = st.sidebar.number_input('Glucose' , min_value=0.0 , max_value=220.0,value=1.0)
blood_pressure =st.sidebar.number_input('blood_pressure' , min_value=0.0 , max_value=150.0,value=1.0)
skin_thickness =st.sidebar.number_input('skin_thickness' , min_value=0.0 , max_value=100.0,value=1.0)
Insulin =  st.sidebar.number_input('Insulin' , min_value=0.0 , max_value=900.0,value=1.0)
BMI =  st.sidebar.number_input('BMI' , min_value=0.0 , max_value=100.0,value=1.0)
DiabetesPedigreeFunction =  st.sidebar.number_input('DiabetesPedigreeFunction' , min_value=0.0 , max_value=4.0,value=1.0)
Age =  st.sidebar.number_input('Age' , min_value=0.0 , max_value=100.0,value=1.0)

output = model.predict([[Pregnancies,Glucose,blood_pressure,skin_thickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

st.write("diabetes patient : ",round(output[0],2))


from PIL import Image
image = Image.open("diabetes_image.jpg")
image = Image.open("diabetesimage2.jpg")
st.image(image, caption="", use_column_width=True)
