PRAGMA foreign_keys=OFF;

BEGIN TRANSACTION;

CREATE TABLE station(station_id TEXT PRIMARY KEY, station_name TEXT NOT NULL);
INSERT INTO station VALUES('st_001','Majestic');
INSERT INTO station VALUES('st_002','Bangalore City');
INSERT INTO station VALUES('st_003','Kengeri');
INSERT INTO station VALUES('st_004','Rajajinagar');
INSERT INTO station VALUES('st_005','Malleswaram');
INSERT INTO station VALUES('st_006','Sankey Tank');
INSERT INTO station VALUES('st_007','Cubbon Park');
INSERT INTO station VALUES('st_008','Indiranagar');
INSERT INTO station VALUES('st_009','Koramangala');
INSERT INTO station VALUES('st_010','Whitefield');
INSERT INTO station VALUES('st_011','Marathahalli');
INSERT INTO station VALUES('st_012','Bellandur');
INSERT INTO station VALUES('st_013','Sarjapur');
INSERT INTO station VALUES('st_014','BTM Layout');
INSERT INTO station VALUES('st_015','JP Nagar');
INSERT INTO station VALUES('st_016','Bannerghatta');
INSERT INTO station VALUES('st_017','Electronics City');
INSERT INTO station VALUES('st_018','Hosur Road');
INSERT INTO station VALUES('st_019','Yelahanka');
INSERT INTO station VALUES('st_020','KR Puram');
INSERT INTO station VALUES('st_021','HSR Layout');
INSERT INTO station VALUES('st_022','Kasturinagar');
INSERT INTO station VALUES('st_023','Shanti Nagar');
INSERT INTO station VALUES('st_024','Jayanagar');
INSERT INTO station VALUES('st_025','BTM');
INSERT INTO station VALUES('st_026','Vijayanagar');
INSERT INTO station VALUES('st_027','Banashankari');
INSERT INTO station VALUES('st_028','Nagarbhavi');
INSERT INTO station VALUES('st_029','Rajamahal Vilas');
INSERT INTO station VALUES('st_030','Vaswani Park');
INSERT INTO station VALUES('st_031','Brigade Road');
INSERT INTO station VALUES('st_032','MG Road');
INSERT INTO station VALUES('st_033','Ulsoor Lake');
INSERT INTO station VALUES('st_034','Lalbagh');
INSERT INTO station VALUES('st_035','Madiwala');
INSERT INTO station VALUES('st_036','Koramangala 3rd Block');
INSERT INTO station VALUES('st_037','Jakkasandra');
INSERT INTO station VALUES('st_038','Vijaya Bank Layout');
INSERT INTO station VALUES('st_039','Hennur');
INSERT INTO station VALUES('st_040','Kalyan Nagar');
INSERT INTO station VALUES('st_041','Tavarekere');
INSERT INTO station VALUES('st_042','Yelahanka New Town');
INSERT INTO station VALUES('st_043','Kudlu Gate');
INSERT INTO station VALUES('st_044','Srinagar');
INSERT INTO station VALUES('st_045','Shivaji Nagar');
INSERT INTO station VALUES('st_046','Gandhi Bazar');
INSERT INTO station VALUES('st_047','Nandi Hills');
INSERT INTO station VALUES('st_048','Gokula');
INSERT INTO station VALUES('st_049','Mysore Road');
INSERT INTO station VALUES('st_050','Chikkalasandra');
INSERT INTO station VALUES('st_051','Anekal');
INSERT INTO station VALUES('st_052','Banashankari 2nd Stage');
INSERT INTO station VALUES('st_053','Chandapura');
INSERT INTO station VALUES('st_054','Mahalakshmi Layout');
INSERT INTO station VALUES('st_055','Nagawara');
INSERT INTO station VALUES('st_056','Marasandra');
INSERT INTO station VALUES('st_057','Mysore');
INSERT INTO station VALUES('st_058','Nayandahalli');
INSERT INTO station VALUES('st_059','Sunkadakatte');
INSERT INTO station VALUES('st_060','Krishna Rajendra Market');
INSERT INTO station VALUES('st_061','Sheshadripuram');
INSERT INTO station VALUES('st_062','Sankey Road');
INSERT INTO station VALUES('st_063','Raja Rajeshwari Nagar');
INSERT INTO station VALUES('st_064','Hosur');
INSERT INTO station VALUES('st_065','Devanahalli');
INSERT INTO station VALUES('st_066','Yelahanka Junction');
INSERT INTO station VALUES('st_067','Jakkur');
INSERT INTO station VALUES('st_068','Doddaballapura');
INSERT INTO station VALUES('st_069','Peenya');
INSERT INTO station VALUES('st_070','Chikkajala');
INSERT INTO station VALUES('st_072','Anjanapura');
INSERT INTO station VALUES('st_073','Basavanagudi');
INSERT INTO station VALUES('st_074','RT Nagar');
INSERT INTO station VALUES('st_075','Shivajinagar');
INSERT INTO station VALUES('st_076','Ulsoor');
INSERT INTO station VALUES('st_077','Girinagar');
INSERT INTO station VALUES('st_078','Chamarajpet');
INSERT INTO station VALUES('st_079','Lalbagh West Gate');
INSERT INTO station VALUES('st_080','Madiwala Market');
INSERT INTO station VALUES('st_081','Indira Nagar');
INSERT INTO station VALUES('st_082','Koramangala 5th Block');
INSERT INTO station VALUES('st_083','Brigade Gardens');
INSERT INTO station VALUES('st_084','Malleswaram 8th Cross');
INSERT INTO station VALUES('st_085','Seshadripuram');
INSERT INTO station VALUES('st_086','Shantinagar');
INSERT INTO station VALUES('st_087','Hosur Road Junction');
INSERT INTO station VALUES('st_088','Yeshwanthpur');
INSERT INTO station VALUES('st_089','Kengeri Satellite Town');
INSERT INTO station VALUES('st_090','Nagarathpet');
INSERT INTO station VALUES('st_091','Bangalore University');

CREATE TABLE route(route_id TEXT PRIMARY KEY, station_ids TEXT);
INSERT INTO route VALUES('route_001','st_002,st_003,st_004,st_005,st_006,st_007,st_001,st_008,st_009,st_010');
INSERT INTO route VALUES('route_002','st_011,st_012,st_013,st_014,st_015,st_016,st_001,st_017,st_018,st_019');
INSERT INTO route VALUES('route_003','st_020,st_021,st_022,st_023,st_024,st_025,st_001,st_026,st_027,st_028');
INSERT INTO route VALUES('route_004','st_029,st_030,st_031,st_032,st_033,st_034,st_001,st_035,st_036,st_037');
INSERT INTO route VALUES('route_005','st_038,st_039,st_040,st_041,st_042,st_043,st_001,st_044,st_045,st_046');
INSERT INTO route VALUES('route_006','st_047,st_048,st_049,st_050,st_051,st_052,st_001,st_053,st_054,st_055');
INSERT INTO route VALUES('route_007','st_056,st_057,st_058,st_059,st_060,st_061,st_001,st_062,st_063,st_064');
INSERT INTO route VALUES('route_008','st_065,st_066,st_067,st_068,st_069,st_070,st_001,st_072,st_073');
INSERT INTO route VALUES('route_009','st_074,st_075,st_076,st_077,st_078,st_079,st_001,st_080,st_081,st_082');
INSERT INTO route VALUES('route_010','st_083,st_084,st_085,st_086,st_087,st_088,st_001,st_089,st_090,st_091');

CREATE TABLE schedule(schedule_id TEXT PRIMARY KEY, time_stamp TIME NOT NULL);
INSERT INTO schedule VALUES('schedule_1','09:00');
INSERT INTO schedule VALUES('schedule_2','09:15');
INSERT INTO schedule VALUES('schedule_3','09:30');
INSERT INTO schedule VALUES('schedule_4','09:45');
INSERT INTO schedule VALUES('schedule_5','10:00');
INSERT INTO schedule VALUES('schedule_6','10:15');
INSERT INTO schedule VALUES('schedule_7','10:30');
INSERT INTO schedule VALUES('schedule_8','10:45');

CREATE TABLE train(train_id TEXT PRIMARY KEY, route_id TEXT, schedule_id TEXT, FOREIGN KEY (route_id) REFERENCES route (route_id), FOREIGN KEY (schedule_id) REFERENCES schedule (schedule_id));
INSERT INTO train VALUES('train_001','route_008','schedule_2');
INSERT INTO train VALUES('train_002','route_001','schedule_3');
INSERT INTO train VALUES('train_003','route_006','schedule_8');
INSERT INTO train VALUES('train_004','route_002','schedule_2');
INSERT INTO train VALUES('train_005','route_009','schedule_1');
INSERT INTO train VALUES('train_006','route_008','schedule_3');
INSERT INTO train VALUES('train_007','route_007','schedule_1');
INSERT INTO train VALUES('train_008','route_004','schedule_5');
INSERT INTO train VALUES('train_009','route_003','schedule_4');
INSERT INTO train VALUES('train_010','route_006','schedule_3');
INSERT INTO train VALUES('train_011','route_009','schedule_3');
INSERT INTO train VALUES('train_012','route_002','schedule_6');
INSERT INTO train VALUES('train_013','route_004','schedule_6');
INSERT INTO train VALUES('train_014','route_010','schedule_6');
INSERT INTO train VALUES('train_015','route_005','schedule_6');
INSERT INTO train VALUES('train_016','route_002','schedule_8');
INSERT INTO train VALUES('train_017','route_008','schedule_5');
INSERT INTO train VALUES('train_018','route_003','schedule_8');
INSERT INTO train VALUES('train_019','route_002','schedule_4');
INSERT INTO train VALUES('train_020','route_004','schedule_2');

CREATE TABLE ticket(ticket_id TEXT PRIMARY KEY, source TEXT, destination TEXT, price INTEGER);

CREATE TABLE user(user_id TEXT PRIMARY KEY, user_name TEXT NOT NULL, tickets TEXT, admin TEXT);
INSERT INTO user VALUES('pratham','Pratham Rao',NULL,'False');
INSERT INTO user VALUES('rahul','Rahul Jacob',NULL,'True');

CREATE TRIGGER delete_station_from_route
AFTER DELETE ON station
BEGIN
    UPDATE route
    SET station_ids = CASE
        WHEN station_ids LIKE OLD.station_id || ',%' THEN REPLACE(station_ids, OLD.station_id || ',', '')
        WHEN station_ids LIKE '%,' || OLD.station_id || ',%' THEN REPLACE(station_ids, ',' || OLD.station_id || ',', ',')
        WHEN station_ids LIKE '%,' || OLD.station_id THEN REPLACE(station_ids, ',' || OLD.station_id, '')
        ELSE station_ids
    END
    WHERE station_ids LIKE '%' || OLD.station_id || '%';
END;

CREATE TRIGGER delete_trains_from_schedule
AFTER DELETE ON schedule
BEGIN
    DELETE FROM train
    WHERE schedule_id = OLD.schedule_id;
END;

COMMIT;
