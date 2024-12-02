import streamlit as st
import pandas as pd

st.set_page_config(page_title='Buy Houses',page_icon='🏠')
csvlink = pd.read_csv('house.csv')

#TEST 1: House.py
#write a python program for house buyers
#create a menu for the buy house page and the house database page
#Ask them for their name
#ask them for their yearly salary
#if they earn below 100,000 they can buy or rent an apartment
#If the earn between 100,000-500,000 they can buy a bungalow
#If the earn between >500,000-1,000,000 they can buy a duplex
#If the earn between >1,000,000-5,000,000 they can buy a mansion
#if the earn above 5000000 they can buy an estate
#create a database to to store and view their answers and display in another customer section


menu = st.sidebar.selectbox('Menu',['Houses','Database'])

st.title('Buy Houses')

if menu == 'Houses':
    st.header('Houses:')
    left,right = st.columns(2)

    with left:
        firstname = st.text_input('First Name:')
        age = st.number_input('Age:',0)

    with right:
        lastname = st.text_input('Last Name:')
        salary = st.number_input('Yearly Salary:',0)
    
    with left:
        if st.button('Search Houses'):
            if salary < 99999:
                st.write('You can not afford a house')
            elif salary < 100000:
                st.write('You can afford an apartment')
            elif salary < 500000:
                st.write('You can afford a bungalow')
            elif salary < 1000000:
                st.write('You can afford a duplex')
            elif salary < 5000000:
                st.write('You can afford a mansion')
            elif salary < 100000000:
                st.write('You can afford an estate')
            elif salary < 50000000000000000000000:
                st.write('You can afford a country')
            elif salary > 500000000000000000000000000000:
                st.write('You can afford the world')
            else:
                st.error('Unkown')
    
    with right:
        if st.button('Comfirm Purchase'):
            st.success('Purchase Success')
            housedict = {'First Name':[firstname],
                         'Last Name':[lastname],
                         'Age':[age],
                         'Yearly Salary':[salary]}
            housetable = pd.DataFrame(housedict)
            tablesjoin = pd.concat([csvlink,housetable],ignore_index=True)
            tablesjoin.to_csv('house.csv',index = False)
    

if menu == 'Database':
    st.header('Database:')
    password = st.text_input('Password:',type='password')
    if password == 'housedatabase':
        st.table(csvlink)