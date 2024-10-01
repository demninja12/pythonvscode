import streamlit as st

#Data collections: used when you want to save multiple in a variable

#list by the square bracets
restaurantlist = ['McDonalds','KFC','Burger King','DQ','A & W']

#Dictionary:
#can help save items in different categories

#a list is good when you want to group items and choose one from items
#but dictionary when you want to put items in categories and also create a table
MostBoughtFoods = ['McDonalds',10,20,30]

st.write(MostBoughtFoods)


MostBoughtFoodsDict = {'Restaurant':'McDonalds','Burger':50,'McNuggets':25,'Fries':10}

st.write(MostBoughtFoodsDict)

st.table(MostBoughtFoodsDict)


#write this out with your own examples. include all comments too and run your code