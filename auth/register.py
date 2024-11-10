import streamlit as st
import streamlit_authenticator as stauth
import yaml
from sqlalchemy import text
from yaml.loader import SafeLoader

conn = st.connection("metro.db", type="sql", url="sqlite:///./metro.db")

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

query = text("INSERT INTO user (user_id, user_name, admin) VALUES (:user_id, :user_name, :admin);")

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['expiry_days']
)

try:
    email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user()
    if email_of_registered_user:
        st.success('User registered successfully')
        st.session_state.logged_in = True
        st.session_state.admin = False
        st.session_state['name'] = name_of_registered_user
        with conn.session as session:
            session.execute(query, {
                'user_id': username_of_registered_user,
                'user_name': name_of_registered_user,
                'admin': 'False'
            })
            session.commit()
        with open('config.yaml', 'w') as file:
            yaml.dump(config, file, default_flow_style=False)
except Exception as e:
    st.error(e)
