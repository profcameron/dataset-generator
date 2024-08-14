-- Sample output data set for reference
-- Fake data set generated on 2024-08-13 21:10:00
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
    'C01', 'Lin', 'Li',
    '9169 Donna Avenue',
    'Indiana', 'PA', '15705',
    'LLi42044@optonline.net',
    '973-338-3779');
INSERT INTO Client VALUES (
    'C02', 'Azzi', 'Rabab',
    '4313 Landau Terrace',
    'Norwood', 'MN', '55583',
    'RabaA37563@ymail.com',
    '565-804-5653');
INSERT INTO Client VALUES (
    'C03', 'Yoon', 'Jung',
    '8090 Pillow Circle',
    'Hickory', 'KY', '42051',
    'JunYoo72497@gmail.com',
    '977-573-6640');
INSERT INTO Client VALUES (
    'C04', 'Jayaraman', 'Abhinav',
    '5818 Chester Park Place',
    'Peoria', 'IL', '61602',
    'AJa26973@live.com',
    '880-857-5333');
INSERT INTO Client VALUES (
    'C05', 'Song', 'Nam',
    '7498 Chamber Highway',
    'Millwood', 'VA', '22646',
    'NaSo63013@gmail.com',
    '308-213-6665');
INSERT INTO Client VALUES (
    'C06', 'Hariri', 'Casilda',
    '9832 Science Highway',
    'Lincolnton', 'NC', '28092',
    'CaHariri96334@verizon.net',
    '221-897-8933');
INSERT INTO Client VALUES (
    'C07', 'Mehta', 'Nishi',
    '311 Prospect Avenue',
    'Sassamansville', 'PA', '19472',
    'NisMeh22525@zohomail.com',
    '378-259-5898');
INSERT INTO Client VALUES (
    'C08', 'Sato', 'Hideo',
    '6661 Kiana Drive',
    'North Smithfield', 'RI', '02896',
    'HideS86523@aol.com',
    '597-457-3328');
INSERT INTO Client VALUES (
    'C09', 'Balasubramanium', 'Raj',
    '3750 Middlerock Court',
    'Fairfield', 'CT', '06828',
    'RaBal37426@ymail.com',
    '813-803-3495');
INSERT INTO Client VALUES (
    'C10', 'Harrah', 'David',
    '1268 Max Court',
    'Lincoln', 'NE', '68583',
    'DHar38243@mail.com',
    '321-672-8867');
INSERT INTO Client VALUES (
    'C11', 'Kapoor', 'Harish',
    '9977 Rabbit Creek Court',
    'Smithland', 'KY', '42081',
    'HKapoor86287@ymail.com',
    '343-902-2568');
INSERT INTO Client VALUES (
    'C12', 'Khan', 'Pavithra',
    '8520 Kutchin Street',
    'Clinton', 'TN', '37717',
    'PavithraKhan96139@hotmail.com',
    '213-266-1311');
INSERT INTO Client VALUES (
    'C13', 'Martinez', 'Raul',
    '6651 Farpoint Lane',
    'Jamestown', 'SC', '29453',
    'RMartinez23849@ymail.com',
    '374-390-5812');
INSERT INTO Client VALUES (
    'C14', 'Chatterjee', 'Harish',
    '2784 Ostovia Boulevard',
    'Melcher-dallas', 'IA', '50163',
    'HChatte87242@yahoo.com',
    '358-283-6428');
INSERT INTO Client VALUES (
    'C15', 'Liu', 'Jian',
    '1834 Comet Court',
    'Fort Worth', 'TX', '76198',
    'JianLiu69322@optonline.net',
    '426-223-9970');
INSERT INTO Client VALUES (
    'C16', 'Evans', 'Helen',
    '9573 Joli Court',
    'West Memphis', 'AR', '72301',
    'HelenEvans67460@ymail.com',
    '891-316-9097');
INSERT INTO Client VALUES (
    'C17', 'Wilson', 'Donna',
    '1092 Patrick Boulevard',
    'Apo', 'AE', '09852',
    'DonnWils73813@gmail.com',
    '939-581-3020');
INSERT INTO Client VALUES (
    'C18', 'Azzi', 'Loelia',
    '6360 Alumni Boulevard',
    'Garita', 'NM', '88421',
    'LoeA99670@hotmail.com',
    '885-543-1168');
INSERT INTO Client VALUES (
    'C19', 'Takahashi', 'Kenji',
    '1444 Perenosa Circle',
    'Elmaton', 'TX', '77440',
    'KT15062@yahoo.com',
    '875-263-5993');
INSERT INTO Client VALUES (
    'C20', 'Shin', 'Min',
    '2402 Sherman Circle',
    'Santa Monica', 'CA', '90401',
    'MiSh61059@mail.com',
    '632-246-2750');
INSERT INTO Client VALUES (
    'C21', 'Wu', 'Lian',
    '3209 Amber Bay Avenue',
    'Boonville', 'NY', '13309',
    'LWu30865@ymail.com',
    '552-286-9950');
INSERT INTO Client VALUES (
    'C22', 'Tanaka', 'Kenji',
    '9036 Lace Circle',
    'Madison', 'IL', '62060',
    'KenTan38942@verizon.net',
    '775-220-4100');
INSERT INTO Client VALUES (
    'C23', 'Yoshida', 'Makoto',
    '4467 Parkwood Terrace',
    'Alamo', 'ND', '58830',
    'MakotoYo38974@gmail.com',
    '810-378-1612');
INSERT INTO Client VALUES (
    'C24', 'Daher', 'Dalia',
    '8322 Spectrum Way',
    'Irvine', 'CA', '92614',
    'DaliDahe61005@gmail.com',
    '461-765-3494');
INSERT INTO Client VALUES (
    'C25', 'Rivera', 'Alejandro',
    '7701 Angela Street',
    'Farnhamville', 'IA', '50538',
    'AlejandRi40426@optonline.net',
    '438-245-8382');
INSERT INTO Client VALUES (
    'C26', 'Kang', 'Ryung',
    '2996 Richardson Terrace',
    'Waltersburg', 'PA', '15488',
    'RKan87929@ymail.com',
    '978-989-9602');
INSERT INTO Client VALUES (
    'C27', 'Carter', 'Dorothy',
    '491 Snug Harbor Place',
    'Indiana', 'PA', '15705',
    'DorotCarte92630@live.com',
    '817-799-9722');
INSERT INTO Client VALUES (
    'C28', 'Pillai', 'Karthik',
    '5703 Ostovia Terrace',
    'Lithonia', 'GA', '30038',
    'KarthiPill50264@gmail.com',
    '496-725-7007');
INSERT INTO Client VALUES (
    'C29', 'Zhao', 'Chan',
    '9890 Chrome Way',
    'West Lebanon', 'NY', '12195',
    'CZha23457@live.com',
    '276-654-1772');
INSERT INTO Client VALUES (
    'C30', 'Bettar', 'Farrah',
    '6503 Big Blue Boulevard',
    'Moca', 'PR', '00676',
    'FarraBetta78814@verizon.net',
    '681-535-3839');
INSERT INTO Client VALUES (
    'C31', 'Ramirez', 'Alfredo',
    '7726 Lore Avenue',
    'Caney', 'KS', '67333',
    'AlfRa83857@mail.com',
    '806-549-2845');
INSERT INTO Client VALUES (
    'C32', 'Hayek', 'Cala',
    '1999 Kumquat Circle',
    'Lyerly', 'GA', '30730',
    'CalHaye37135@optonline.net',
    '664-459-1969');
INSERT INTO Client VALUES (
    'C33', 'Chen', 'Ju',
    '2339 Hood Circle',
    'Oakville', 'IN', '47367',
    'JChe89224@gmail.com',
    '637-255-2149');
INSERT INTO Client VALUES (
    'C34', 'Lin', 'Kang',
    '9308 Jelinek Highway',
    'Murrells Inlet', 'SC', '29576',
    'KangLin66770@zohomail.com',
    '517-671-1644');
INSERT INTO Client VALUES (
    'C35', 'Kim', 'Ki',
    '4337 Sonstrom Road',
    'Lanham', 'MD', '20706',
    'KK83538@hotmail.com',
    '976-967-7508');
INSERT INTO Client VALUES (
    'C36', 'Chen', 'Ju',
    '3573 China Berry Court',
    'Tucson', 'AZ', '85730',
    'JCh23236@mail.com',
    '491-390-8646');
INSERT INTO Client VALUES (
    'C37', 'Mitchell', 'David',
    '3879 Boulder Court',
    'King City', 'MO', '64463',
    'DavMitchell90972@zohomail.com',
    '390-988-6042');
INSERT INTO Client VALUES (
    'C38', 'Gao', 'Kang',
    '6165 Kody Avenue',
    'Glenbrook', 'NV', '89413',
    'KanGao35389@ymail.com',
    '812-939-4739');
INSERT INTO Client VALUES (
    'C39', 'Shimizu', 'Kiyoshi',
    '7140 Shasta Drive',
    'Whately', 'MA', '01093',
    'KiyoshiShimiz15652@mail.com',
    '265-283-5791');
INSERT INTO Client VALUES (
    'C40', 'Daher', 'Nabila',
    '4144 Brewery Way',
    'Cincinnati', 'OH', '45299',
    'NabilaDahe21681@live.com',
    '244-770-6449');
INSERT INTO Client VALUES (
    'C41', 'Park', 'Myung',
    '3304 Arrow Place',
    'Florence', 'AZ', '85132',
    'MyunPark24122@gmail.com',
    '583-767-7863');
