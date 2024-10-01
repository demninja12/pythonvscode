import streamlit as st

st.write('PYTHON IF ELSE')
st.title('QUESTION 16: IF ELSE')
st.write('July 24 2024')
st.subheader('')

st.write('Sam and his friends are planning a fun summer holiday. They have saved up $250 each to spend on various activities. They want to visit a theme park, go to the movies, buy some snacks, rent bikes for a day, and go to the beach. Sam wants to know how much money he has left after all these activities.')

savings = 250

theme_park_cost = st.number_input('Input theme park cost: ',0)

movies_cost = st.number_input('Input movie cost: ',0)

snacks_cost = st.number_input('Input snacks cost: ',0)

bikes_cost = st.number_input('Input bikes coost: ',0)

beach_cost = st.number_input('Input beach cost: ',0)

total = theme_park_cost + movies_cost + snacks_cost + bikes_cost + beach_cost

remaining = savings - total

if remaining > 0:
    if st.button('Checkout'):
        st.write('you still have',remaining,'dollars left')
else:
    if st.button('Checkout'):
        st.write('you spent',remaining ,'more than your savings')