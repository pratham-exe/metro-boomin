import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)


conn = st.connection("metro.db", type="sql", url="sqlite:///./metro.db")

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['expiry_days']
)

try:
    authenticator.login()
    if st.session_state['authentication_status']:
        user_privilege = conn.query(f"SELECT admin FROM user WHERE user_id = '{st.session_state['username']}'")['admin'][0]
        st.session_state.logged_in = True
        if user_privilege == 'False':
            st.session_state.admin = False
            st.success("User logged in successfully")
        else:
            st.session_state.admin = True
            st.success("Admin logged in successfully")

except Exception as e:
    st.error(e)
