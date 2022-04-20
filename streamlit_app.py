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
     sipr_date = Heger.get("1")
     cnet_date = Heger.get("2")


st.title('Login Expirations')

with st.container():
     st.header('SIPR')
     
     if not sipr_date:
          sipr_button = st.button("Enter New Login Date")

          if sipr_button:
               sipr_date = st.date_input(label="Enter Last Login", value=None, key=1)

               if sipr_date:
                    Heger.put({"SIPR": str(sipr_date), "key": "1"})
     if sipr_date:
          st.write("Last Login: " + str(sipr_date["SIPR"]))



     st.header('CNET')
    
     if not cnet_date:
          cnet_button = st.button("Enter New Login Date")

          if cnet_button:
               cnet_date = st.date_input(label='Enter Last Login', value=None, key=2)

               if cnet_date:
                    Heger.put({"CNET": str(cnet_date), "key": "2"})

     if cnet_date:
          st.write("Last Login: " + str(cnet_date["CNET"]))

