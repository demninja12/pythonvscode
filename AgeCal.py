import streamlit as st

a1,a2,a3 = st.columns(3)

with a2:
    st.header('Age Calculator')

name = st.text_input('Input Name: ')

currentyear = st.number_input('Input Current Year: ',0)

yob = st.number_input('Input Birth Year: ',0)

age = currentyear - yob

if st.button('Check My Age'):
    st.write('Your age is',age,'in',currentyear)