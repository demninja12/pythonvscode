import streamlit as st
import pandas as pd

st.set_page_config(page_title='Blood Donation Registration',page_icon='🩸')

menu = st.sidebar.selectbox('Menu',['Registration','Donation Database'])
csvlink = pd.read_csv('donor.csv')

if menu == 'Registration':
    st.header('Blood Donation Registartion')
    left,right = st.columns(2)

    with left:
        name = st.text_input('Name:')

    with right:
        number = st.number_input('Contact Number:',0)
    
    with left:
        blood = st.radio('Select Your Blood Group:',['A','B','AB','O'])
    
    with right:
        illness = st.radio('Select Illness',['Disease','Infection','None'],horizontal=True)
    
    if st.button('Submit Donor Details'):
        donordict = {'Name':[name],'Contact Number':[number],
                 'Blood Group':[blood],'Illness':[illness]}
        donortable = pd.DataFrame(donordict)
        #st.table(donordict)
        tablesjoin = pd.concat([csvlink,donortable],ignore_index=True)
        tablesjoin.to_csv('donor.csv',index=False)
        st.success('Success')
    
if menu == 'Donation Database':
    st.table(csvlink)