import streamlit as st

conn = st.connection("metro.db", type="sql", url="sqlite:///./metro.db")

routes = conn.query("SELECT route_id FROM route")["route_id"].to_list()
option = st.selectbox("Route", (routes))

stations = conn.query(f"SELECT station_ids FROM route WHERE route_id = '{option}'")["station_ids"].values[0]
station_list = stations.split(",")

station_names = conn.query("SELECT * FROM station")

station_id_list = " -> ".join(f"'{each_station}'" for each_station in station_list)
st.write(station_id_list)
