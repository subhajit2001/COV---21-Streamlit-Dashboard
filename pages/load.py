import streamlit as st
import pandas as pd
import requests

#loading cache data
@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def load_data_response():
    #importing the daily time-series data
    response = requests.get("https://api.covid19india.org/data.json").json()
    return response
@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def load_cov_states():
    #daily data
    cov_states = pd.read_csv("https://api.covid19india.org/csv/latest/states.csv")
    return cov_states
@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def load_cov_daily():
    #daily data
    cov_states_daily = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
    return cov_states_daily
