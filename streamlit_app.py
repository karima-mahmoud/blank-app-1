import streamlit as st
import pickle

with open('model3.pkl', 'rb') as file:
    model = pickle.load(file)


st.title("diabetes patient")

Pregnancies = st.sidebar.number_input('Pregnancies' , min_value=0 , max_value=20,value=1)
Glucose = st.sidebar.number_input('Glucose' ,min_value= 0 ,max_value=200,value=1)
blood_pressure =st.sidebar.number_input('blood_pressure' ,min_value=0 ,max_value= 130,value=1)
skin_thickness =st.sidebar.number_input('skin_thickness' , min_value=0 , max_value=100,value=1)
Insulin =  st.sidebar.number_input('Insulin' , min_value=0 , max_value=900,value=1)
BMI =  st.sidebar.number_input('BMI' , min_value=0.0 , max_value=70.0,value=1.0)
DiabetesPedigreeFunction =  st.sidebar.number_input('DiabetesPedigreeFunction' , min_value=0.0 , max_value=2.5,value=0.0)
Age =  st.sidebar.number_input('Age' , min_value=15 , max_value=100,value=25)

output = model.predict([[Pregnancies,Glucose,blood_pressure,skin_thickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
prediction_proba = model.predict_proba([[Pregnancies,Glucose,blood_pressure,skin_thickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])[0]

st.write("diabetes patient : ",round(output[0],2))


if output[0] == 1:
    st.success(f"من المتوقع أن تكون مصاباً بالسكري بنسبة احتمال تصل إلى {prediction_proba[1] * 100:.2f}%.")
else:
    st.success(f"من المتوقع أن تكون غير مصاب بالسكري بنسبة احتمال تصل إلى {prediction_proba[0] * 100:.2f}%.")



from PIL import Image
image1 = Image.open("diabetes_image.jpg")
image2 = Image.open("diabetesimage2.jpg")
st.image(image1, caption="", use_column_width=True)
st.image(image2, caption="", use_column_width=True)
