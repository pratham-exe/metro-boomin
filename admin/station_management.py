import streamlit as st
from sqlalchemy import text

conn = st.connection("metro.db", type="sql", url="sqlite:///./metro.db")
session = conn.session

tabs = st.tabs(["Create a New Station", "Delete an existing Station"])

with tabs[0]:
    station_name = st.text_input(label="Enter Station Name")

    insert_station_query = text("INSERT INTO station VALUES (:station_id, :station_name)")

    if st.button("Create"):
        check_station_existence = session.execute(text("SELECT COUNT(*) AS station_count FROM station WHERE station_name = :station_name"), {
            'station_name': station_name
        }).scalar()
        if check_station_existence:
            st.write(f"Station {station_name} already exists")
        else:
            last_station = session.execute(text("SELECT station_id FROM station ORDER BY station_id DESC LIMIT 1")).fetchone()
            station_id = last_station[0]
            last_station_number = int(station_id.split('_')[1])
            next_station_id = f"st_{str(last_station_number + 1).zfill(3)}"
            session.execute(insert_station_query, {
                'station_id': next_station_id,
                'station_name': station_name
            })
            st.write(f"Station {station_name} created with Station ID {next_station_id}")
            session.commit()

with tabs[1]:
    stations = session.execute(text("SELECT station_name FROM station")).fetchall()
    stations = [station[0] for station in stations]
    delete_station_name = st.selectbox("Enter Station Name", stations)

    if st.button("Delete"):
        session.execute(text("DELETE FROM station WHERE station_name = :station_name"), {
            'station_name': delete_station_name
        })
        session.commit()
        st.success("Deleted successfully")
