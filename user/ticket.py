import streamlit as st
from sqlalchemy import text

conn = st.connection("metro.db", type="sql", url="sqlite:///./metro.db")

stations = conn.query("SELECT station_name FROM station")["station_name"].to_list()
source = st.selectbox("From", stations)
destination = st.selectbox("To", stations)
routes = conn.query("SELECT route_id FROM route")["route_id"].to_list()
station_id_source = conn.query(f"SELECT station_id FROM station WHERE station_name = '{source}'")['station_id'].values[0]
station_id_dest = conn.query(f"SELECT station_id FROM station WHERE station_name = '{destination}'")['station_id'].values[0]
station_id_center = conn.query("SELECT station_id FROM station WHERE station_name = 'Majestic'")['station_id'].values[0]

query = text("INSERT INTO ticket (ticket_id, source, destination, price) VALUES (:ticket_id, :source, :destination, :price)")

if source == destination:
    st.write("Destination cannot be same as Source")
else:
    for route in routes:
        station_ids_for_route = conn.query(f"SELECT station_ids FROM route WHERE route_id = '{route}'")['station_ids'].values[0].split(',')
        if station_id_source in station_ids_for_route:
            source_index = station_ids_for_route.index(station_id_source)
            center_index_source = station_ids_for_route.index(station_id_center)
            source_route = route
            break
    for route in routes:
        station_ids_for_route = conn.query(f"SELECT station_ids FROM route WHERE route_id = '{route}'")['station_ids'].values[0].split(',')
        if station_id_dest in station_ids_for_route:
            dest_index = station_ids_for_route.index(station_id_dest)
            center_index_dest = station_ids_for_route.index(station_id_center)
            dest_route = route
            break
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
