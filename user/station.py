import streamlit as st
from datetime import datetime, timedelta
from sqlalchemy import text

conn = st.connection("metro.db", type="sql", url="sqlite:///./metro.db")

with conn.session as session:
    stations = session.execute(text("SELECT station_name FROM station")).fetchall()
    stations = [station[0] for station in stations]
    option = st.selectbox("Station", stations)

    routes = session.execute(text("SELECT route_id FROM route")).fetchall()
    routes = [route[0] for route in routes]

    endtime = datetime.strptime("21:00", "%H:%M")

    station_id_option = session.execute(text("SELECT station_id FROM station WHERE station_name = :option"), {
        "option": option
    }).fetchone()[0]

    for route in routes:
        station_ids_for_route = session.execute(text("SELECT station_ids FROM route WHERE route_id = :route"), {
            "route": route
        }).fetchone()[0].split(',')

        if station_id_option in station_ids_for_route:
            train_route = session.execute(text("SELECT train_id, schedule_id FROM train WHERE route_id = :route"), {
                "route": route
            }).fetchall()

            for train_id, schedule_id in train_route:
                cur_time = datetime.strptime(
                    session.execute(text("SELECT time_stamp FROM schedule WHERE schedule_id = :schedule_id"), {
                        "schedule_id": schedule_id
                    }).fetchone()[0], "%H:%M"
                )

                position = 0
                direction = 1
                with st.expander(f"{train_id}"):
                    while cur_time < endtime:
                        station_name_query = session.execute(text("SELECT station_name FROM station WHERE station_id = :station_id"), {
                            "station_id": station_ids_for_route[position]
                        }).fetchone()

                        if not station_name_query:
                            break
                        else:
                            station_name = station_name_query[0]

                        if station_name == option:
                            st.write(f"{station_name} - {cur_time.strftime('%H:%M')}")

                        cur_time += timedelta(minutes=20)
                        position += direction

                        if position == len(station_ids_for_route) - 1:
                            direction = -1
                        elif position == 0:
                            direction = 1
