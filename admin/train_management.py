import streamlit as st
from sqlalchemy import text

conn = st.connection("metro.db", type="sql", url="sqlite:///./metro.db")
session = conn.session

routes = session.execute(text("SELECT route_id FROM route"))
routes = routes.scalars().all()

schedule = session.execute(text("SELECT time_stamp FROM schedule"))
schedule = schedule.scalars().all()

check_query = """SELECT COUNT(*) FROM train WHERE route_id = :route_id AND schedule_id = :schedule_id"""

route_list = []
route_dict = {}
route_dict_reverse = {}
timestamp_list = []

tabs = st.tabs(["Create a New Train", "Delete an existing Train"])

with tabs[0]:
    for route in routes:
        result = session.execute(text("SELECT station_ids FROM route WHERE route_id = :route_id"), {'route_id': route})
        stations = result.scalar().split(',')
        station_start = stations[0]
        station_end = stations[-1]
        result_start = session.execute(text("SELECT station_name FROM station WHERE station_id = :station_start"), {'station_start': station_start})
        station_start_name = result_start.scalar()
        result_end = session.execute(text("SELECT station_name FROM station WHERE station_id = :station_end"), {'station_end': station_end})
        station_end_name = result_end.scalar()
        station_select = f"{station_start_name} - {station_end_name} Line"

        route_list.append(station_select)
        route_dict[station_select] = route
        route_dict_reverse[route] = station_select

    for timestamp in schedule:
        timestamp_list.append(timestamp)

    option = st.selectbox("Route", route_list)
    time_option = st.selectbox("Time", timestamp_list)

    if st.button("Add Train"):
        last_train = session.execute(text("SELECT train_id FROM train ORDER BY train_id DESC LIMIT 1")).fetchone()[0]
        last_train = last_train.split("_")
        next_train = f"train_{str(int(last_train[1]) + 1).zfill(3)}"
        schedule_id = session.execute(text("SELECT schedule_id FROM schedule WHERE time_stamp = :time_option "), {"time_option": time_option}).fetchone()[0]
        route_id = route_dict[option]
        check_train_constraint = session.execute(text(check_query), {"route_id": route_id, "schedule_id": schedule_id}).scalar()
        if check_train_constraint == 0:
            session.execute(text("INSERT INTO train VALUES (:train_id, :route_id, :schedule_id)"), {"train_id": next_train, "route_id": route_id, "schedule_id": schedule_id})
            st.write("Train added Successfully")
        else:
            st.write("Trains cant have same route and schedule")
        session.commit()

with tabs[1]:
    trains = session.execute(text("SELECT * FROM train")).all()

    for item in trains:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write(item[0])
        with col2:
            result = session.execute(text("SELECT station_ids FROM route WHERE route_id = :route_id"), {'route_id': item[1]})
            stations = result.scalar().split(',')
            route_start_id = stations[0]
            route_end_id = stations[-1]
            route_start_name = session.execute(text("SELECT station_name FROM station WHERE station_id = :station_start"), {'station_start': route_start_id}).scalar()
            route_end_name = session.execute(text("SELECT station_name FROM station WHERE station_id = :station_end"), {'station_end': route_end_id}).scalar()
            st.write(f"{route_start_name} - {route_end_name}")
        with col3:
            schedule_id = session.execute(text("SELECT time_stamp FROM schedule WHERE schedule_id = :schedule_id"), {"schedule_id": item[2]}).fetchone()[0]
            st.write(schedule_id)
        with col4:
            if st.button("Remove Train", key=item[0]):
                st.write("Train Removed")
                session.execute(text("DELETE FROM train WHERE train_id = :train_id"), {'train_id': item[0]})
                session.commit()
                st.rerun()
