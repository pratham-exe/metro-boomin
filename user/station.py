import streamlit as st

conn = st.connection("metro.db", type="sql", url="sqlite:///./metro.db")

stations = conn.query("SELECT station_name FROM station")["station_name"].to_list()
option = st.selectbox("Station", stations)
routes = conn.query("SELECT route_id FROM route")["route_id"].to_list()

station_id_option = conn.query(f"SELECT station_id FROM station WHERE station_name = '{option}'")['station_id'].values[0]

for route in routes:
    station_ids_for_route = conn.query(f"SELECT station_ids FROM route WHERE route_id = '{route}'")['station_ids'].values[0].split(',')
    if station_id_option in station_ids_for_route:
        train_route = conn.query(f"SELECT train_id, schedule_id FROM train WHERE route_id = '{route}'")
        train_id = train_route['train_id'].values
        st.write(train_id)
