import streamlit as st 
import pandas as pd
import numpy as np

def randomize():
    x = np.random.randint(100)
    return x

def tot_1():
    st.markdown("**KPI**")
    
    number1 = randomize()
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number1}</h1>", unsafe_allow_html=True)

def tot_2():
    st.markdown("**KPI**")
    number1 = randomize()
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number1}</h1>", unsafe_allow_html=True)

def tot_3():
    st.markdown("**KPI**")
    number1 = randomize() 
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number1}</h1>", unsafe_allow_html=True)

def tot_4():
    st.markdown("**KPI**")
    number1 = randomize() 
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number1}</h1>", unsafe_allow_html=True)

def tot_5():
    st.markdown("**KPI**")
    number1 = randomize() 
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number1}</h1>", unsafe_allow_html=True)

def tot_6():
    st.markdown("**KPI**")
    number1 = randomize()
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number1}</h1>", unsafe_allow_html=True)
