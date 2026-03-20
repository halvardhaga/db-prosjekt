PRAGMA foreign_keys = ON;

--Prevent registration after three dots
CREATE TRIGGER trg_registration_block_blacklisted
BEFORE INSERT ON group_lesson_registration
BEGIN
    SELECT RAISE (ABORT, 'Registration blocked: Person is blacklisted.')
    WHERE (
        --Counts the number of dots for the person in the last 30 days
        SELECT COUNT(*)
        FROM dot
        WHERE dot.person_id = NEW.person_id
        AND datetime(time) > datetime('now', '-30 days')
    ) >= 3;
END;

--Issue dot if a person is late for a group lesson
CREATE TRIGGER trg_dot_for_late_arrival
AFTER INSERT ON group_lesson_arrival
BEGIN
    INSERT INTO dot (person_id, time)
    SELECT 
        NEW.person_id,
        datetime(NEW.time)
    WHERE datetime(NEW.time) > datetime(
        --Gets the start time of the group lesson the person is arriving late to
        (SELECT start_time FROM group_lesson
         WHERE start_time    = NEW.group_lesson_start_time
           AND instructor_id = NEW.group_lesson_instructor_id)
        - '5 minutes'
    )
END;

--Prevent double booking of a facility by a sport team if a group lesson is already sheduled at that time
CREATE TRIGGER trg_prevent_double_booking_team_vs_group_lesson
BEFORE INSERT ON sport_team_booking
BEGIN
SELECT RAISE (ABORT, 'Booking blocked: Facility is already booked by a group lesson at this timeperiod.')
WHERE EXISTS (
    SELECT 1
    FROM group_lesson
    WHERE group_lesson.facility_id = NEW.facility_id AND (
        (datetime(NEW.start_time) >= datetime(group_lesson.start_time) AND datetime(NEW.start_time) < datetime(group_lesson.end_time))
        OR
        (datetime(NEW.end_time) > datetime(group_lesson.start_time) AND datetime(NEW.end_time) <= datetime(group_lesson.end_time))
        OR
        (datetime(NEW.start_time) <= datetime(group_lesson.start_time) AND datetime(NEW.end_time) >= datetime(group_lesson.end_time))
    )
)

--Prevent double booking of a facility by a group lesson if a sport team has already booked it at that time
CREATE TRIGGER trg_prevent_double_booking_group_lesson_vs_team
BEFORE INSERT ON group_lesson
BEGIN
SELECT RAISE (ABORT, 'Booking blocked: Facility is already booked by a sport team at this timeperiod.')
WHERE EXISTS (
    SELECT 1
    FROM sport_team_booking
    WHERE sport_team_booking.facility_id = NEW.facility_id AND (
        (datetime(NEW.start_time) >= datetime(sport_team_booking.start_time) AND datetime(NEW.start_time) < datetime(sport_team_booking.end_time))
        OR
        (datetime(NEW.end_time) > datetime(sport_team_booking.start_time) AND datetime(NEW.end_time) <= datetime(sport_team_booking.end_time))
        OR
        (datetime(NEW.start_time) <= datetime(sport_team_booking.start_time) AND datetime(NEW.end_time) >= datetime(sport_team_booking.end_time))
    )
)

--Make sure that group_lessons's max_participants_at_creation equals the facilities max_people
CREATE TRIGGER trg_lesson_max_participants_equals_facility_max_people
BEFORE INSERT ON group_lesson
BEGIN
SELECT RAISE (ABORT, "Creation blocked: max_participants_at_creation must equal the facility's max_people.")
WHERE NEW.max_participants_at_creation != (
    SELECT max_people
    FROM facility
    WHERE facility_id = NEW.facility_id
);
END;

--Same but on update
CREATE TRIGGER trg_lesson_max_participants_equals_facility_max_people_update
BEFORE UPDATE ON group_lesson
BEGIN
SELECT RAISE (ABORT, "Update blocked: max_participants_at_creation must equal the facility's max_people.")
WHERE NEW.max_participants_at_creation != (
    SELECT max_people
    FROM facility
    WHERE facility_id = NEW.facility_id
);
END;

--Group lessons must be made by someone with a sit membership
CREATE TRIGGER trg_group_instructor_must_be_sit_member
BEFORE INSERT ON group_lesson
BEGIN
SELECT RAISE (ABORT, "Creation blocked: Instructor must have a sit membership.")
WHERE (
    SELECT is_sit_member
    FROM person
    WHERE person_id = NEW.instructor_id
) != 1;
END;

--Same but on update
CREATE TRIGGER trg_group_instructor_must_be_sit_member_update
BEFORE UPDATE ON group_lesson
BEGIN
SELECT RAISE (ABORT, "Update blocked: Instructor must have a sit membership.")
WHERE (
    SELECT is_sit_member
    FROM person
    WHERE person_id = NEW.instructor_id
) != 1;
END;

