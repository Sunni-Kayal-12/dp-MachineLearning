import streamlit as st

st.title('🤖 Machine Learning')

st.write('This app builds a Machine learning model.')

df = pd.read_csv('https://github.com/dataprofessor/data/edit/master/penguins_cleaned.csv')
df
