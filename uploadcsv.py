import streamlit as st
import pandas as pd

menu = st.sidebar.selectbox('Choose an option',['Upload CSV','Upload Image'])

if menu == 'Upload CSV':
    uploadcsv = st.file_uploader('Upload CSV File',type='CSV')

    if uploadcsv:
        csvlink = pd.read_csv(uploadcsv)
        with st.expander('Open CSV table'):
            st.table(csvlink)

if menu == 'Upload Image':
    uploadimage = st.file_uploader('Upload image file',type=['jpg','jpeg','png'])

    if uploadimage:
        st.image(uploadimage,use_column_width=True)