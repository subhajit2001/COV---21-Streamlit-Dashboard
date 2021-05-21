import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from pages import load

response = load.load_data_response()

def india_elements():
        st.title('India Dashboard')
        st.subheader('Count of Daily Confirmed, Recovered and Deceased Cases')
        #daily data
        cov_daily = pd.DataFrame(response["cases_time_series"])
        #converting the column data types to proper data types
        cov_daily["dailyconfirmed"] = pd.to_numeric(cov_daily["dailyconfirmed"])
        cov_daily["dateymd"] = pd.to_datetime(cov_daily["dateymd"])
        cov_daily["dailyrecovered"] = pd.to_numeric(cov_daily["dailyrecovered"])
        cov_daily["dailydeceased"] = pd.to_numeric(cov_daily["dailydeceased"])
        dataf = cov_daily[["dailyconfirmed","dailyrecovered","dailydeceased"]]
        dataf.drop(dataf.columns[0],axis=1)
        st.table(dataf[-1:].assign(hack='').set_index('hack'))
        #figure object
        fig = go.Figure()
        fig.update_layout(height=500,width=800,legend_orientation="h",
                            title="Daily Cases vs Daywise Pattern")
        #displaying daily confirmed cases plot
        fig.add_trace(go.Scatter(
                    x=cov_daily["dateymd"],
                    y=cov_daily["dailyconfirmed"],
                    name="Daily Confirmed",
                    mode="lines+markers"))
        fig.add_trace(go.Scatter(
                    x=cov_daily["dateymd"],
                    y=cov_daily["dailyrecovered"],
                    name="Daily Recovered",
                    mode="lines+markers"))
        fig.add_trace(go.Scatter(
                    x=cov_daily["dateymd"],
                    y=cov_daily["dailydeceased"],
                    name="Daily Deceased",
                    mode="lines+markers"))
        fig.update_yaxes(showgrid=False)
        fig.update_xaxes(showgrid=False)
        st.plotly_chart(fig,use_container_width=True)
        #converting the column data types to proper data types
        st.subheader("Count of Total Confirmed, Recovered, Deceased")
        cov_daily["totalconfirmed"] = pd.to_numeric(cov_daily["totalconfirmed"])
        cov_daily["dateymd"] = pd.to_datetime(cov_daily["dateymd"])
        cov_daily["totalrecovered"] = pd.to_numeric(cov_daily["totalrecovered"])
        cov_daily["totaldeceased"] = pd.to_numeric(cov_daily["totaldeceased"])
        dataf = cov_daily[["totalconfirmed","totalrecovered","totaldeceased"]]
        dataf.drop(dataf.columns[0],axis=1)
        st.table(dataf[-1:].assign(hack='').set_index('hack'))
        #figure object
        fig = go.Figure()
        fig.update_layout(height=500,width=800,legend_orientation="h",
                            title="Total Cases vs Daywise Pattern")
        #displaying daily confirmed cases plot
        fig.add_trace(go.Scatter(
                    x=cov_daily["dateymd"],
                    y=cov_daily["totalconfirmed"],
                    name="Total Confirmed",
                    mode="lines+markers"))
        fig.add_trace(go.Scatter(
                    x=cov_daily["dateymd"],
                    y=cov_daily["totalrecovered"],
                    name="Total Recovered",
                    mode="lines+markers"))
        fig.add_trace(go.Scatter(
                    x=cov_daily["dateymd"],
                    y=cov_daily["totaldeceased"],
                    name="Total Deceased",
                    mode="lines+markers"))
        fig.update_yaxes(showgrid=False)
        fig.update_xaxes(showgrid=False)
        st.plotly_chart(fig,use_container_width=True)
    