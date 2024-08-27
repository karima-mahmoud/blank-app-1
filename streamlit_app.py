import streamlit as st
import pickle
import numpy as np

# تحميل النموذج المحفوظ
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# عنوان التطبيق
st.title("تطبيق توقع مرض السكري")

# واجهة إدخال المستخدم
st.sidebar.header("أدخل البيانات الخاصة بك:")

def user_input_features():
    pregnancies = st.sidebar.number_input("عدد مرات الحمل", 0, 20, 1)
    glucose = st.sidebar.slider("تركيز الجلوكوز في البلازما", 0, 200, 120)
    blood_pressure = st.sidebar.slider("ضغط الدم الانبساطي (مم زئبق)", 0, 122, 70)
    skin_thickness = st.sidebar.slider("سمك ثنيات الجلد (مم)", 0, 99, 20)
    insulin = st.sidebar.slider("الأنسولين (ميكرومتر/مل)", 0, 846, 79)
    bmi = st.sidebar.slider("مؤشر كتلة الجسم (الوزن بالكجم/الطول بالمتر)^2", 0.0, 67.1, 25.0)
    diabetes_pedigree_function = st.sidebar.slider("دالة النسب الوراثي للسكري", 0.0, 2.42, 0.5)
    age = st.sidebar.slider("العمر (بالسنوات)", 21, 81, 30)
    
    data = {
        'Pregnancies': pregnancies,
        'Glucose': glucose,
        'BloodPressure': blood_pressure,
        'SkinThickness': skin_thickness,
        'Insulin': insulin,
        'BMI': bmi,
        'DiabetesPedigreeFunction': diabetes_pedigree_function,
        'Age': age
    }
    
    features = pd.DataFrame(data, index=[0])
    return features

# إدخال المستخدم
input_df = user_input_features()

# التنبؤ باستخدام النموذج المدرب
prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

# عرض النتيجة
st.subheader("النتيجة:")
diabetes_status = np.array(["غير مصاب", "مصاب"])
st.write(diabetes_status[prediction])

st.subheader("احتمالية الإصابة بالسكري:")
st.write(f"غير مصاب: {prediction_proba[0][0]:.2f}")
st.write(f"مصاب: {prediction_proba[0][1]:.2f}")
