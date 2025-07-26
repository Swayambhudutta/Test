
import streamlit as st
import random

st.title("🎲 Dice Roll Simulator")

st.write("Click the button below to roll the dice!")

if st.button("Roll the Dice"):
    dice_value = random.randint(1, 6)
    st.write(f"You rolled a **{dice_value}**!")
    st.image(f"https://raw.githubusercontent.com/streamlit/example-data/master/dice/dice{dice_value}.png", width=150)
