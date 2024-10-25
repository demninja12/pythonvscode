import streamlit as st
import pandas as pd

st.set_page_config(page_title='Job Employment',page_icon='🏢')

menu = st.sidebar.selectbox('Menu',['Register Staff','Staff Database','Staff File'])

if menu == 'Register Staff':
    st.subheader('Register Here')

    left,right = st.columns(2)

    with left:
        firstname = st.text_input('First Name:')
    
    with right:
        lastname = st.text_input('Last name')

    with left:
        adress = st.text_input('Email Adress:')
    
    with right:
        gender = st.selectbox('Gender:',['Male','Female'])
    
    with left:
        department = st.selectbox('Department:',['Management','Accounting','Engineering','Human Resources','Security','Medical','Transportation'])
    
    with right:
        title = st.selectbox('Job Title:',['Board Of Directors', 'Supervisor', 'Senior Staff', 'Junior Staff', 'Paid Intern', 'Unpaid Intern'])
    
    with left:
        status = st.selectbox('Contract Status:',['Full Time','Part Time'])
    
    with right:
        income = st.number_input('Monthly Income:',0)
    
    with left:
        degree = st.selectbox('Educational Degree:',['None', 'Associate Degree', 'Bachelor Degree', 'Graduate Degree', 'Professional Degree', 'Doctoral Degree'])
    
    with right:
        date = st.date_input('Employment Date:')