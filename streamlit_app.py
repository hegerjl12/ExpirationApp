import streamlit as st

st.set_page_config(
     page_title="Login Expirations",
     page_icon="🔒",
     layout="wide",
     initial_sidebar_state="expanded",
)

st.title('Login Expirations')

with st.container():
    st.header('SIPR')
    
    sipr_date = st.date_input(label='Enter Last Login')