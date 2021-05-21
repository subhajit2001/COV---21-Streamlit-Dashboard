import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from pages import load


states_dict = {
        'AP':'Andhra Pradesh',
        'AR':'Arunachal Pradesh',
        'AS':'Assam',
        'BR':'Bihar',
        'CT':'Chhattisgarh',
        'GA':'Goa',
        'GJ':'Gujarat',
        'HR':'Haryana',
        'HP':'Himachal Pradesh',
        'JK':'Jammu and Kashmir',
        'JH':'Jharkhand',
        'KA':'Karnataka',
        'KL':'Kerala',
        'LA':'Ladakh',
        'MP':'Madhya Pradesh',
        'MH':'Maharashtra',
        'MN':'Manipur',
        'ML':'Meghalaya',
        'MZ':'Mizoram',
        'NL':'Nagaland',
        'OR':'Odisha',
        'PB':'Punjab',
        'RJ':'Rajasthan',
        'SK':'Sikkim',
        'TG':'Telangana',
        'TN':'Tamil Nadu',
        'TR':'Tripura',
        'UK':'Uttarakhand',
        'UP':'Uttar Pradesh',
        'UT':'Uttarakhand',
        'WB':'West Bengal',
        'TN':'Tamil Nadu',
        'TR':'Tripura',
        'AN':'Andaman and Nicobar Islands',
        'CH':'Chandigarh',
        'DN':'Dadra and Nagar Haveli and Daman and Diu',
        'DD':'Daman and Diu',
        'DL':'Delhi',
        'LD':'Lakshadweep',
        'PY':'Pondicherry'
    }

def state_elements():
        cov_states = load.load_cov_states()
        cov_states_daily = load.load_cov_daily()        
        #heading
        st.header('States Dashboard')
        #states list
        states = np.array(cov_states['State'].unique())
        states = np.delete(states,[1,36])
        #Selectbox of states
        state_selected = st.selectbox("Select State to Show Statewise Data",states,index=0)

        if state_selected:
            df_statewise = cov_states[cov_states["State"]==state_selected]
            #subheading
            st.subheader('Total Cases Category wise as per present day')
            st.table(df_statewise[["Confirmed","Recovered","Deceased"]][-1:].assign(hack='').set_index('hack'))
            df_statewise["Date"] = pd.to_datetime(df_statewise["Date"])
            #figure object
            state = go.Figure()
            state.update_layout(height=500,width=800,legend_orientation="h",
            title="Total Cases vs Daywise Trend")

            #displaying daily confirmed cases plot
            state.add_trace(go.Scatter(
                        x=df_statewise["Date"],
                        y=df_statewise["Confirmed"],
                        name="Daily Confirmed",
                        mode="lines+markers"))
            state.add_trace(go.Scatter(
                        x=df_statewise["Date"],
                        y=df_statewise["Recovered"],
                        name="Daily Recovered",
                        mode="lines+markers"))
            state.add_trace(go.Scatter(
                        x=df_statewise["Date"],
                        y=df_statewise["Deceased"],
                        name="Daily Deceased",
                        mode="lines+markers"))
            state.update_yaxes(showgrid=False)
            state.update_xaxes(showgrid=False)
            st.plotly_chart(state,use_container_width=True)
        #converting the column data types to proper data types
        cov_states_daily['Date_YMD'] = pd.to_datetime(cov_states_daily['Date_YMD'])
        #renaming columns
        cov_states_daily = cov_states_daily.rename(columns=states_dict)
        
        if state_selected:
            df_confirmed = cov_states_daily[cov_states_daily["Status"]=='Confirmed']
            df_recovered = cov_states_daily[cov_states_daily["Status"]=='Recovered']
            df_deceased = cov_states_daily[cov_states_daily["Status"]=='Deceased']
            df_state_confirmed = df_confirmed[[state_selected,'Date_YMD']]
            df_state_recovered = df_recovered[[state_selected,'Date_YMD']]
            df_state_deceased = df_deceased[[state_selected,'Date_YMD']]
            #dictionary
            st.subheader('Daily Cases Category wise as per present day')
            dict_daily={
                'Daily Confirmed':np.array(df_state_confirmed[[state_selected]])[-1],
                'Daily Recovered':np.array(df_state_recovered[[state_selected]])[-1],
                'Daily Deceased':np.array(df_state_deceased[[state_selected]])[-1]
            }
            df_daily = pd.DataFrame.from_dict(dict_daily)
            #df_daily = df_daily.reset_index(drop=True).set_index('Daily Confirmed')
            #df_daily.index.name='Daily Confirmed'
            st.table(df_daily.assign(hack='').set_index('hack'))
            #figure object
            state = go.Figure()
            state.update_layout(height=500,width=800,legend_orientation="h",
            title="Daily Cases vs Daywise Trend")

            #displaying daily confirmed cases plot
            state.add_trace(go.Scatter(
                        x=df_state_confirmed["Date_YMD"],
                        y=df_state_confirmed[state_selected],
                        name="Daily Confirmed",
                        mode="lines+markers"))
            state.add_trace(go.Scatter(
                        x=df_state_recovered["Date_YMD"],
                        y=df_state_recovered[state_selected],
                        name="Daily Recovered",
                        mode="lines+markers"))
            state.add_trace(go.Scatter(
                        x=df_state_deceased["Date_YMD"],
                        y=df_state_deceased[state_selected],
                        name="Daily Deceased",
                        mode="lines+markers"))
            state.update_yaxes(showgrid=False)
            state.update_xaxes(showgrid=False)
            st.plotly_chart(state,use_container_width=True)
