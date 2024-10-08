import streamlit as st
st.set_page_config(page_title='Football Purchases',page_icon='🏈')

#Liam is an enthusiastic football fan and wants to enhance his game-day experience by purchasing various items. He plans to buy match tickets,
#a season pass, team merchandise, snacks, and even subscribe to a premium sports channel.
#Write a Python program to help Liam calculate the total cost of his football adventure.

ticket = 0

if st.checkbox('Purchase Tickets: $100'):
    st.success('Successfully purchased tickets')
    ticket += 100
    username = st.text_input('Username:')
    password = st.text_input('Password:',type='password')
    if username == 'Liam':
        if password == 'AlsoLiam':

            passes = st.radio('Choose a Pass',['Standard Pass: $200','VIP Pass: $500'],horizontal=True)
            merchandise = st.radio('Choose a item',['Jersey: $60','Scarf: $30','Hat: $20'])
            premium = st.radio('Choose a Premium Sports channel to subscribe to',['Monthly: $20','Annuel: $200'])

            if passes == 'Standard Pass: $200':
                st.success('Successfully purchased item')
            if passes == 'VIP Pass: $500':
                st.success('Successfully purchased item')
        
            if merchandise == 'Jersey: $60':
                st.success('Successfully purchased item')
            if merchandise == 'Scarf: $30':
                st.success('Successfully purchased item')
            if merchandise == 'Hat: $20':
                st.success('Successfully purchased item')
        
            if premium == 'Monthly: $20':
                st.success('Successfully purchased item')
            if premium == 'Annuel: $200':
                st.success('Successfully purchased item')







if username == 'Liam':
    if password == 'AlsoLiam':
        passes = st.radio('Choose a Pass',['Standard Pass: $200','VIP Pass: $500'],horizontal=True)
        merchandise = st.radio('Choose a item',['Jersey: $60','Scarf: $30','Hat: $20'])
        premium = st.radio('Choose a Premium Sports channel to subscribe to',['Monthly: $20','Annuel: $200'])

        if passes == 'Standard Pass: $200':
            st.success('Successfully purchased item')
        if passes == 'VIP Pass: $500':
            st.success('Successfully purchased item')
        
        if merchandise == 'Jersey: $60':
            st.success('Successfully purchased item')
        if merchandise == 'Scarf: $30':
            st.success('Successfully purchased item')
        if merchandise == 'Hat: $20':
            st.success('Successfully purchased item')
        
        if premium == 'Monthly: $20':
            st.success('Successfully purchased item')
        if premium == 'Annuel: $200':
            st.success('Successfully purchased item')



