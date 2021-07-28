import streamlit as st
#sidebar
def sidebar_elements():
    st.sidebar.title('COVID-19 DASHBOARD')
    pages = ['Home','Country Dashboard','India Dashboard','State Dashboard','Testing Data Dashboard']
    page_selected = st.sidebar.radio("Navigate",pages,index=0)
    st.sidebar.subheader("About Me")
    st.sidebar.info(
        """
        This app is maintained by Subhajit Saha. You can learn more about me at
        [subhajitsaha.netlify.app](https://subhajitsaha.netlify.app).
        """)
    st.sidebar.subheader("Contribute and Disclaimer")
    st.sidebar.info(
        """
        Feel free to contribute to this open source project.
        The github link can be found [here](https://github.com/subhajit2001/Cov-19-Analytics-Dashboard). 
        """
    )
    return page_selected
