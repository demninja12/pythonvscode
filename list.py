import streamlit as st

#a variable can store data, item but one at a time

#example:
restaurant = 'McDonalds' #stores only one restaurant

#what if you want to store all your favorite restaurants

#DATA COLLECTIONS: list, tuple, dictionary, set
#this helps you store more than one data, items at a time

#example:
FavRestaurants = ['McDonalds','KFC','Dominos','Burger King']

st.write('My favorite restaurants are',FavRestaurants)

#Examples of using lists:
#1. SELECTBOX: this give user the option to pick from in a box

#examples:
SelectFood = st.selectbox('Choose your favorite food',['Pizza','Burger','Hot Dog','Taco','Other'])

st.write('Your favorite food is',SelectFood)

#2. RADIO: This gives the user options to choose (Displays all options, good for less things)

IceCream = st.radio('Choose your favorite Ice Cream Flavour',['Chocolate','Vanilla','Other'])

st.write('Your favorite ice cream flavour is',IceCream)

#3. SIDEBAR: This is good for navigating from one page to the other
Menu = st.sidebar.selectbox('Menu',['First Page','Second Page','Third Page'])