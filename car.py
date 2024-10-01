import streamlit as st


st.title('Ride Peggy')

column1,column2 = st.columns(2)
with column1:
    name = st.text_input('Enter your name: ')

with column2:
    salery = st.number_input('Enter your yearly salery: ',0,100000000000)

if st.button('Find a Car'):
    if salery < 29000:
        st.write('you can not afford any cars')
    elif salery < 30000:
        st.write('you can afford a used car')
    elif salery < 60000:
        st.write('you can buy a economy car')
    elif salery < 100000:
        st.write('you can buy a mid range car')
    elif salery < 200000:
        st.write('you can buy a luxury car')
    elif salery > 200000:
        st.write('you can buy a super car')



#'>' =  'Bigger'
#'<' =  'Smaller'
#'==' = 'is'