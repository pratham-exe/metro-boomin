import streamlit as st
from sqlalchemy import text

conn = st.connection("metro.db", type="sql", url="sqlite:///./metro.db")
session = conn.session
username = st.session_state['name']

st.write(username)

with st.expander("Ticket History"):
    tickets_list = session.execute(text("SELECT tickets FROM user WHERE user_name = :user_name"), {
        'user_name': st.session_state['name']
    }).fetchone()[0]
    if tickets_list is None:
        st.write("")
    else:
        tickets_list = tickets_list.split(',')
        for each_ticket in tickets_list:
            each_ticket_info = conn.query(f"SELECT source, destination, price FROM ticket WHERE ticket_id = '{each_ticket}'")
            source = each_ticket_info['source'].values[0]
            dest = each_ticket_info['destination'].values[0]
            price = each_ticket_info['price'].values[0]
            st.write(f"{source} - {dest} : {price}Rs")
