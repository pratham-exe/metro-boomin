import streamlit as st

if st.button("Logout"):
    st.session_state.logged_in = False
    st.session_state['authentication_status'] = False
    st.rerun()
