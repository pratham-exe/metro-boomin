import streamlit as st
from sqlalchemy import text

conn = st.connection("metro.db", type="sql", url="sqlite:///./metro.db")

session = conn.session

routes = session.execute(text("SELECT route_id FROM route"))
routes = routes.scalars().all()

all_stations = session.execute(text("SELECT station_name FROM station"))
all_stations = all_stations.scalars().all()

if "station_list" not in st.session_state:
    st.session_state.station_list = []

modify_tab, add_route_tab, delete_route_tab = st.tabs(["Modify existing route", "Add a new route", "Delete a Route"])

with modify_tab:
    st.header("Modify Route")
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
        with st.expander(f"{station_select}"):
            stations_on_route = session.execute(text("SELECT station_ids FROM route where route_id = :route_id"), {'route_id': route})
            stations_on_route = stations_on_route.scalars().all()
            stations_on_route = stations_on_route[0].split(',')
            coln1, coln2, coln3 = st.columns([2, 2, 1])
            with coln1:
                added_station = st.selectbox("Station", all_stations, key=f"{route}_selectbox")
            with coln2:
                position = st.number_input(label="Enter a position", min_value=1, max_value=len(stations_on_route), key=f"{route}_number")
            with coln3:
                if st.button("Add Stop", key=f"{route}_button"):
                    added_station_id = session.execute(text("SELECT station_id FROM station WHERE station_name = :station_name"), {'station_name': added_station}).scalar()
                    if added_station_id not in stations_on_route:
                        stations_on_route.insert(position - 1, added_station_id)
                        new_stations = ",".join(stations_on_route)
                        session.execute(text("UPDATE route SET station_ids = :new_station_ids WHERE route_id = :route_id_to_update"),
                                        {"new_station_ids": new_stations, "route_id_to_update": route})
                        session.commit()
                        st.rerun()
                    else:
                        st.write("Station is in Route")
            for station_id in stations_on_route:
                station_name = session.execute(text("SELECT station_name FROM station WHERE station_id = :station_id"), {'station_id': station_id}).scalar()
                col1, col2 = st.columns([4, 1])  # Create columns for alignment
                with col1:
                    st.write(station_name)
                with col2:
                    if st.button("−", key=f"remove_{station_id}_route_id_{route}"):
                        stations_on_route.remove(station_id)
                        new_stations = ",".join(stations_on_route)
                        session.execute(text("UPDATE route SET station_ids = :new_station_ids WHERE route_id = :route_id_to_update"),
                                        {"new_station_ids": new_stations, "route_id_to_update": route})
                        session.commit()
                        st.rerun()
with add_route_tab:
    st.header("Add Route")
    last_route = session.execute(text("SELECT route_id FROM route ORDER BY route_id DESC LIMIT 1")).fetchone()
    if last_route:
        last_route = last_route[0]
        last_route_no = int(last_route.split("_")[1])
        next_route = last_route_no + 1
        next_route_id = f"route_{str(next_route).zfill(3)}"

        with st.expander("Stations"):
            routes = session.execute(text("SELECT route_id FROM route")).fetchall()
            routes = [route[0] for route in routes]

            for route in routes:
                stations_query = session.execute(text("SELECT station_ids FROM route WHERE route_id = :route"), {
                    "route": route
                }).fetchone()

                if stations_query:
                    stations = stations_query[0].split(',')

                for station in stations:
                    station_name = session.execute(text("SELECT station_name FROM station WHERE station_id = :station_id"), {
                        "station_id": station
                    }).fetchone()
                    if station_name is None:
                        continue
                    else:
                        station_name = station_name[0]

                    col1, col2 = st.columns([4, 1])
                    with col1:
                        st.write(station_name)
                    with col2:
                        if st.button("✚", key=f"station_{station_name}route{route}"):
                            station_id = session.execute(text("SELECT station_id FROM station WHERE station_name = :station_name"), {'station_name': station_name}).fetchone()[0]
                            if station_id not in st.session_state.station_list:
                                st.session_state.station_list.append(station_id)

        with st.expander(f"Route {next_route}"):
            if st.session_state.station_list:
                for station_id in st.session_state.station_list:
                    station_name = session.execute(text("SELECT station_name FROM station WHERE station_id = :station_id"), {"station_id": station_id}).fetchone()[0]
                    col1, col2 = st.columns([4, 1])
                    with col1:
                        st.write(f"- {station_name}")
                    with col2:
                        if st.button("−", key=f"station_{station_name}"):
                            st.session_state.station_list.remove(station_id)
                            st.rerun()

        if st.button("Add route"):
            if st.session_state.station_list:
                station_list = ",".join(st.session_state.station_list)
                session.execute(text("INSERT INTO route VALUES (:route_id, :station_ids)"), {
                    'route_id': next_route_id,
                    'station_ids': station_list
                })
                session.commit()
                st.session_state.station_list = []
                st.rerun()

with delete_route_tab:
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

            station_start_name = session.execute(text("SELECT station_name FROM station WHERE station_id = :station_id"), {"station_id": station_start}).fetchone()[0]
            station_end_name = session.execute(text("SELECT station_name FROM station WHERE station_id = :station_id"), {"station_id": station_end}).fetchone()[0]
            station_select = f"{station_start_name} - {station_end_name}"

            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(station_select)
            with col2:
                if st.button("−", key=f"route_{route}"):
                    session.execute(text("DELETE FROM route WHERE route_id = :route_id"), {
                        'route_id': route
                    })
                    session.commit()
                    st.rerun()
