import streamlit as st

st.write("Emily saved $150. She decided to spend some of her savings on different items. First, she bought a book. Then, she purchased some snacks. After that, she saw a toy she liked and bought it. She also needed to take a taxi ride to get home, and finally, she spent some money on a game. Write a Python program to calculate how much money Emily has left after her expenses. Use an if condition to tell her if she still has money saved or if she spent more than she saved.")

savings = 150
st.write("you saved",savings,'dollars')
book_cost = 12
st.write('you spent',book_cost,'dollars on books')
snack_cost = 65
st.write('you spent',snack_cost,'dollars on snacks')
toy_cost = 48
st.write('you spent',toy_cost,'dollars on toys')
taxi_cost = 91
st.write = ('you spent',taxi_cost,'dollars on toys')
game_cost = 19
st.write = ('you spent',game_cost,'dollars on games')
total = book_cost + snack_cost + toy_cost + taxi_cost + game_cost

amount_remaining = total - savings

if amount_remaining > 0:
    st.write('you have',amount_remaining,'dollars left')
else:
    st.write('you spent more than your savings')