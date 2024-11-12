import streamlit as st
from sqlalchemy import text

conn = st.connection("metro.db", type="sql", url="sqlite:///./metro.db")
session = conn.session

users = session.execute(text("SELECT user_name FROM user WHERE admin = :admin"), {
    'admin': 'False'
}).fetchall()

st.header("Users")
for each_user in users:
    with st.expander(f"{each_user[0]}"):
        tickets_list = session.execute(text("SELECT tickets FROM user WHERE user_name = :user_name"), {
            'user_name': each_user[0]
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
