import streamlit as st
from sqlalchemy import text

conn = st.connection("metro.db", type="sql", url="sqlite:///./metro.db")
session = conn.session

st.header("Create a New Train")

last_train = session.execute(text("SELECT train_id FROM train ORDER BY train_id DESC LIMIT 1")).fetchone()[0]

routes = 

st.selectbox("Select Route")

