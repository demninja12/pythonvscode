import streamlit as st
import pandas as pd

#create a simple church age range project
#This will get the name of the member, get the age too
#also get the gender of the church member (radio button) -submit button

#when you click on submit button:
#Make sure you group members in different category based on their age 
# (Kids(3- 12), Teens(13-19), Youth(20-35), Adult(36-64), Elders(65+) )


st.title('Church Sign Up')
csvlink = pd.read_csv('church.csv')

section1,section2 = st.columns(2)

password = st.text_input('Enter your password: ',type='password')

with section1:
    name = st.text_input('Enter your name: ')

with section2:
    age = st.number_input('Enter your age: ',0)

with section1:
    gender = st.radio('Enter your age: ',['Male','Female'],horizontal=True)

with section2:
    if st.button('Sign Up'):
        if age < 12:
            st.write(name,'you are in the Kids section')
        elif age < 19:
            st.write(name,'you are in the Teens section')
        elif age < 35:
            st.write(name,'you are in the Youth section')
        elif age <64:
            st.write(name,'you are in the Adults section')
        elif age > 65:
            st.write(name,'you are in the Elders section')
        
        churchdict = {'Name':[name],'Age':[age],'Gender':[gender]}
        churchtable = pd.DataFrame(churchdict)
        #table?
        tablesjoin = pd.concat([csvlink,churchtable],ignore_index=True)
        tablesjoin.to_csv('church.csv',index=False)
        st.success('Sign Up Complete')

        if password == 'church':
          st.write('hello',name)





