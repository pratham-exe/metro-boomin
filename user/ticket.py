import streamlit as st

conn = st.connection("metro.db", type="sql", url="sqlite:///./metro.db")

stations = conn.query("SELECT station_name FROM station")["station_name"].to_list()
source = st.selectbox("From", stations)
destination = st.selectbox("To", stations)
routes = conn.query("SELECT route_id FROM route")["route_id"].to_list()
station_id_source = conn.query(f"SELECT station_id FROM station WHERE station_name = '{source}'")['station_id'].values[0]
station_id_dest = conn.query(f"SELECT station_id FROM station WHERE station_name = '{destination}'")['station_id'].values[0]
station_id_center = conn.query("SELECT station_id FROM station WHERE station_name = 'Majestic'")['station_id'].values[0]

if source == destination:
    st.write("Destination cannot be same as Source")
else:
    for route in routes:
        station_ids_for_route = conn.query(f"SELECT station_ids FROM route WHERE route_id = '{route}'")['station_ids'].values[0].split(',')
        source_index = station_ids_for_route.index(station_id_source)
        if source_index != -1:
            center_index = station_ids_for_route.index(station_id_center)
            break
    for route in routes:
        station_ids_for_route = conn.query(f"SELECT station_ids FROM route WHERE route_id = '{route}'")['station_ids'].values[0].split(',')
        dest_index = station_ids_for_route.index(station_id_dest)
        if dest_index != -1:
            center_index = station_ids_for_route.index(station_id_center)
            break
    source_to_center = abs(center_index - source_index)
    center_to_dest = abs(dest_index - center_index)
    distance = source_to_center + center_to_dest
    price = distance * 10
    st.write(f"Price: {price}")
