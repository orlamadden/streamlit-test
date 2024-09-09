import streamlit as st
import pandas as pd

st.title('My First Streamlit App')

st.write("Hello, welcome to my first Streamlit app!")

# Create a sample dataframe
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40],
    'C': [100, 200, 300, 500]
})

st.write("Here is a sample dataframe:")
st.dataframe(df)
