import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.title("NIMMA METRO")

# User Pages
login_page = st.Page("auth/login.py", title="Log in", icon=":material/login:")
register_page = st.Page("auth/register.py", title="Register", icon=":material/login:")
logout_page = st.Page("user/logout.py", title="Log out", icon=":material/logout:")
dashboard_page = st.Page("user/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True)
routes_page = st.Page("user/routes.py", title="Routes")
station_page = st.Page("user/station.py", title="Station")
ticket_page = st.Page("user/ticket.py", title="Ticket")

# Admin Pages
station_management = st.Page("admin/station_management.py", title="Station Management")
route_management = st.Page("admin/route_management.py", title="Route Management")
schedule_management = st.Page("admin/schedule_management.py", title="Schedule Management")
train_management = st.Page("admin/train_management.py", title="Train Management")
dashboard_admin = st.Page("admin/dashboard_admin.py", title="Dashboard", icon=":material/dashboard:", default=True)

if st.session_state.logged_in:
    if not st.session_state.admin:
        pg = st.navigation({"Account": [logout_page, dashboard_page, routes_page, station_page, ticket_page]})
    else:
        pg = st.navigation({"Account": [logout_page, dashboard_admin, station_management, route_management, schedule_management, train_management]})
else:
    pg = st.navigation({"Authorize": [login_page, register_page]})
pg.run()
