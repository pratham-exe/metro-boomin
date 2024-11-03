import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.title("OUR METRO")

login_page = st.Page("auth/login.py", title="Log in", icon=":material/login:")
register_page = st.Page("auth/register.py", title="Register", icon=":material/login:")
logout_page = st.Page("user/logout.py", title="Log out", icon=":material/logout:")
dashboard_page = st.Page("user/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True)
routes_page = st.Page("user/routes.py", title="Routes")
station_page = st.Page("user/station.py", title="Station")
ticket_page = st.Page("user/ticket.py", title="Ticket")

if st.session_state.logged_in:
    pg = st.navigation({"Account": [logout_page, dashboard_page, routes_page, station_page, ticket_page]})
else:
    pg = st.navigation({"Authorize": [login_page, register_page]})
pg.run()
