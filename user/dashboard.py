import streamlit as st
from sqlalchemy import text

conn = st.connection("metro.db", type="sql", url="sqlite:///./metro.db")
session = conn.session
username = st.session_state['name']


def calculate_total_money_spent_by_user(user_name):
    aggregate_query = f"""
    SELECT SUM(t.price) AS total_spent
    FROM ticket t
    JOIN (
        SELECT user_id, user_name, tickets
        FROM user
        WHERE user_name = '{user_name}'
    ) u ON ',' || u.tickets || ',' LIKE '%,' || t.ticket_id || ',%';
    """
    result = session.execute(text(aggregate_query)).fetchone()
    total_spent = result[0] if result else 0
    return total_spent


total_money_spent_on_metro = calculate_total_money_spent_by_user(username)

st.write(username)
st.write(f"Money spent: {total_money_spent_on_metro}Rs")

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
