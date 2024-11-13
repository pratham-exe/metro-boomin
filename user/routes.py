import streamlit as st
import sqlite3

# Function to retrieve the start and end station names for a given route_id
def get_start_end_station_names(route_id):
    cursor = conn.cursor()

    cursor.execute("SELECT station_ids FROM route WHERE route_id = ?", (route_id,))
    stations_query = cursor.fetchone()

    if stations_query:
        stations = stations_query[0].split(',')
        station_start = stations[0]
        station_end = stations[-1]

        # Retrieve start station name
        cursor.execute("SELECT station_name FROM station WHERE station_id = ?", (station_start,))
        station_start_name = cursor.fetchone()[0]

        # Retrieve end station name
        cursor.execute("SELECT station_name FROM station WHERE station_id = ?", (station_end,))
        station_end_name = cursor.fetchone()[0]

        # Return the formatted start-end route name
        return f"{station_start_name} - {station_end_name}"
    return None

# Connect to SQLite database
conn = sqlite3.connect("metro.db")
cursor = conn.cursor()

# Register the custom function with SQLite
conn.create_function("get_start_end_station_names", 1, get_start_end_station_names)

station_options = []
station_route_id_dict = {}

# Query all route IDs
cursor.execute("SELECT route_id FROM route")
routes = [route[0] for route in cursor.fetchall()]

# Loop through each route and get the start-end station names using the registered function
for route in routes:
    cursor.execute("SELECT get_start_end_station_names(?)", (route,))
    station_select = cursor.fetchone()[0]

    if station_select:
        station_options.append(station_select)
        station_route_id_dict[station_select] = route

# Streamlit dropdown to select a route
option = st.selectbox("Routes", station_options)

# Query the selected route's stations and display their names
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

# Close the database connection
conn.close()