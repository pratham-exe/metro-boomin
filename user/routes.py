import streamlit as st
import sqlite3


def get_start_end_station_names(route_id):
    cursor = conn.cursor()

    cursor.execute("SELECT station_ids FROM route WHERE route_id = ?", (route_id,))
    stations_query = cursor.fetchone()

    if stations_query:
        stations = stations_query[0].split(',')
        station_start = stations[0]
        station_end = stations[-1]

        cursor.execute("SELECT station_name FROM station WHERE station_id = ?", (station_start,))
        station_start_name = cursor.fetchone()[0]

        cursor.execute("SELECT station_name FROM station WHERE station_id = ?", (station_end,))
        station_end_name = cursor.fetchone()[0]

        return f"{station_start_name} - {station_end_name}"
    return None


conn = sqlite3.connect("metro.db")
cursor = conn.cursor()

conn.create_function("get_start_end_station_names", 1, get_start_end_station_names)

station_options = []
station_route_id_dict = {}

cursor.execute("SELECT route_id FROM route")
routes = [route[0] for route in cursor.fetchall()]

for route in routes:
    cursor.execute("SELECT get_start_end_station_names(?)", (route,))
    station_select = cursor.fetchone()[0]

    if station_select:
        station_options.append(station_select)
        station_route_id_dict[station_select] = route

try:
    option = st.selectbox("Routes", station_options)

    route_id = station_route_id_dict[option]
    cursor.execute("SELECT station_ids FROM route WHERE route_id = ?", (route_id,))
    station_ids_query = cursor.fetchone()

    if station_ids_query:
        station_list = station_ids_query[0].split(',')

        for station_id in station_list:
            cursor.execute("SELECT station_name FROM station WHERE station_id = ?", (station_id,))
            station_name = cursor.fetchone()
            if station_name:
                st.write(station_name[0])

    conn.close()
except Exception as e:
    print(e)
