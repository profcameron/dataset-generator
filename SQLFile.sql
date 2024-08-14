-- Sample Starting Data Set for reference
-- Fake data set generated on 2024-08-13 21:03:32
DROP TABLE IF EXISTS Client;
CREATE TABLE Client (
    ClientNum CHAR(3) PRIMARY KEY,
    LastName CHAR(15),
    FirstName CHAR(15),
    Street CHAR(40),
    City CHAR(30),
    State CHAR(2),
    ZIPCode CHAR(5),
    Email CHAR(75),
    Phone CHAR(12)
);
INSERT INTO Client VALUES (
    'C01', 'Yamaguchi', 'Akira',
    '7455 Lido Boulevard',
    'Lacon', 'IL', '61540',
    'AkiYamag17054@aol.com',
    '753-431-4880');
INSERT INTO Client VALUES (
    'C02', 'Hong', 'Sang',
    '6581 Ardaiz Lane',
    'Broad Run', 'VA', '20137',
    'SH94613@mail.com',
    '937-973-8260');
INSERT INTO Client VALUES (
    'C03', 'Baker', 'Elizabeth',
    '7503 Colonel Highway',
    'Vienna', 'VA', '22183',
    'ElizabethBaker29330@verizon.net',
    '420-764-6716');
INSERT INTO Client VALUES (
    'C04', 'Sun', 'Jie',
    '2660 Blue Bear Drive',
    'Olympia', 'KY', '40358',
    'JiS93554@hotmail.com',
    '257-233-3890');
INSERT INTO Client VALUES (
    'C05', 'Ramirez', 'Rodrigo',
    '7834 Jamestown Boulevard',
    'Sherrills Ford', 'NC', '28673',
    'RRamir20018@gmail.com',
    '878-830-1541');
INSERT INTO Client VALUES (
    'C06', 'Hyat', 'Elmira',
    '2845 Shadetree Court',
    'Royalton', 'IL', '62983',
    'EHy25026@gmail.com',
    '278-416-8406');
INSERT INTO Client VALUES (
    'C07', 'Perez', 'Javier',
    '3190 Breakwater Road',
    'Ilion', 'NY', '13357',
    'JaPe45956@gmail.com',
    '951-887-7087');
INSERT INTO Client VALUES (
    'C08', 'Kato', 'Hideo',
    '9115 Taos Street',
    'Washington', 'DC', '20410',
    'HKato97095@live.com',
    '519-729-6638');
INSERT INTO Client VALUES (
    'C09', 'Park', 'Yong',
    '8330 Sweetgale Drive',
    'San Leandro', 'CA', '94579',
    'YongPark98124@yahoo.com',
    '529-511-6132');
INSERT INTO Client VALUES (
    'C10', 'Han', 'Whan',
    '539 Buena Vista Boulevard',
    'Cross River', 'NY', '10518',
    'WhanH16356@optonline.net',
    '348-415-3380');
INSERT INTO Client VALUES (
    'C11', 'Young', 'James',
    '8223 Viscount Way',
    'Torrance', 'CA', '90504',
    'JaY60256@zohomail.com',
    '648-423-7510');
INSERT INTO Client VALUES (
    'C12', 'Kadam', 'Kumar',
    '7188 Kruger Circle',
    'Trafford', 'PA', '15085',
    'KuKad40080@ymail.com',
    '789-754-7546');
INSERT INTO Client VALUES (
    'C13', 'Hariri', 'Elmira',
    '5009 Ira Court',
    'Woodville', 'MS', '39669',
    'ElmiHa30283@hotmail.com',
    '754-912-1662');
INSERT INTO Client VALUES (
    'C14', 'Abdul', 'Nabila',
    '7767 Ken Logan Court',
    'Klamath Falls', 'OR', '97601',
    'NA83411@gmail.com',
    '936-281-2796');
INSERT INTO Client VALUES (
    'C15', 'Pillai', 'Arun',
    '7254 Michelle Court',
    'Buffalo', 'NY', '14269',
    'AruP70489@ymail.com',
    '875-424-3513');
