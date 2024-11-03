import sqlite3

conn = sqlite3.connect("metro.db")
cur = conn.cursor()

stations = [
    ("st_001", "Majestic"),
    ("st_002", "Bangalore City"),
    ("st_003", "Kengeri"),
    ("st_004", "Rajajinagar"),
    ("st_005", "Malleswaram"),
    ("st_006", "Sankey Tank"),
    ("st_007", "Cubbon Park"),
    ("st_008", "Indiranagar"),
    ("st_009", "Koramangala"),
    ("st_010", "Whitefield"),
    ("st_011", "Marathahalli"),
    ("st_012", "Bellandur"),
    ("st_013", "Sarjapur"),
    ("st_014", "BTM Layout"),
    ("st_015", "JP Nagar"),
    ("st_016", "Bannerghatta"),
    ("st_017", "Electronics City"),
    ("st_018", "Hosur Road"),
    ("st_019", "Yelahanka"),
    ("st_020", "KR Puram"),
    ("st_021", "HSR Layout"),
    ("st_022", "Kasturinagar"),
    ("st_023", "Shanti Nagar"),
    ("st_024", "Jayanagar"),
    ("st_025", "BTM"),
    ("st_026", "Vijayanagar"),
    ("st_027", "Banashankari"),
    ("st_028", "Nagarbhavi"),
    ("st_029", "Rajamahal Vilas"),
    ("st_030", "Vaswani Park"),
    ("st_031", "Brigade Road"),
    ("st_032", "MG Road"),
    ("st_033", "Ulsoor Lake"),
    ("st_034", "Lalbagh"),
    ("st_035", "Madiwala"),
    ("st_036", "Koramangala 3rd Block"),
    ("st_037", "Jakkasandra"),
    ("st_038", "Vijaya Bank Layout"),
    ("st_039", "Hennur"),
    ("st_040", "Kalyan Nagar"),
    ("st_041", "Tavarekere"),
    ("st_042", "Yelahanka New Town"),
    ("st_043", "Kudlu Gate"),
    ("st_044", "Srinagar"),
    ("st_045", "Shivaji Nagar"),
    ("st_046", "Gandhi Bazar"),
    ("st_047", "Nandi Hills"),
    ("st_048", "Gokula"),
    ("st_049", "Mysore Road"),
    ("st_050", "Chikkalasandra"),
    ("st_051", "Anekal"),
    ("st_052", "Banashankari 2nd Stage"),
    ("st_053", "Chandapura"),
    ("st_054", "Mahalakshmi Layout"),
    ("st_055", "Nagawara"),
    ("st_056", "Marasandra"),
    ("st_057", "Mysore"),
    ("st_058", "Nayandahalli"),
    ("st_059", "Sunkadakatte"),
    ("st_060", "Krishna Rajendra Market"),
    ("st_061", "Sheshadripuram"),
    ("st_062", "Sankey Road"),
    ("st_063", "Raja Rajeshwari Nagar"),
    ("st_064", "Hosur"),
    ("st_065", "Devanahalli"),
    ("st_066", "Yelahanka Junction"),
    ("st_067", "Jakkur"),
    ("st_068", "Doddaballapura"),
    ("st_069", "Peenya"),
    ("st_070", "Chikkajala"),
    ("st_071", "Nagarbhavi"),
    ("st_072", "Anjanapura"),
    ("st_073", "Basavanagudi"),
    ("st_074", "RT Nagar"),
    ("st_075", "Shivajinagar"),
    ("st_076", "Ulsoor"),
    ("st_077", "Girinagar"),
    ("st_078", "Chamarajpet"),
    ("st_079", "Lalbagh West Gate"),
    ("st_080", "Madiwala Market"),
    ("st_081", "Indira Nagar"),
    ("st_082", "Koramangala 5th Block"),
    ("st_083", "Brigade Gardens"),
    ("st_084", "Malleswaram 8th Cross"),
    ("st_085", "Seshadripuram"),
    ("st_086", "Shantinagar"),
    ("st_087", "Hosur Road Junction"),
    ("st_088", "Yeshwanthpur"),
    ("st_089", "Kengeri Satellite Town"),
    ("st_090", "Nagarathpet"),
    ("st_091", "Bangalore University")
]
routes = [
    ("route_001", "st_002,st_003,st_004,st_005,st_006,st_007,st_001,st_008,st_009,st_010"),
    ("route_002", "st_011,st_012,st_013,st_014,st_015,st_016,st_001,st_017,st_018,st_019"),
    ("route_003", "st_020,st_021,st_022,st_023,st_024,st_025,st_001,st_026,st_027,st_028"),
    ("route_004", "st_029,st_030,st_031,st_032,st_033,st_034,st_001,st_035,st_036,st_037"),
    ("route_005", "st_038,st_039,st_040,st_041,st_042,st_043,st_001,st_044,st_045,st_046"),
    ("route_006", "st_047,st_048,st_049,st_050,st_051,st_052,st_001,st_053,st_054,st_055"),
    ("route_007", "st_056,st_057,st_058,st_059,st_060,st_061,st_001,st_062,st_063,st_064"),
    ("route_008", "st_065,st_066,st_067,st_068,st_069,st_070,st_001,st_071,st_072,st_073"),
    ("route_009", "st_074,st_075,st_076,st_077,st_078,st_079,st_001,st_080,st_081,st_082"),
    ("route_010", "st_083,st_084,st_085,st_086,st_087,st_088,st_001,st_089,st_090,st_091")
]
schedules = [
    ("schedule_1", "09:00"),
    ("schedule_2", "09:15"),
    ("schedule_3", "09:30"),
    ("schedule_4", "09:45"),
    ("schedule_5", "10:00"),
    ("schedule_6", "10:15"),
    ("schedule_7", "10:30"),
    ("schedule_8", "10:45")
]
trains = [
    ("train_001", "route_008", "schedule_2"),
    ("train_002", "route_001", "schedule_3"),
    ("train_003", "route_006", "schedule_8"),
    ("train_004", "route_002", "schedule_2"),
    ("train_005", "route_009", "schedule_1"),
    ("train_006", "route_008", "schedule_3"),
    ("train_007", "route_007", "schedule_1"),
    ("train_008", "route_004", "schedule_5"),
    ("train_009", "route_003", "schedule_4"),
    ("train_010", "route_006", "schedule_3"),
    ("train_011", "route_009", "schedule_3"),
    ("train_012", "route_002", "schedule_6"),
    ("train_013", "route_004", "schedule_6"),
    ("train_014", "route_010", "schedule_6"),
    ("train_015", "route_005", "schedule_6"),
    ("train_016", "route_002", "schedule_8"),
    ("train_017", "route_008", "schedule_5"),
    ("train_018", "route_003", "schedule_8"),
    ("train_019", "route_002", "schedule_4"),
    ("train_020", "route_004", "schedule_2")
]

cur.execute("CREATE TABLE IF NOT EXISTS station(station_id TEXT PRIMARY KEY, station_name TEXT NOT NULL)")
cur.executemany("INSERT INTO station VALUES (?, ?)", stations)

cur.execute("CREATE TABLE IF NOT EXISTS route(route_id TEXT PRIMARY KEY, station_ids TEXT)")
cur.executemany("INSERT INTO route VALUES (?, ?)", routes)

cur.execute("CREATE TABLE IF NOT EXISTS schedule(schedule_id TEXT PRIMARY KEY, time_stamp TIME NOT NULL)")
cur.executemany("INSERT INTO schedule VALUES (?, ?)", schedules)

cur.execute("CREATE TABLE IF NOT EXISTS train(train_id TEXT PRIMARY KEY, route_id TEXT, schedule_id TEXT, FOREIGN KEY (route_id) REFERENCES route (route_id), FOREIGN KEY (schedule_id) REFERENCES schedule (schedule_id))")
cur.executemany("INSERT INTO train VALUES (?, ?, ?)", trains)

cur.execute("CREATE TABLE IF NOT EXISTS ticket(ticket_id, source, destination, price)")

cur.execute("CREATE TABLE IF NOT EXISTS user(user_id, user_name, age, gender, tickets)")

conn.commit()
conn.close()
