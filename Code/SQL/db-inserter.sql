--THIS FILE ADDS DATA TO THE DATABASE. IT SHOULD BE RUN AFTER db-creator.sql. 
--Data is based on the Sit website, with some random data. Adds all data nescessary to test all given use cases. 

--ADD GYM
INSERT INTO gym (name, open_time, closing_time, address_street, address_street_number, address_postcode) VALUES 
    ('Øya treningssenter', '05:00', '00:00', 'Klæbuveien', 70, 7030), --1
    ('Dragvoll idrettssenter', '05:00', '00:00', 'Loholt alle', 81, 7049); --2

--ADD FACILITIES
INSERT INTO facility (gym_id, name, max_people) VALUES
    --Øya
    (1, 'Styrkerom', 40), --1
    (1, 'Kondisjonsrom', 35), --2
    (1, 'Spinningsal', 25), --3
    (1, 'Yoga-sal', 20), --4
    (1, 'Crossfit-sal', 30), --5
    --Dragvoll
    (2, 'Styrkerom', 40), --6
    (2, 'Kondisjonsrom', 35), --7
    (2, 'Spinningsal', 25), --8
    (2, 'Yoga-sal', 20), --9
    (2, 'Crossfit-sal', 30); --10

--ADD BIKES
INSERT INTO bike (facility_id, number, has_bodybike) VALUES
    -- Spinningsal øya
    (3, 1, 1),
    (3, 2, 1),
    (3, 3, 1),
    (3, 4, 0),
    (3, 5, 0),
    (3, 6, 0),
    -- Crossfit-sal øya
    (5, 1, 0),
    (5, 2, 0),
    (5, 3, 1),
    (5, 4, 1);

--ADD TRAINERS AND USERS
INSERT INTO person (first_name, last_name, email, mobile_number, is_sit_member) VALUES
    -- Users, randomly generated
    ('Jhonny', 'Hansen', 'jhonny@stud.ntnu.no', '912345678', 1), --1
    ('Ingrid', 'Berntsen', 'ingrid@stud.ntnu.no', '922345678', 1), --2
    ('Marius', 'Larsen', 'marius@stud.ntnu.no', '932345678', 1), --3
    ('Sofie', 'Nilsen', 'sofie@stud.ntnu.no', '942345678', 1), --4
    ('Henrik', 'Olsen', 'henrik@stud.ntnu.no', '952345678', 1), --5
    ('Emma', 'Kristiansen', 'emma@stud.ntnu.no', '962345678', 1), --6
    ('Ole', 'Andersen', 'ole@stud.ntnu.no', '972345678', 1), --7
    ('Nora', 'Haugen', 'nora@stud.ntnu.no', '982345678', 1), --8
    ('Eirik', 'Johansen', 'eirik@stud.ntnu.no', '992345678', 0), --9
    ('Linn', 'Pedersen', 'linn@stud.ntnu.no', '902345678', 0), --10
    -- Instructors, with names as per Sit website
    ('Eirin', 'Helseth', 'eirin@stud.ntnu.no', '962345679', 1), --11
    ('Siri', 'Mostad Larsen', 'siri@stud.ntnu.no', '932345680', 1), --12
    ('Jorunn', 'Barte By', 'jorunn@stud.ntnu.no', '932345780', 1), --13
    ('Ramona', 'Los Satones', 'ramona@stud.ntnu.no', '932345780', 1), --14
    ('Trine', 'Røstad', 'trine@stud.ntnu.no', '932345780', 1), --15
    ('Nora', 'Dahl', 'nora@stud.ntnu.no', '932345781', 1), --16
    ('Håkon', 'Wold', 'hakon@stud.ntnu.no', '932345782', 1), --17
    ('Hanne', 'Haga', 'hanne@stud.ntnu.no', '932345783', 1), --18
    ('Ada', 'Jensen Røstad', 'ada@stud.ntnu.no', '932345784', 1), --19
    ('Sindre', 'Kristiansen Sæter', 'sindre@stud.ntnu.no', '932345785', 1), --20
    ('Kaja', 'Sæther', 'kaja@stud.ntnu.no', '932345786', 1), --21
    ('Amalie', 'Martinsen Høst', 'amalie@stud.ntnu.no', '932345787', 1); --22


--ADD CATEGORIES
INSERT INTO category (name) VALUES
    ('Spinning'), --1
    ('Yoga'), --2
    ('Crossfit'), --3
    ('Styrkesport'), --4
    ('Pilates'), --5
    ('Pump'), --6
    ('Sit WOD'), --7
    ('Sit HIIT'), --8
    ('Løp'), --9
    ('Step'), --10
    ('Tabata'); --11

--ADD ACTIVITIES, with descriptions from Sit website. 
INSERT INTO activity (category_id, name, description) VALUES
    --All spinning activities
    (1, 'Spin 4x4', --1
    'En forutsigbar intervalltime: 4 stående intervaller på 4 minutter hver, med ca 2 minutter aktiv pause mellom hvert drag. God oppvarming og nedsykling inkludert.'), 
    (1, 'Spin45', --2
    'En variert spinningtime med 2-3 arbeidsperioder som passer for alle. Perfekt for deg som er ny på spinning! Du styrer intensiteten selv, og vi bruker takta til å tråkke oss gjennom timen.'),
    (1, 'Spin 8x3', --3
    'En forutsigbar intervalltime med 8 intervaller på 3 minutter hver, der du sitter og står annethvert drag. 90-120 sek pause mellom hvert intervall. God oppvarming og nedsykling inkludert.'), 
    (1, 'Spin60', --4
    'En variert spinningtime som er noe mer utfordrende enn Spin45 med lengre varighet og tidvis høyere tempo. Du styrer likevel intensiteten selv, og timen passer alle som liker å tråkke i takt! Timen inneholder 2-4 arbeidsperioder med variert løype.'),
    --Selection of other activities
    (2, 'Yoga Stretch', --5
    'En rolig time med fokus på uttøying og fleksibilitet. Vi bruker yogaposisjoner og tar for oss de store muskelgruppene, med mål om å mykne- og åpne opp stramme og anspente kropper. Vi holder oss lavt på matta og holder posisjonene over lengre tid. Timen er rolig og passer alle. Avsluttes med avspenning i savasana; hvilestilling.'),
    (7, 'Sit WOD', --6
    'CrossFit-inspirert time. Funksjonell trening (functional fitness) der du kombinerer styrke og utholdenhet. Øktene består ofte av 2-3 ulike bolker, der du jobber i en gitt tid. Øktene varierer med tanke på oppsett og øvelser, men det er alltid mulig å tilpasse til sin egen form. Utstyr som benyttes er eksempelvis romaskin, plyobokser, vektskiver, hantler, stenger, assault bikes, kettlebells - og mye egen kroppsvekt. '),
    (4, 'Pump', --7
    'Styrketrening for hele kroppen med vektstang, i takt til musikk. Hver øvelse gjøres i 3-4 sett, med 6-12 repetisjoner. Pause mellom hvert sett der du kan hente deg inn og justere vektene. Du tilpasser selv belastningen ved å legge på vekter. Timen er perfekt for deg som er ny med styrketrening, eller som ønsker å trene på grunnleggende styrkeøvelser.'),
    (8, 'Sit HIIT', --8
    'HIIT står for High Intensity Interval Training. Timen kombinerer løping og styrke i intervaller. Du skal gjennom 3-6 bolker der du veksler mellom mølle og en styrkestasjon. Her bruker vi manualer, kettlebells og egen kroppsvekt. Du styrer intensiteten helt selv gjennom å justere fart på mølla, tilpasse vektene, og tempoet du utfører styrkeøvelsene i.');


--ADD SPINNING CLASSES. All spinning classes from sit website during specified time frame.
INSERT INTO group_lesson (start_time, end_time, instructor_id, max_participants_at_creation, activity_id, facility_id) VALUES
    -- Monday 16.03.2026
    ('2026-03-16 07:00:00', '2026-03-16 07:45:00', 11, 20, 1, 3),   -- Spin 4x4, Eirin H., Spinningsal Øya
    ('2026-03-16 16:30:00', '2026-03-16 17:15:00', 12, 20, 1, 8),   -- Spin 4x4, Siri M. L., Spinningsal Dragvoll
    ('2026-03-16 16:30:00', '2026-03-16 17:15:00', 13, 20, 2, 3),   -- Spin45, Jorunn B. B., Spinningsal Øya
    ('2026-03-16 17:40:00', '2026-03-16 18:35:00', 14, 20, 3, 3),   -- Spin8x3, Ramona L. S, Spinningsal Øya
    ('2026-03-16 19:00:00', '2026-03-16 20:00:00', 15, 20, 4, 3),   -- Spin60, Trine R., Spinningsal Øya
    -- Tuesday 17.03.2026
    ('2026-03-17 16:30:00', '2026-03-17 17:30:00', 16, 20, 3, 3),   -- Spin8x3, Nora D., Spinningsal Øya
    ('2026-03-17 18:30:00', '2026-03-17 19:30:00', 17, 20, 4, 3),   -- Spin60, Håkon W., Spinningsal Øya
    ('2026-03-17 19:45:00', '2026-03-17 20:30:00', 18, 20, 1, 3),   -- Spin 4x4, Hanne H., Spinningsal Øya
    -- Wednesday 18.03.2026
    ('2026-03-18 16:15:00', '2026-03-18 17:15:00', 16, 20, 4, 3),   -- Spin60, Nora D., Spinningsal Øya
    ('2026-03-18 16:30:00', '2026-03-18 17:15:00', 19, 20, 2, 8),   -- Spin45, Ada J. R., Spinningsal Dragvoll
    ('2026-03-18 17:30:00', '2026-03-18 18:15:00', 20, 20, 1, 3),   -- Spin 4x4, Sindre K. S., Spinningsal Øya
    ('2026-03-18 18:30:00', '2026-03-18 19:15:00', 21, 20, 2, 3),   -- Spin45, Kaja S., Spinningsal Øya
    ('2026-03-18 19:30:00', '2026-03-18 20:25:00', 22, 20, 3, 3);   -- Spin8x3, Amalie M. H., Spinningsal Øya

--ADD BOOKINGS
--TODO

--ADD ARRIVALS
--TODO