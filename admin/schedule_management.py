import streamlit as st
from sqlalchemy import text

conn = st.connection("metro.db", type="sql", url="sqlite:///./metro.db")
session = conn.session

tabs = st.tabs(["Add a new schedule", "Delete existing schedule"])

with tabs[0]:
    schedule_time = st.time_input("")
    hrs_min_time = schedule_time.strftime("%H:%M")
    last_schedule = session.execute(text("SELECT schedule_id FROM schedule ORDER BY schedule_id DESC LIMIT 1")).fetchone()[0]
    next_schedule = f"schedule_{str(int(last_schedule.split('_')[1]) + 1)}"
    old_timings = session.execute(text("SELECT schedule_id, time_stamp FROM schedule")).fetchall()
    schedule_timings = [schedule[1] for schedule in old_timings]
    if st.button("Add schedule"):
        if hrs_min_time not in schedule_timings:
            session.execute(text("INSERT INTO schedule VALUES (:schedule_id, :time_stamp)"), {
                'schedule_id': next_schedule,
                'time_stamp': hrs_min_time
            })
            session.commit()
            st.success("Schedule added successfully")

with tabs[1]:
    current_timings = session.execute(text("SELECT schedule_id, time_stamp FROM schedule")).fetchall()
    with st.expander("Schedules"):
        for each_schedule, time_stamp in current_timings:
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(time_stamp)
            with col2:
                if st.button("−", key=f"schedule_{each_schedule}"):
                    session.execute(text("DELETE FROM schedule WHERE schedule_id = :schedule_id"), {
                        'schedule_id': each_schedule
                    })
                    session.commit()
                    st.rerun()
