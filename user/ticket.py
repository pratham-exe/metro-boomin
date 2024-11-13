import streamlit as st
from sqlalchemy import text

conn = st.connection("metro.db", type="sql", url="sqlite:///./metro.db")
session = conn.session

stations = session.execute(text("SELECT station_name FROM station")).fetchall()
stations = [station[0] for station in stations]

source = st.selectbox("From", stations)
destination = st.selectbox("To", stations)

routes = session.execute(text("SELECT route_id FROM route")).fetchall()
routes = [route[0] for route in routes]


def get_station_id(station_name):
    query = "SELECT station_id FROM station WHERE station_name = :station_name"
    result = session.execute(text(query), {
        "station_name": station_name
    }).fetchone()
    if result:
        return result[0]
    return None


station_id_source = get_station_id(source)
station_id_dest = get_station_id(destination)
station_id_center = get_station_id("Majestic")

query = text("INSERT INTO ticket (ticket_id, source, destination, price) VALUES (:ticket_id, :source, :destination, :price)")

if source == destination:
    st.write("Destination cannot be same as Source")
else:
    source_index = None
    dest_index = None
    for route in routes:
        station_ids_for_route = conn.query(f"SELECT station_ids FROM route WHERE route_id = '{route}'")['station_ids'].values[0].split(',')
        if station_id_source in station_ids_for_route:
            source_index = station_ids_for_route.index(station_id_source)
            if station_id_center:
                center_index_source = station_ids_for_route.index(station_id_center)
            source_route = route
            break
    for route in routes:
        station_ids_for_route = conn.query(f"SELECT station_ids FROM route WHERE route_id = '{route}'")['station_ids'].values[0].split(',')
        if station_id_dest in station_ids_for_route:
            dest_index = station_ids_for_route.index(station_id_dest)
            if station_id_center:
                center_index_dest = station_ids_for_route.index(station_id_center)
            dest_route = route
            break
    if source_index is None or dest_index is None:
        st.write("There is no route which goes through these two stations.")
    else:
        if station_id_center is None and source_route != dest_route:
            st.write("There is no route which goes through these two stations.")
        else:
            if station_id_center is None and source_route == dest_route:
                distance = abs(source_index - dest_index)
            else:
                source_to_center = abs(center_index_source - source_index)
                center_to_dest = abs(dest_index - center_index_dest)
                if (source_index > center_index_source and dest_index > center_index_dest and source_route == dest_route) or (source_index < center_index_source and dest_index < center_index_dest and source_route == dest_route):
                    distance = abs(source_to_center - center_to_dest)
                else:
                    distance = source_to_center + center_to_dest
            price = distance * 10
            st.write(f"Price: {price}")
            if st.button("Buy Ticket"):
                with conn.session as session:
                    session.begin()
                    last_ticket = session.execute(text("SELECT ticket_id FROM ticket ORDER BY ticket_id DESC LIMIT 1")).fetchone()
                    if last_ticket is None:
                        next_ticket_id = "t_001"
                    else:
                        ticket_id = last_ticket[0]
                        last_ticket_num = int(ticket_id.split('_')[1])
                        next_ticket_id = f"t_{str(last_ticket_num + 1).zfill(3)}"
                    session.execute(query, {
                        'ticket_id': next_ticket_id,
                        'source': source,
                        'destination': destination,
                        'price': price
                    })
                    session.commit()
                    user_tickets = session.execute(text(f"SELECT tickets FROM user WHERE user_name = '{st.session_state['name']}'")).fetchone()[0]
                    if user_tickets is None:
                        new_tickets = next_ticket_id
                    else:
                        new_tickets = f"{user_tickets},{next_ticket_id}"
                    session.execute(text("UPDATE user SET tickets = :tickets WHERE user_name = :user_name"), {
                        'tickets': new_tickets,
                        'user_name': st.session_state["name"]
                    })
                    session.commit()
                    st.success("Ticket purchased successfully")
