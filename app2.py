import streamlit as st
import pandas as pd
import plotly as pl
import plotly.express as px
import plotly.validators as pv


st.set_page_config(layout='wide')

df_reviews = pd.read_csv('Base de Dados/customer reviews.csv')
df_top100_books = pd.read_csv('Base de Dados/Top-100 Trending Books.csv')

price_max = df_top100_books['book price'].max() # O COLCHETE PODE SER INTERPRETADO COMO DIZENDO "QUANDO"
price_min = df_top100_books['book price'].min()

max_price = st.sidebar.slider('Price Range', price_min, price_max, price_max) # mas só isso não faz o slider ficar ativo, tem que definir uma variável para ele. 
# dai criar a variável associada no exemplo, max_price 

df_books = df_top100_books[df_top100_books['book price'] <= max_price]
df_books # DEIXANDO SOLTO ASSIM O STREMLIT ENTENDE QUE TEM QUE PRINTAR NA TELA 




