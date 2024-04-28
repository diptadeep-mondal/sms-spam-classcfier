import streamlit as st
import pickle
import sklearn

cv=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

st.title('Email/SMS spam classifier')

input_sms=st.text_area('Enter the messeage')
if st.button('predict'):

    vector_input=cv.transform([input_sms])

    result=model.predict(vector_input)[0]

    if result==1:
        st.header('Spam')
    else:
        st.header('Ham')