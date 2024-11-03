import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['expiry_days']
)

try:
    authenticator.login()
    if st.session_state['authentication_status']:
        st.success("User logged in successfully")
        st.session_state.logged_in = True
except Exception as e:
    st.error(e)
