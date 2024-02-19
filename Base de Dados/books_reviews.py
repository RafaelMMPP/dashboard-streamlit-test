import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
st.write('REVIEWS')


df_reviews = pd.read_csv('Base de Dados/customer reviews.csv')
df_top100_books = pd.read_csv('Base de Dados/Top-100 Trending Books.csv')

books = df_top100_books['book title'].unique()
book = st.sidebar.selectbox('Books', books)

df_book = df_top100_books[df_top100_books['book title']==book]
df_reviews_filtrado = df_reviews[df_reviews['book name']==book]

df_book
df_reviews_filtrado
