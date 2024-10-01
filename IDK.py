import streamlit as st

st.title('?')

if st.button('Click This Button'):
    st.title('THIS PAGE WILL CRASH')
    while True:
        st.balloons()

if st.checkbox('Check This Checkbox'):
    st.title('THIS PAGE WILL CRASH')
    while True:
        st.balloons()



st.chat_input('???')


