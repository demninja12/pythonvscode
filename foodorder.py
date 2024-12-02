import streamlit as st
import pandas as pd

st.set_page_config(page_title='Peggy Cafe',page_icon='☕')

csvlink = pd.read_csv('peggycafe.csv')

Menu = st.sidebar.selectbox('Menu',['Cafe','Other'])

if Menu == 'Cafe':

    st.title('Peggy Cafe')

    st.image('https://d1csarkz8obe9u.cloudfront.net/posterpreviews/fast-food-banner-template-design-925774928d842fc1ac0186b839a10444_screen.jpg?ts=1689218877')

    app1 = 0
    app2 = 0
    app3 = 0
    mea1 = 0
    mea111 = 0
    mea21 = 0
    mea22 = 0
    mea23 = 0
    mea24 = 0
    mea222 = 0
    mea3 = 0
    mea333 = 0
    fru1 = 0
    fru2 = 0
    fru3 = 0
    des1 = 0
    des2 = 0
    des3 = 0
    des31 = 0
    des32 = 0
    des33 = 0
    des34 = 0
    dri1 = 0
    dri2 = 0
    dri3 = 0
    km1 = 0
    km2 = 0
    km3 = 0
    ptc = 0
    
    pt = 0
    
    st.subheader('Appetizer')

    Appetizer1,Appetizer2,Appetizer3 = st.columns(3)

    with Appetizer1:
        if st.checkbox('Mozzarella Sticks: $4.99'):
            st.write('Added to cart')
            app1 = (4.99)

    with Appetizer2:
        if st.checkbox('Chicken Wings: $6.99'):
            app2 = (6.99)
            st.write('Sauce (FREE)')
            if st.checkbox('Barbeque'):
                st.write('Added to cart')
            if st.checkbox('Ketchup'):
                st.write('Added to cart')
            if st.checkbox('No Sauce'):
                st.write('Added to cart')

    with Appetizer3:
        if st.checkbox('Shrimps: $5.99'):
            st.write('Added to cart')
            app3 = (5.99)

    st.subheader('')

    st.subheader('Main Meals')

    meal1,meal2,meal3 = st.columns(3)

    with meal1:
        if st.checkbox('Bacon Burger: $9.99'):
            st.write('Added to cart')
            mea1 = (9.99)
        st.write('')
        if st.checkbox('Taco'):
            tacoa = st.number_input('Amount of Tacos:',2,8,2,2)
            st.write('2 tacos = $3.99')

            if tacoa == 2:
                st.write('Added to cart')
                mea111 = (3.99)
            elif tacoa == 4:
                st.write('Added to cart')
                mea111 = (7.98)
            elif tacoa == 6:
                st.write('Added to cart')
                mea111 = (11.97)   
            elif tacoa == 8:
                st.write('Added to cart')
                mea111 = (15.96)
            else:
                st.write('???')
            
    with meal2:
        if st.checkbox('Extra Pork Pizza'):
            if st.checkbox('X-Large: $18.99'):
                st.write('Added to cart')
                mea24 = (18.99)
            if st.checkbox('Large: $13.99'):
                st.write('Added to cart')
                mea21 = (13.99)
            if st.checkbox('Medium: $9.99'):
                st.write('Added to cart')
                mea22 = (9.99)
            if st.checkbox('Small: $5.99'):
                st.write('Added to cart')
                mea23 = (5.99)
        st.write('')
        if st.checkbox('Cheese Bacon Burger: $9.99'):
            st.write('Added to cart')
            mea222 = (9.99)

    with meal3:
        if st.checkbox('Hot Dog: $7.99'):
            st.write('Added to cart')
            mea3 = (7.99)
        st.write('')
        if st.checkbox('Chicken Bacon Burger: $9.99'):
            st.write('Added to cart')
            mea333 = (9.99)
    
    st.subheader('')

    st.subheader('Fruits')

    fruit1,fruit2,fruit3 = st.columns(3)

    with fruit1:
        if st.checkbox('Apples: $4.99'):
            st.write('Added to cart')
            fru1 = (4.99)

    with fruit2:
        if st.checkbox('Bananas: $4.99'):
            st.write('Added to cart')
            fru2 = (4.99)

    with fruit3:
        if st.checkbox('Oranges: $4.99'):
            st.write('Added to cart')
            fru3 = (4.99)

    st.subheader('')

    st.subheader('Desserts')

    dessert1,dessert2,dessert3 = st.columns(3)

    with dessert1:
        if st.checkbox('Ice cream: $6.99'):
            des1 = (6.99)
            if st.checkbox('Chocolate'):
                st.write('Added to cart')
            if st.checkbox('Vanilla'):
                st.write('Added to cart')
            if st.checkbox('Strawberry'):
                st.write('Added to cart')

    with dessert2:
        if st.checkbox('Cookie: $2.99'):
            st.write('Added to cart')
            des2 = (2.99)

    with dessert3:
        if st.checkbox('Cake: $14.99'):
            st.write('Customize your cake')
            des3 = (14.99)
            if st.checkbox('Icing: $2.49'):
                st.write('Cake Customized')
                des31 = (2.49)
            if st.checkbox('Cookies: $4.99'):
                st.write('Cake Customized')
                des32 = (4.99)
            if st.checkbox('Cream: $1.99'):
                st.write('Cake Customized')
                des33 = (1.99)
            if st.checkbox('Candles: $2.99'):
                st.write('Cake Customized')
                des34 = (2.99)
    
    st.subheader('')

    st.subheader('Drinks')

    drink1,drink2,drink3 = st.columns(3)

    with drink1:
        if st.checkbox('Milkshake: $9.99'):
            dri1 = (9.99)
            if st.checkbox(' Chocolate'):
                st.write('Added to cart')
            if st.checkbox(' Vanilla'):
                st.write('Added to cart')

    with drink2:
        if st.checkbox('Crush: $6.99'):
            dri2 = (6.99)
            if st.checkbox('Orange'):
                st.write('Added to cart')
            if st.checkbox('Cream Soda'):
                st.write('Added to cart')
            if st.checkbox('Grape'):
                st.write('Added to cart')

    with drink3:
        if st.checkbox('Lemonade: $9.99'):
            st.write('Added to cart')
            dri3 = (9.99)
    
    st.subheader('')

    st.subheader('Kids Menu')

    kids1,kids2,kids3 = st.columns(3)

    with kids1:
        if st.checkbox('Mini Bacon Burger: $4.99'):
            st.write('Added to cart')
            km1 = (4.99)
        
    with kids2:
        if st.checkbox('Pork Pizza: $4.99'):
            st.write('Added to cart')
            km2 = (4.99)
    
    with kids3:
        if st.checkbox('Mini Hot Dog: $4.99'):
            st.write('Added to cart')
            km3 = (4.99)
    
    st.subheader('')

    tax = 0

    if st.checkbox('Remove Pig Tax ($19.99)'):
        st.write('Pig Tax Removed')
        pt = (1)
        ptc = (19.99)

    subtotal = app1 + app2 + app3 + mea1 + mea111 + mea21 + mea22 + mea23 + mea24 + mea222 + mea3 + mea333 + fru1 + fru2 + fru3 + des1 + des2 + des3 + des31 + des32 + des33 + des34 + dri1 + dri2 + dri3 + km1 + km2 + km3 + ptc

    if subtotal < 5:
        tax = 0

    elif subtotal < 10:
        tax = 5

    elif subtotal < 15:
        tax = 10

    elif subtotal < 20:
        tax = 20

    elif subtotal < 25:
        tax = 30

    elif subtotal < 50:
        tax = 40

    elif subtotal < 65:
        tax = 50

    elif subtotal < 75:
        tax = 60

    elif subtotal < 85:
        tax = 70

    elif subtotal < 100:
        tax = 85

    elif subtotal < 125:
        tax = 100

    elif subtotal < 150:
        tax = 125

    elif subtotal < 175:
        tax = 150

    elif subtotal < 200:
        tax = 175

    elif subtotal > 200:
        tax = 200

    else:
        tax = 'Your Pig Tax is Unkown'




    if pt == 1:
        tax = 0

    total = subtotal + tax




    if st.button('Checkout'):
        st.write('Subtotal:',round(subtotal,2))
        st.write('Pig Tax:',tax)
        st.write('Total:',round(total,2))

        historydict = {'Subtotal':[subtotal],
                      'Pig Tax':[tax],
                      'Total':[total]}
        historytable = pd.DataFrame(historydict)
        tablesjoin = pd.concat([csvlink,historytable],ignore_index=True)
        tablesjoin.to_csv('peggycafe.csv',index=False)
    

if Menu == 'Other':
    st.title('Other')
    ViewPass = st.text_input('Enter Viewing Password:',type='password')
    
    if ViewPass == 'PeggyView':
        st.subheader('Latest Purchases:')
        st.table(csvlink)



