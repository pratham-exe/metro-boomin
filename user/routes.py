import streamlit as st
from sqlalchemy import text

station_options = []
station_route_id_dict = {}

conn = st.connection("metro.db", type="sql", url="sqlite:///./metro.db")

with conn.session as session:
    routes = session.execute(text("SELECT route_id FROM route")).fetchall()
    routes = [route[0] for route in routes]

    for route in routes:
        stations_query = session.execute(text("SELECT station_ids FROM route WHERE route_id = :route"), {
            "route": route
        }).fetchone()

        if stations_query:
            stations = stations_query[0].split(',')
            station_start = stations[0]
            station_end = stations[-1]

            station_start_name = session.execute(text("SELECT station_name FROM station WHERE station_id = :station_id"), {
                "station_id": station_start
            }).fetchone()[0]

            station_end_name = session.execute(text("SELECT station_name FROM station WHERE station_id = :station_id"), {
                "station_id": station_end
            }).fetchone()[0]

            station_select = f"{station_start_name} - {station_end_name}"
            station_options.append(station_select)
            station_route_id_dict[station_select] = route

option = st.selectbox("Routes", station_options)

with conn.session as session:
    station_ids_query = session.execute(text("SELECT station_ids FROM route WHERE route_id = :route_id"), {
        "route_id": station_route_id_dict[option]
    }).fetchone()

    if station_ids_query:
        station_list = station_ids_query[0].split(',')

        for station in station_list:
            station_name = session.execute(text("SELECT station_name FROM station WHERE station_id = :station_id"), {
                "station_id": station
            }).fetchone()
            if station_name is None:
                continue
            else:
                station_name = station_name[0]
            st.write(station_name)
