--THIS FILE CREATES THE DATABASE.

--Enforce foreign key constraints
PRAGMA foreign_keys = ON;

CREATE TABLE
    gym (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, --ADDED
        open_time TEXT NOT NULL CHECK (open_time LIKE '__:__'),
        closing_time TEXT NOT NULL CHECK (closing_time LIKE '__:__'),
        address_street TEXT NOT NULL,
        address_street_number INTEGER NOT NULL,
        address_postcode INTEGER NOT NULL
    );

CREATE TABLE
    staffed_period (
        gym_id INTEGER PRIMARY KEY,
        weekday_start TEXT NOT NULL CHECK (weekday_start LIKE '__:__'),
        weekday_end TEXT NOT NULL CHECK (weekday_end LIKE '__:__'),
        weekend_start TEXT NOT NULL CHECK (weekend_start LIKE '__:__'),
        weekend_end TEXT NOT NULL CHECK (weekend_end LIKE '__:__'),
        FOREIGN KEY (gym_id) REFERENCES gym (id) ON DELETE CASCADE,
        CHECK (
            weekday_start < weekday_end
            AND weekend_start < weekend_end
        )
    );

CREATE TABLE
    facility (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        gym_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        max_people INTEGER NOT NULL,
        FOREIGN KEY (gym_id) REFERENCES gym (id) ON DELETE CASCADE
    );

CREATE TABLE
    treadmill (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        facility_id INTEGER NOT NULL,
        number INTEGER NOT NULL CHECK (number >= 0),
        manufacturer TEXT NOT NULL,
        max_speed INTEGER NOT NULL CHECK (max_speed >= 0),
        max_incline INTEGER NOT NULL CHECK (max_incline >= 0),
        FOREIGN KEY (facility_id) REFERENCES facility (id),
        UNIQUE (facility_id, number)
    );

CREATE TABLE
    bike (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        facility_id INTEGER NOT NULL,
        number INTEGER NOT NULL CHECK (number >= 0),
        has_bodybike INTEGER NOT NULL CHECK (has_bodybike IN (0, 1)) DEFAULT 0,
        FOREIGN KEY (facility_id) REFERENCES facility (id),
        UNIQUE (facility_id, number)
    );

CREATE TABLE
    sport_team (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );

CREATE TABLE
    sport_team_member (
        sport_team_id INTEGER NOT NULL,
        person_id INTEGER NOT NULL,
        PRIMARY KEY (sport_team_id, person_id),
        FOREIGN KEY (sport_team_id) REFERENCES sport_team (id) ON DELETE CASCADE,
        FOREIGN KEY (person_id) REFERENCES person (id) ON DELETE CASCADE
    );

CREATE TABLE
    sport_team_booking (
        sport_team_id INTEGER NOT NULL,
        facility_id INTEGER NOT NULL,
        start_time TEXT NOT NULL CHECK (start_time LIKE '____-__-__ __:__:00'),
        PRIMARY KEY (sport_team_id, facility_id, start_time),
        FOREIGN KEY (sport_team_id) REFERENCES sport_team (id) ON DELETE CASCADE,
        FOREIGN KEY (facility_id) REFERENCES facility (id) ON DELETE CASCADE
    );

CREATE TABLE
    person (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL CHECK (email LIKE '%_@_%._%'),
        mobile_number TEXT NOT NULL CHECK (length (mobile_number) BETWEEN 9 AND 15),
        is_sit_member INTEGER NOT NULL CHECK (is_sit_member IN (0, 1)) DEFAULT 0,
        UNIQUE(email, mobile_number)
    );

CREATE TABLE
    dot (
        person_id INTEGER NOT NULL,
        time TEXT NOT NULL CHECK (time LIKE '____-__-__ __:__:__'),
        PRIMARY KEY (person_id, time),
        FOREIGN KEY (person_id) REFERENCES person (id) ON DELETE CASCADE
    );

CREATE TABLE
    gym_arrival (
        gym_id INTEGER NOT NULL,
        person_id INTEGER NOT NULL,
        time TEXT NOT NULL CHECK (time LIKE '____-__-__ __:__:__'),
        PRIMARY KEY (gym_id, person_id, time),
        FOREIGN KEY (gym_id) REFERENCES gym (id),
        FOREIGN KEY (person_id) REFERENCES person (id)
    );

CREATE TABLE
    group_lesson (
        start_time TEXT NOT NULL CHECK (start_time LIKE '____-__-__ __:__:00'),
        end_time TEXT NOT NULL CHECK (end_time LIKE '____-__-__ __:__:00'), --ADDED (idk hvorfor den ikke var her fra før)
        instructor_id INTEGER NOT NULL,
        max_participants_at_creation INTEGER NOT NULL,
        activity_id INTEGER NOT NULL,
        facility_id INTEGER NOT NULL,
        PRIMARY KEY (start_time, instructor_id),
        FOREIGN KEY (instructor_id) REFERENCES person (id),
        FOREIGN KEY (activity_id) REFERENCES activity (id),
        FOREIGN KEY (facility_id) REFERENCES facility (id) ON DELETE CASCADE,
        UNIQUE(start_time, facility_id)
    );

CREATE TABLE
    group_lesson_arrival (
        person_id INTEGER NOT NULL,
        group_lesson_start_time TEXT NOT NULL,
        group_lesson_instructor_id INTEGER NOT NULL,
        time TEXT NOT NULL,
        CHECK (time LIKE '____-__-__ __:__:__'),
        PRIMARY KEY (
            person_id,
            group_lesson_start_time,
            group_lesson_instructor_id
        ),
        FOREIGN KEY (
            group_lesson_start_time,
            group_lesson_instructor_id
        ) REFERENCES group_lesson (start_time, instructor_id) ON DELETE CASCADE,
        FOREIGN KEY (person_id) REFERENCES person (id) ON DELETE CASCADE
    );

CREATE TABLE
    category (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );

CREATE TABLE
    activity (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        description TEXT,
        FOREIGN KEY (category_id) REFERENCES category (id) ON DELETE CASCADE
    );

CREATE TABLE
    group_lesson_registration (
        person_id INTEGER NOT NULL,
        group_lesson_start_time TEXT NOT NULL,
        group_lesson_instructor_id INTEGER NOT NULL,
        queue_position INTEGER NOT NULL CHECK (queue_position >= 0),
        PRIMARY KEY (
            person_id,
            group_lesson_start_time,
            group_lesson_instructor_id
        ),
        FOREIGN KEY (person_id) REFERENCES person (id) ON DELETE CASCADE,
        FOREIGN KEY (
            group_lesson_start_time,
            group_lesson_instructor_id
        ) REFERENCES group_lesson (start_time, instructor_id) ON DELETE CASCADE,
        UNIQUE (person_id, group_lesson_start_time)
    );