import streamlit as st 
import pandas as pd
import numpy as np

from src.totais import tot_1, tot_2, tot_3, tot_4, tot_5, tot_6
from src.row_2 import grafico001, grafico002
from src.row_3 import grafico31, grafico32

from streamlit_autorefresh import st_autorefresh


def set_dashboard():
    
    # st_autorefresh(interval=5000, limit=1, key='min')

    ### ----------------- row 1 -----------------
    st.markdown("### Totais de Mensagens")
    first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi, sixth_kpi = st.columns(6)

    with first_kpi: tot_1()
    with second_kpi:tot_2()
    with third_kpi: tot_3()
    with fourth_kpi:tot_4()
    with fifth_kpi: tot_5()
    with sixth_kpi: tot_6()
    
    ### ----------------- row 2 -----------------
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.markdown("### Chart Section: 1")

    first_chart, second_chart = st.columns(2)

    with first_chart:   grafico001()
    with second_chart:  grafico002()


    ### ----------------- row 3 -----------------
    st.markdown("### Chart Section: 2")

    first_chart, second_chart = st.columns(2)

    with first_chart: grafico31()
    with second_chart:grafico32()

    ### ----------------- row 4 -----------------

    ### ----------------- row 5 -----------------