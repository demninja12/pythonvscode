import streamlit as st
from email.message import EmailMessage
import ssl
import smtplib

sender = 'githubtee@gmail.com'
password = 'cczaelfrzzyywngz'

reasiever = st.text_input('Enter email send to: ')
subject = st.text_input('Enter email subject: ')

body = st.text_area('Enter email content here: ',height=200)

if st.button('Send Mail'):
    email = EmailMessage()
    email['From']=sender
    email['To']=reasiever
    email['subject']=subject
    email.set_content(body)
    securecontent = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',456,context=securecontent) as smtp:
        smtp.login(sender,password)
        smtp.sendmail(sender,reasiever,email.as_string())
        st.success('Email Sent')