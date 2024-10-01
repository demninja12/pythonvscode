import streamlit as st
st.set_page_config(page_title='Roblox',page_icon='🎮')

user = 0
log = 0
RobloxCost = 0

bc1 = 0
bc10 = 0
mc1 = 0
mc10 = 0

pc100 = 0
pc1000 = 0
pc10000 = 0
pc100000 = 0

rb10 = 0
rb25 = 0
rb50 = 0


st.title('Play Store')

if st.checkbox('Roblox: $150'):
    st.success('Purchase Complete')
    RobloxCost = 150

st.title('')

st.title('Apps:')
if st.checkbox('Roblox'):
    st.title('ROBLOX')
    if RobloxCost == 150:
        username = st.text_input('Username: ')
        if username == 'Daniel19':
            user = 1

        password = st.text_input('Password: ',type='password')
        if password == 'Roblox16':
            log = 1
        
        login = user + log

        if st.checkbox('Login'):
            if login == 2:
                st.success('Successfully loged in')

                st.subheader('Discover')
                games = st.radio('Games:',['Piggy','Toilet Tower Defence'],horizontal=True)

                if st.checkbox('Purchase Robux'):
                    if st.checkbox('$10: 800R'):
                        st.success('Successfully bought 800 Robux')
                        rb10 = 10
                    if st.checkbox('$25: 2000R'):
                        st.success('Successfully bought 2,000 Robux')
                        rb25 = 25
                    if st.checkbox('$50: 4500R'):
                        st.success('Successfully bought 4,500 Robux')
                        rb50 = 50

                if games == 'Piggy':
                    st.title('PIGGY')
                    if st.checkbox('Buy Coins'):
                        if st.checkbox('100: $10'):
                            st.success('successfully bought 100 coins')
                            pc100 = 10
                        if st.checkbox('1,000: $100'):
                            st.success('successfully bought 1,000 coins')
                            pc1000 = 100
                        if st.checkbox('10,000: $1,000'):
                            st.success('successfully bought 10,000 coins')
                            pc10000 = 1000
                        if st.checkbox('100,000: $10,000'):
                            st.success('successfully bought 100,000 coins')
                            pc100000 = 10000
                
                if games == 'Toilet Tower Defence':
                    st.title('Toilet Tower Defence')

                    menu = st.radio('',['Summon Units','Exclusive Shop'],horizontal=True)

                    if menu == 'Summon Units':
                        crates = st.selectbox('Crates',['Basic Crate','Mythic Crate'])

                        if crates == 'Basic Crate':
                            if st.checkbox('Summon 1: 100🪙'):
                                bc1 = 100
                            
                            if st.checkbox('Summon 10: 900🪙'):
                                bc10 = 900
                        
                        if crates == 'Mythic Crate':
                            if st.checkbox('Summon 1: 1200🪙'):
                                mc1 = 1200
                            
                            if st.checkbox('Summon 10: 10800🪙'):
                                mc10 = 10800
                    
                    if menu == 'Exclusive Shop':
                        st.write('')
            
            else:
                st.write('Login Incorrect')
    else:
        st.write('Game Not Installed')

st.subheader('')

if st.checkbox('Bank'):
    st.title('Bank')

    st.write('')

    st.subheader('History:')
    history = bc1 + bc10 + mc1 + mc10 + RobloxCost + pc100 + pc1000 + pc10000 + pc100000 + rb10 + rb25 + rb50
    if st.button('View History'):
        st.write('You spent',history,'dollors')
        
            
