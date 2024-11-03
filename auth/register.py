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
    email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user()
    if email_of_registered_user:
        st.success('User registered successfully')
        st.session_state.logged_in = True
        with open('config.yaml', 'w') as file:
            yaml.dump(config, file, default_flow_style=False)
except Exception as e:
    st.error(e)
