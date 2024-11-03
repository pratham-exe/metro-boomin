import streamlit as st

station_options = []
station_route_id_dict = {}

conn = st.connection("metro.db", type="sql", url="sqlite:///./metro.db")
routes = conn.query("SELECT route_id FROM route")["route_id"].to_list()

for route in routes:
    stations = conn.query(f"SELECT station_ids FROM route WHERE route_id = '{route}'")["station_ids"].values[0].split(',')
    station_start = stations[0]
    station_end = stations[-1]
    station_start_name = conn.query(f"SELECT station_name FROM station WHERE station_id = '{station_start}'")["station_name"].values[0]
    station_end_name = conn.query(f"SELECT station_name FROM station WHERE station_id = '{station_end}'")["station_name"].values[0]
    station_select = f"{station_start_name} - {station_end_name}"
    station_options.append(station_select)
    station_route_id_dict[station_select] = route


option = st.selectbox("Routes", (station_options))

stations = conn.query(f"SELECT station_ids FROM route WHERE route_id = '{station_route_id_dict[option]}'")["station_ids"].values[0]
station_list = stations.split(",")

for station in station_list:
    station_name = conn.query(f"SELECT station_name FROM station WHERE station_id = '{station}'")['station_name'].values[0]
    st.write(station_name)
