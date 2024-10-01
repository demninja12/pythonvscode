import streamlit as st
import pandas as pd

csvfile = pd.read_csv('scores.csv')



menu = st.sidebar.selectbox('menu',['Submit Score','Database'])

if menu == 'Database':
    st.table(csvfile)


if menu == 'Submit Score':
    st.subheader('Student Scores')

    st.write('Submit Students Name:')
    name = st.text_input('')

    sc1,sc2 = st.columns(2)
    sc3,sc4 = st.columns(2)
    sc5,sc6 = st.columns(2)
    
    with sc1:
     math = st.number_input('Enter Students Math Score:',0,100)
    
    with sc2:
     eng = st.number_input('Enter Students English Score: ',0,100)
    
    with sc3:
     sci = st.number_input('Enter Students Science Score:  ',0,100)
    
    with sc4:
     history = st.number_input('Enter Students History Score:   ',0,100)

    with sc5:
     art = st.number_input('Enter Students Art Score:    ',0,100)

    with sc6:
     geo = st.number_input('Enter Students Geography Score:      ',0,100)

    total = math + eng + sci + history + art + geo



    average = total / 6

    if average >= 90:
     grade = 'A'
    elif average >= 80:
     grade = 'B'
    elif average >= 70:
     grade = 'C'
    elif average >= 60:
     grade = 'D'
    elif average >= 50:
     grade = 'D-'
    elif average < 50:
     grade = 'F'
    else:
     grade = '?'


    if st.button('Save Student Score'):
     st.write(name,'total score is',total,'and',name,'average is',average,'and',name,'got a',grade)

    studentdict = {'Name':[name],'Math':[math],'English':[eng],'Science':[sci],'History':[history],'Art':[art],'Geography':[geo]}
    studenttable = pd.DataFrame(studentdict)
    tablesjoin = pd.concat([csvfile,studenttable],ignore_index=True)
    tablesjoin.to_csv('scores.csv',index=False)