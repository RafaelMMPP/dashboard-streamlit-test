import streamlit as st
import pandas as pd
import numpy as np 

st.title('UBER PICKSUPS IN NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("DONE You motherfucker !! ")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data) #  st.write renderizará quase tudo o que você passar a ele. Nesse caso, você está passando um dataframe e ele está sendo 
# renderizado como um mesa interativa. O st.write tenta fazer a coisa certa com base em no tipo de dados da entrada. 
# Se ele não está fazendo o que você espera, você pode usar um comando especializado como st.dataframe em vez disso. NESSE CASO ESPECÍFICO EU PERCEBI QUE 
# TBM PODE APENAS DEIXAR A VARIÁVEL data ESCRITA SOLTA, QUE RENDERIZA DO MESMO JEITO. 

st.subheader('Number of pickups by hour')

hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

st.subheader('Map of all pickups')

hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h

filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)













