import streamlit as st
import pandas as pd #this can help it read csv

st.set_page_config(page_title='Book a Doctor',page_icon='😷')

Menu = st.sidebar.selectbox('Menu',['Book Appointment','Database'])
csvlink = pd.read_csv('appointment.csv') #this will read the csv link

if Menu == 'Database':
    adminpass = st.sidebar.text_input('Enter admin password',type='password')
    if adminpass == 'doctorapple':
        st.table(csvlink)

if Menu == 'Book Appointment':

    st.subheader('Docter Appointment Request Form')
    st.write('Fill the form below and we will get back soon to you for more updates and plan your appointment')

    left, right = st.columns(2)

    with left:
        firstname = st.text_input('First name')

    with right:
        lastname = st.text_input('Last name')


    with left:
        birthday = st.date_input('Birthday')

    with right:
        occupation = st.text_input('Enter your occupation')


    with left:
        gender = st.selectbox('Gender',['Male','Female'])

    with right:
        phone = st.text_input('Phone Number')

    street1 = st.text_input('Street Address 1')

    street2 = st.text_input('Street Address 2')

    left1,right1 = st.columns(2)

    with left1:
        city = st.text_input('City')
    
    with right1:
        state = st.text_input('Province|State')


    if st.button('Book Appointment'):
        doctordict = {'Firstname':[firstname],'Lastname':[lastname],
                          'Birthday':[birthday],'Occupation':[occupation],'Gender':[gender],
                          'Phone':[phone],'Street1':[street1],'Street2':[street2],'City':[city],'State':[state]}
        doctortable = pd.DataFrame(doctordict)
        #st.write(doctordict)
        #st.table(doctordict)
        tablesjoin = pd.concat([csvlink,doctortable],ignore_index=True)
        tablesjoin.to_csv('appointment.csv',index=False)
        st.success('Submission Completed')


 


    #control + ]    #space for Menu 
    #windows + .    #icon



