import streamlit as st
import pandas as pd

st.set_page_config(page_title='File Uploader',page_icon='📂')

menu = st.sidebar.selectbox('Choose an option',['Upload CSV','Upload Image','Upload Audio','Upload Video'])

if menu == 'Upload CSV':
    st.subheader('Upload CSV to View')
    uploadcsv = st.file_uploader('Upload CSV File',type='CSV')

    if uploadcsv:
        csvlink = pd.read_csv(uploadcsv)
        with st.expander('Open CSV table'):
            st.table(csvlink)

if menu == 'Upload Image':
    st.subheader('Upload Images To View')
    uploadimage = st.file_uploader('Upload image file',type=['jpg','jpeg','png'])

    if uploadimage:
        st.image(uploadimage,use_column_width=True)

if menu == 'Upload Audio':
    st.subheader('Upload Audio To Play')
    uploadaudio = st.file_uploader('Upload Audio File',type=['mp3','wav'])
    if uploadaudio:
        st.audio(uploadaudio,format='audio/mp3')

if menu == 'Upload Video':
    st.subheader('Upload YouTube Video Link to Play')
    youtubelink = st.text_input('Paste IN Your YouTube Video Link Here')
    if st.button('Play YouTube Video'):
        try:
            if youtubelink:
                st.video(youtubelink)
        except:
            st.error('Sorry cannot play this video')


