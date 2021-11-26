import streamlit as st
import pandas as pd
import numpy as np

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

import json
import os
import sys

# funcao para listar todos os dados
def search_all(es_object, index_name):  
    search_param = {"query": {"match_all": {}}}
    try:
        res = es_object.search(index=index_name, body=search_param)
        # print("Got %d Hits:" % res['hits']['total']['value'])
        result = []
        for hit in res['hits']['hits']:
            # print(hit['_source'])
            result = hit['_source']
        return result
    except Exception as ex:
        print('Index no encontrado')
        print(str(ex))

# funcao para verificar e conecta no elastic search
def connect_elasticsearch(es_host, es_port):
    host=es_host
    try:
        _es = Elasticsearch([{'host': host, 'port': es_port}])
    except Exception as ex:
        print(str(ex))

    if _es.ping():
        print('Host:[{}] Conectado...!'.format(host))
    else:
        print('não pode Conectar ao host: [{}] ...'.format(host))
    return _es

es_conn = connect_elasticsearch('192.168.0.144', 9200) 

try:
    if es_conn:
        data = search_all(es_conn, 'msg_notificacoes_dia')
        print( { "status": True, "mensagem": ' hello!' } )
        pd.DataFrame(data)
except Exception as ex:
    msg={
        "status": False,
        "mensagem": 'Verifique conecão com elasticsearch!',
        "err": str(ex)
    }
    print(msg)

# -----------------------------------------
col1, col2, col3 = st.columns(3)
with col1:
    st.title('Uber pickups in NYC')

    DATE_COLUMN = 'date/time'
    DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
                'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

    @st.cache
    def load_data(nrows):
        data = pd.read_csv(DATA_URL, nrows=nrows)
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis='columns', inplace=True)
        data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
        return data

    data_load_state = st.text('Loading data...')
    data = load_data(10000)
    data_load_state.text("Done! (using st.cache)")

    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(data)

    st.subheader('Number of pickups by hour')
    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)

    # Some number in the range 0-23
    hour_to_filter = st.slider('hour', 0, 23, 17)
    filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

    st.subheader('Map of all pickups at %s:00' % hour_to_filter)
    st.map(filtered_data)

with col2:
    st.title('hello worl2')
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.title('hello worl3')
    st.image("https://static.streamlit.io/examples/owl.jpg")