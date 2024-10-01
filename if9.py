import streamlit as st

st.write('PYTHON IF ELSE')
st.title('QUESTION 9: IF ELSE')
st.write('MAY 22 2024')
st.subheader('')

st.write('A boy saved $200. Write a Python program to find out how much money he has left after spending on various activities and check if he has any money left or if he spent more than he saved.')

savings = 200

movie_cost = st.number_input('Enter movie cost: ',1)

popcorn_cost = st.number_input('Enter popcorn cost: ',1)

ice_cream_cost = st.number_input('Enter ice cream cost: ',1)

transport_cost = st.number_input('Enter transport cost: ',1)

lost_money = st.number_input('Enter how much money you lost: ',1)

total = movie_cost + popcorn_cost + ice_cream_cost + transport_cost + lost_money

remaining = savings - total

if remaining > 0:
    if st.button('Checkout'):
        st.write('you still have',remaining,'dollars remaining')

elif remaining == 0:
    if st.button('Checkout'):
        st.write('you spent all of your saved amount')

else:
    if st.button('Checkout'):
        st.write('You spent',remaining,'dollars more than your savings')