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

def get_start_and_end_station_names(route_id):
    result = session.execute(
        text("SELECT station_ids FROM route WHERE route_id = :route_id"),
        {'route_id': route_id}
    )
    station_ids = result.scalar()

    if not station_ids:
        return "Route not found"

    stations = station_ids.split(',')
    station_start = stations[0]
    station_end = stations[-1]

    # Get the names of the start and end stations
    result_start = session.execute(
        text("SELECT station_name FROM station WHERE station_id = :station_start"),
        {'station_start': station_start}
    )
    station_start_name = result_start.scalar()

    result_end = session.execute(
        text("SELECT station_name FROM station WHERE station_id = :station_end"),
        {'station_end': station_end}
    )
    station_end_name = result_end.scalar()

    return f"{station_start_name} - {station_end_name} Line"

conn.create_function("get_route_name", 1, get_start_and_end_station_names)

tabs = st.tabs(["Create a New Train", "Delete an existing Train"])

with tabs[0]:
    for route in routes:
        # result = session.execute(text("SELECT station_ids FROM route WHERE route_id = :route_id"), {'route_id': route})
        # stations = result.scalar().split(',')
        # station_start = stations[0]
        # station_end = stations[-1]
        # result_start = session.execute(text("SELECT station_name FROM station WHERE station_id = :station_start"), {'station_start': station_start})
        # station_start_name = result_start.scalar()
        # result_end = session.execute(text("SELECT station_name FROM station WHERE station_id = :station_end"), {'station_end': station_end})
        # station_end_name = result_end.scalar()
        # station_select = f"{station_start_name} - {station_end_name} Line"

        station_select = session.execute(text("SELECT get_route_name(1)")).fetchone()[0]
        print(station_select)

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
    trains = session.execute(text("""
        SELECT
            t.train_id,
            r.station_ids,
            sch.time_stamp
        FROM
            train t
        JOIN
            route r ON t.route_id = r.route_id
        JOIN
            schedule sch ON t.schedule_id = sch.schedule_id
        """)).all()

    for item in trains:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write(item[0])
        with col2:
            stations = item[1].split(',')
            route_start_id = stations[0]
            route_end_id = stations[-1]
            route_start_name = session.execute(text("SELECT station_name FROM station WHERE station_id = :station_start"), {'station_start': route_start_id}).scalar()
            route_end_name = session.execute(text("SELECT station_name FROM station WHERE station_id = :station_end"), {'station_end': route_end_id}).scalar()
            st.write(f"{route_start_name} - {route_end_name}")
        with col3:
            st.write(item[2])
        with col4:
            if st.button("Remove Train", key=item[0]):
                st.write("Train Removed")
                session.execute(text("DELETE FROM train WHERE train_id = :train_id"), {'train_id': item[0]})
                session.commit()
                st.rerun()
