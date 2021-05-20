#importing all libraries
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def main():
    #sidebar
    st.sidebar.header('COVID-19 DASHBOARD')
    pages = ['India Dashboard','State Dashboard','Testing Data Dashboard','Vaccination Data Dashboard']
    page_selected = st.sidebar.radio("Pages",pages,index=0)

    #state names to codes dictionary
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

    response = load_data_response()
    cov_states = load_cov_states()
    cov_states_daily = load_cov_daily()
    #page-1
    if page_selected == 'India Dashboard':
        st.header('India Dashboard')
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
        st.table(dataf[-1:])
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
        st.table(dataf[-1:])
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

    elif page_selected == 'State Dashboard':
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
            st.table(df_statewise[["Confirmed","Recovered","Deceased"]][-1:])
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
            st.table(df_daily)
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

    elif page_selected == 'Testing Data Dashboard':
        cov_tested = pd.DataFrame(response['tested'])
        cov_tested['updatetimestamp'] = pd.to_datetime(cov_tested['updatetimestamp'])
        cov_tested['dailyrtpcrsamplescollectedicmrapplication'] = pd.to_numeric(cov_tested['dailyrtpcrsamplescollectedicmrapplication'])
        cov_tested['dailyrtpcrsamplescollectedicmrapplication'] = cov_tested['dailyrtpcrsamplescollectedicmrapplication'].replace(r'\s+', np.nan, regex=True)
        cov_tested['dailyrtpcrsamplescollectedicmrapplication'] = cov_tested['dailyrtpcrsamplescollectedicmrapplication'].fillna(0)
        #figure object
        tested = go.Figure()
        tested.update_layout(height=500,width=800,legend_orientation="h",
            title="Daily RTPCR Samples Collected vs Daywise Trend")

        #displaying daily confirmed cases plot
        tested.add_trace(go.Bar(
                        x=cov_tested["testedasof"],
                        y=cov_tested["dailyrtpcrsamplescollectedicmrapplication"]))
        tested.update_yaxes(showgrid=False)
        tested.update_xaxes(showgrid=False)
        st.plotly_chart(tested,use_container_width=True)    

        cov_tested['totalrtpcrsamplescollectedicmrapplication'] = pd.to_numeric(cov_tested['totalrtpcrsamplescollectedicmrapplication'])
        cov_tested['totalrtpcrsamplescollectedicmrapplication'] = cov_tested['totalrtpcrsamplescollectedicmrapplication'].replace(r'\s+', np.nan, regex=True)
        cov_tested['totalrtpcrsamplescollectedicmrapplication'] = cov_tested['totalrtpcrsamplescollectedicmrapplication'].fillna(0)
        #figure object
        tested = go.Figure()
        tested.update_layout(height=500,width=800,legend_orientation="h",
            title="Total RTPCR Samples Collected vs Daywise Trend")

        #displaying daily confirmed cases plot
        tested.add_trace(go.Bar(
                        x=cov_tested["testedasof"],
                        y=cov_tested["totalrtpcrsamplescollectedicmrapplication"]))
        tested.update_yaxes(showgrid=False)
        tested.update_xaxes(showgrid=False)
        st.plotly_chart(tested,use_container_width=True)    

if __name__ == "__main__":
    main()




