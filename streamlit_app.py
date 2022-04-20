import streamlit as st
from deta import Deta

st.set_page_config(
     page_title="Login Expirations",
     page_icon="🔒",
     layout="wide",
     initial_sidebar_state="expanded",
)

# connect to databases
with st.spinner("Connecting to database..."):
     deta = Deta(st.secrets["deta_key"])
     Heger = deta.Base("Heger")


st.title('Login Expirations')

with st.container():
     st.header('SIPR')
    
     sipr_date = st.date_input(label='Enter Last Login')

     Heger.put({"SIPR": str(sipr_date), "key": 1})

     