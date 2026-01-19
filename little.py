import streamlit as st
import pandas as pd

st.title("My First Streamlit App")
st.write("Hello, *world!*")

# Load and display data
df = pd.DataFrame({
"Category": ["A", "B", "C"],
"Values": [10, 20, 30]
})
st.bar_chart(df)

# Add interactivity
number = st.slider("Pick a number", 0, 100)
st.write(f"You selected: {number}")