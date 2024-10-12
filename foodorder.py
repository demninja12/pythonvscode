import streamlit as st
import pandas as pd

st.set_page_config(page_title='Peggy Cafe',page_icon='☕')

csvlink = pd.read_csv('peggycafe.csv')

Menu = st.sidebar.selectbox('Menu',['Order','History'])

if Menu == 'Order':

    st.title('Peggy Cafe')

    st.image('https://d1csarkz8obe9u.cloudfront.net/posterpreviews/fast-food-banner-template-design-925774928d842fc1ac0186b839a10444_screen.jpg?ts=1689218877')

    app1 = 0
    app2 = 0
    app3 = 0
    mea1 = 0
    mea21 = 0
    mea22 = 0
    mea23 = 0
    mea24 = 0
    mea3 = 0
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
    fea = 0
    ptc = 0
    cyo1 = 0
    cyo11 = 0
    cyo12 = 0
    cyo13 = 0
    cyo14 = 0
    cyo15 = 0
    cyo16 = 0
    cyo17 = 0

    pt = 0

    st.subheader('Appetizer')

    Appetizer1,Appetizer2,Appetizer3 = st.columns(3)

    with Appetizer1:
        if st.checkbox('Mozzarella Sticks: $6.99'):
            st.write('Added to cart')
            app1 = (6.99)

    with Appetizer2:
        if st.checkbox('Chicken Wings: $9.99'):
            app2 = (9.99)
            st.write('Sauce (FREE)')
            if st.checkbox('Barbeque'):
                st.write('Added to cart')
            if st.checkbox('Ketchup'):
                st.write('Added to cart')
            if st.checkbox('No Sauce'):
                st.write('Added to cart')

    with Appetizer3:
        if st.checkbox('Shrimps on a Stick: $6.99'):
            st.write('Added to cart')
            app3 = (6.99)

    st.subheader('')

    st.subheader('Main Meals')

    meal1,meal2,meal3 = st.columns(3)

    with meal1:
        if st.checkbox('Giant Pork Burger: $14.99'):
            st.write('Added to cart')
            mea1 = (14.99)
            

    with meal2:
        if st.checkbox('Extra Pork Pizza'):
            if st.checkbox('X-Large: $24.99'):
                st.write('Added to cart')
                mea24 = (24.99)
            if st.checkbox('Large: $19.99'):
                st.write('Added to cart')
                mea21 = (19.99)
            if st.checkbox('Medium: $14.99'):
                st.write('Added to cart')
                mea22 = (14.99)
            if st.checkbox('Small: $9.99'):
                st.write('Added to cart')
                mea23 = (9.99)

    with meal3:
        if st.checkbox('Pork Hot Dog: $9.99'):
            st.write('Added to cart')
            mea3 = (9.99)
    


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
        if st.checkbox('ice cream: $6.99'):
            des1 = (6.99)
            if st.checkbox('Chocolate'):
                st.write('Added to cart')
            if st.checkbox('Vanilla'):
                st.write('Added to cart')
            if st.checkbox('Strawberry'):
                st.write('Added to cart')

    with dessert2:
        if st.checkbox('Cookie: $4.99'):
            st.write('Added to cart')
            des2 = (4.99)

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
    
    st.subheader('Create Your Own')

    create1,create2,create3 = st.columns(3)

    with create1:
        if st.checkbox('Burger: $5.99'):
            st.write('')
            cyo1 = (5.99)
            if st.checkbox('Bun: $0.25'):
                st.write('Added to burger')
                cyo11 = (0.25)
            if st.checkbox('Patty: $1.49'):
                st.write('Added to burger')
                cyo12 = (1.49)
            if st.checkbox('Bacon: $1.99'):
                st.write('Added to burger')
                cyo13 = (1.99)
            if st.checkbox('Lettuce: $0.99'):
                st.write('Added to burger')
                cyo14 = (0.99)
            if st.checkbox('Tomato: $1.49'):
                st.write('Added to burger')
                cyo15 = (1.49)
            if st.checkbox('Cheese: $0.99'):
                st.write('Added to burger')
                cyo16 = (0.99)
            if st.checkbox('Pickles: $0.99'):
                st.write('Added to burger')
                cyo17 = (0.99)
            if st.checkbox('Ketchup: FREE'):
                st.write('Added to burger')

    st.title(' ')
    st.subheader('Feastables')
    if st.checkbox('Buy Feastables: $2.99'):
        fea = (2.99)
        if st.checkbox('Milk Chocolate'):
            st.write('Added to cart')
        if st.checkbox('Milk Crunch'):
            st.write('Added to cart')
        if st.checkbox('Almond'):
            st.write('Added to cart')
        if st.checkbox('Dark Chocolate'):
            st.write('Added to cart')
        if st.checkbox('Dark Chocolate Sea Salt'):
            st.write('Added to cart')
        if st.checkbox('Peanut Butter'):
            st.write('Added to cart')
        if st.checkbox('Peanut Butter Crunch'):
            st.write('Added to cart')
        if st.checkbox('Cookies & Cream'):
            st.write('Added to cart')
    
    st.title('')

    if st.checkbox('Sign In'):
        name = st.text_input('Enter your name: ')

    st.title('')#spacer

    tax = 0

    if st.checkbox('Remove Pig Tax ($19.99)'):
        st.write('Pig Tax Removed')
        pt = (1)
        ptc = (19.99)

    subtotal = app1 + app2 + app3 + mea1 + mea21 + mea22 + mea23 + mea24 + mea3 + fru1 + fru2 + fru3 + des1 + des2 + des3 + des31 + des32 + des33 + des34 + dri1 + dri2 + dri3 + cyo1 + cyo11 + cyo12 + cyo13 + cyo14 + cyo15 + cyo16 + cyo17 + fea + ptc

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

        historydict = {'Name':[name],
                       'Subtotal':[subtotal],
                      'Pig Tax':[tax],
                      'Total':[total]}
        historytable = pd.DataFrame(historydict)
        tablesjoin = pd.concat([csvlink,historytable],ignore_index=True)
        tablesjoin.to_csv('peggycafe.csv',index=False)
    

if Menu == 'History':
    ViewPass = st.text_input('Enter Viewing Password:',type='password')

    if ViewPass == 'PeggyView':
        if st.button('View History'):
            st.table(csvlink)

