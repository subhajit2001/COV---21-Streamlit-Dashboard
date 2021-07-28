import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from pages import load

def test():
        response = load.load_data_response()
        cov_tested = pd.DataFrame(response['tested'])
        cov_tested['updatetimestamp'] = pd.to_datetime(cov_tested['updatetimestamp'])
        cov_tested['dailyrtpcrsamplescollectedicmrapplication'] = pd.to_numeric(cov_tested['dailyrtpcrsamplescollectedicmrapplication'])
        cov_tested['dailyrtpcrsamplescollectedicmrapplication'] = cov_tested['dailyrtpcrsamplescollectedicmrapplication'].replace(r'\s+', np.nan, regex=True)
        cov_tested['dailyrtpcrsamplescollectedicmrapplication'] = cov_tested['dailyrtpcrsamplescollectedicmrapplication'].fillna(0)
        #figure object
        st.markdown("## Testing Data Visualization")
        st.markdown("### Daily RT-PCR Samples Collected")
        tested = go.Figure()
        tested.update_layout(height=500,width=800,legend_orientation="h",title="Daywise Trend")

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
        st.markdown("### Total RT-PCR Samples Collected")
        tested = go.Figure()
        tested.update_layout(height=500,width=800,legend_orientation="h",
            title="Daywise Trend")

        #displaying daily confirmed cases plot
        tested.add_trace(go.Bar(
                        x=cov_tested["testedasof"],
                        y=cov_tested["totalrtpcrsamplescollectedicmrapplication"]))
        tested.update_yaxes(showgrid=False)
        tested.update_xaxes(showgrid=False)
        st.plotly_chart(tested,use_container_width=True)    
