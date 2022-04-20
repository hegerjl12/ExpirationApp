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
    
     sipr_date = st.date_input(label='Enter Last Login', key=1)

     if sipr_date:
          st.write(sipr_date)
          Heger.put({"SIPR": str(sipr_date), "key": "1"})



     st.header('CNET')
    
     cnet_date = st.date_input(label='Enter Last Login', value=None, key=2)

     if cnet_date:
          st.write(cnet_date)
          Heger.put({"CNET": str(cnet_date), "key": "2"})

