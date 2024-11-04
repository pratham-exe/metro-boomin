import streamlit as st

conn = st.connection("metro.db", type="sql", url="sqlite:///./metro.db")

stations = conn.query("SELECT station_name FROM station")["station_name"].to_list()
source = st.selectbox("From", stations)
destination = st.selectbox("To", stations)

if(source == destination):
    st.write("Destination cannot be same as Source")
else:

