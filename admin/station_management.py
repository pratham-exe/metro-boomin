import streamlit as st
from sqlalchemy import text

conn = st.connection("metro.db", type="sql", url="sqlite:///./metro.db")

st.write("**Create a New Station**")
station_name = st.text_input(label="Enter Station Name")

insert_station_query = text("INSERT INTO station VALUES (:station_id, :station_name)")

if st.button("Create"):
    with conn.session as session:
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
        print(conn.query("SELECT * FROM station"))
