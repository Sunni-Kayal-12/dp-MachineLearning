import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning')

st.write('This app builds a Machine learning model.')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
df
