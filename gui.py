import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

conn = st.connection("metro_db", type="sql")
df = conn.query("select * from route")

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['expiry_days']
)

try:
    authenticator.login()
except Exception as e:
    st.error(e)

if st.session_state['authentication_status']:
    st.write(f'Welcome *{st.session_state["name"]}*')
    
    
else:
    try:
        email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user()
        if email_of_registered_user:
            st.success('User registered successfully')
            with open('config.yaml', 'w') as file:
                yaml.dump(config, file, default_flow_style=False)
    except Exception as e:
        st.error(e)

