import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning')

st.write('This app builds a Machine learning model.')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
df

st.write('**X**')
X = df.drop('species', axis =1)
X

st.write('**y**')
y= df.species
y

with st.expander('data Visualization'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g',color='species')

# Data preparations
with st.sidebar:
  st.header('Input features')
  "","bill_depth_mm","flipper_length_mm","body_mass_g"
  island = st.selectbox('Island', ('Biscoe','Dream','Torgerson'))
  gender = st.selectbox('Gender', ('male','female'))
  bill_length_mm = st.slider('Bill length (mm)',32.1, 59.6, 43.9)
