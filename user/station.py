import streamlit as st
from datetime import datetime, timedelta

conn = st.connection("metro.db", type="sql", url="sqlite:///./metro.db")

stations = conn.query("SELECT station_name FROM station")["station_name"].to_list()
option = st.selectbox("Station", stations)
routes = conn.query("SELECT route_id FROM route")["route_id"].to_list()

endtime = datetime.strptime("21:00", "%H:%M")

station_id_option = conn.query(f"SELECT station_id FROM station WHERE station_name = '{option}'")['station_id'].values[0]

for route in routes:
    station_ids_for_route = conn.query(f"SELECT station_ids FROM route WHERE route_id = '{route}'")['station_ids'].values[0].split(',')
    if station_id_option in station_ids_for_route:
        train_route = conn.query(f"SELECT train_id, schedule_id FROM train WHERE route_id = '{route}'")
        train_id = train_route['train_id'].values.tolist()
        schedule_id = train_route['schedule_id'].values.tolist()
        for i in range(len(train_id)):
            cur_time = datetime.strptime(conn.query(f"SELECT time_stamp FROM schedule WHERE schedule_id = '{schedule_id[i]}'")['time_stamp'].values[0], "%H:%M")
            position = 0
            direction = 1
            with st.expander(f"{train_id[i]}"):
                while(cur_time < endtime):
                    station_name = conn.query(f"SELECT station_name FROM station WHERE station_id = '{station_ids_for_route[position]}'")['station_name'].values[0]
                    st.write(f"{station_name} - {cur_time.strftime("%H:%M")}")
                    cur_time = cur_time + timedelta(minutes=20)
                    position += direction
                    if position == len(station_ids_for_route) - 1:
                        direction = -1
                    elif position == 0:
                        direction = 1



