import streamlit as st

conn = st.connection("metro.db", type="sql", url="sqlite:///./metro.db")

stations = conn.query("SELECT station_name FROM station")["station_name"].to_list()
option = st.selectbox("From", stations)
option = st.selectbox("To", stations)
