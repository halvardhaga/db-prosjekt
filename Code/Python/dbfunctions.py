"""Contains various handler functions for database-related commands.

All functions follow:
    Args:
        args (list): List of arguments passed to the command. Expected values are defined in the docstring of each function.
        conn (sqlite3.connection): The database connection object.

    Returns (str): Value of database query or message indicating sucess/failure.

    Raises:
        ValueError: If the args list has incorrect length or invalid data.
        sqlite3.Error: If a database operation fails.

"""

import re
import sqlite3
from typing import List
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent # Absolute path to the directory containing this script.
DB_PATH = HERE.parent / 'database.db' #database file location and name. 

#Template for all db related functions (except db_init) to follow
def db_function_template (args: List, conn: sqlite3.Connection) -> str:
    """
    This is a template for all db functions to follow. 

    Args:
        -
        - ...
    """
    #TODO
    return "Function not implementet yet"

def db_init():
    """
    Initialize the database, if not already initialized.
    """
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        with open(HERE.parent / "SQL" / "db-creator.sql", 'r') as f:
            sqlschema = f.read()
        conn.executescript(sqlschema)
        with open(HERE.parent / "SQL" / "trigger-creator.sql", 'r') as f:
            sqltrigger = f.read()
        conn.executescript(sqltrigger)
        conn.close()

def nuke(args: List, conn: sqlite3.Connection) -> str:
    """
    Clear all data from the database by deleting the database file and recreating it.
    """
    validation = input("Are you sure you want to nuke the database? This will delete the database file and recreate it. (y/n) ")
    if validation.lower() != "y":
        return "Database nuke cancelled."
    os.remove(DB_PATH)
    db_init()
    return "Database cleared and recreated"

def insert_dummy_data(args: List, conn: sqlite3.Connection) -> str:
    """
    Insert dummy data into the database (for testing purposes).
    """
    with open(HERE.parent / "SQL" / "db-inserter.sql", 'r') as f:
        sql = f.read()
    conn.executescript(sql)
    return "Dummy data inserted"

#Use case 2 
#We assume there are no two acitivities of the same category starting at the same time. TODO is this fair?
def book_lesson (args: List, conn: sqlite3.Connection) -> str:
    """
    Create booking for group lesson.

    Args:
        - email: The email of the user booking the lesson.
        - phone: The phone number of the user booking the lesson.
        - category: eg. yoga, spinning, etc.
        - time: In the format YYYY-MM-DD HH:MM (e.g. 2026-03-15 18:30)
    """
    
    if len(args) != 4:
        raise ValueError("Usage: book_lesson <email> <phone> <category> <time>")
    

    #Check if person exists, and fetch person id. 
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM person WHERE email = ? AND phone = ?", (args[0], args[1]))
    person_id = cursor.fetchone()
    if not person_id:
        raise ValueError("User not found")
    
    #Check if category exists, and fetch category id
    cursor.execute("SELECT id FROM category WHERE name = ?", (args[2]))
    category_id = cursor.fetchone()
    if not category_id:
        raise ValueError("Category not found")

    #Check if class exists at given time and fetch start time and instructor id
    cursor.execute("""
                   SELECT start_time, instructor_id 
                   FROM group_lesson 
                   JOIN activity ON activity_id = activity.id
                   WHERE category_id = ? AND start_time = ?""", 
                   (category_id[0], args[3]))
    group_lesson = cursor.fetchone()
    if not group_lesson:
        raise ValueError("Group lesson not found")
    start_time = group_lesson[0]
    instructor_id = group_lesson[1]
    
    #QUEUE LOGIC TODO
    queue_position = 0

    cursor.execute("INSERT INTO group_lesson_registration (person_id, group_lesson_start_time, group_lesson_instructor_id, queue_position) VALUES ?, ?, ?, ?", (person_id, start_time, instructor_id, queue_position))

    return "Group lesson booked successfully"

#Use case 3
def attend_gym (args: List, conn: sqlite3.Connection) -> str:
    """
    Registers that given user attended given gym at current time. 

    Args:
        - email: The email of the user attending the gym.
        - phone: The phone number of the user attending the gym.
        - gym: The name or ID of the gym.
    """

    if len(args) != 3:
        raise ValueError("Usage: attend_gym <email> <phone> <gym>")
    
    #Check if person exists, and fetch person id. 
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM person WHERE email = ? AND phone = ?", (args[0], args[1]))
    person_id = cursor.fetchone()
    if not person_id:
        raise ValueError("User not found")
    
    #Check if gym exists, and fetch gym id
    cursor.execute("SELECT id FROM gym WHERE name = ? OR id = ?", (args[2], args[2]))
    gym_id = cursor.fetchone()
    if not gym_id:
        raise ValueError("Gym not found")

    #Insert gym arrival
    cursor.execute("INSERT INTO gym_arrival (person_id, gym_id, time) VALUES (?, ?, datetime('now'))", (person_id[0], gym_id[0]))

    return "Gym attendance registered successfully"

#Use case 3
def attend_class (args: List, conn: sqlite3.Connection) -> str:
    """
    Registers that given user attended given class at current time. 

    Args:
        - email: The email of the user booking the lesson.
        - phone: The phone number of the user booking the lesson.
        - category: eg. yoga, spinning, etc.
        - time: In the format YYYY-MM-DD HH:MM (e.g. 2026-03-15 18:30)
    """
       
    if len(args) != 4:
        raise ValueError("Usage: attend_class <email> <phone> <category> <time>")

    #Check if person exists, and fetch person id. 
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM person WHERE email = ? AND phone = ?", (args[0], args[1]))
    person_id = cursor.fetchone()
    if not person_id:
        raise ValueError("User not found")
    
    #Check if category exists, and fetch category id
    cursor.execute("SELECT id FROM category WHERE name = ?", (args[2]))
    category_id = cursor.fetchone()
    if not category_id:
        raise ValueError("Category not found")

    #Check if class exists at given time and fetch start time and instructor id
    cursor.execute("""
                   SELECT start_time, instructor_id 
                   FROM group_lesson 
                   JOIN activity ON activity_id = activity.id
                   WHERE category_id = ? AND start_time = ?""", 
                   (category_id[0], args[3]))
    group_lesson = cursor.fetchone()
    if not group_lesson:
        raise ValueError("Group lesson not found")
    start_time = group_lesson[0]
    instructor_id = group_lesson[1]

    #insert class attendance
    cursor.execute("INSERT INTO group_lesson_arrival (person_id, group_lesson_start_time, group_lesson_instructor_id, time) VALUES (?, ?, ?, datetime('now'))", (person_id[0], start_time, instructor_id))

    return "Class attendance registered successfully"

#Use case 4
def weekly_schedule (args: List, conn: sqlite3.Connection) -> str:
    """
    Returns all group lessons for a given week.

    Args:
        - date: Will return all group lessons seven days starting from given date. Format: YYYY-MM-DD (e.g. 2026-03-15)
    """
    
    if len(args) != 1:
        raise ValueError("Usage: weekly_schedule <YYYY-MM-DD>")
    
    cursor = conn.cursor()
    cursor.execute("""
                    SELECT start_time, category.name, person.first_name
                    FROM group_lesson
                    JOIN activity ON group_lesson.activity_id = activity.id
                    JOIN category ON activity.category_id = category.id
                    JOIN person ON group_lesson.instructor_id = person.id
                    WHERE date(start_time) >= date(?) AND date(start_time) < date(?, '+7 day')
                   )""", (args[0], args[0]))
    rows = cursor.fetchall()
    if not rows:
        return "No group lessons found for given week"
    result = "Group lessons for the week:\n"
    for start_time, category_name, instructor_name in rows:
        result += f"{start_time}: {category_name} with instructor {instructor_name}\n"
    return result


#Use case 5
def visit_history (args: List, conn: sqlite3.Connection) -> str:
    """
    Returns all gym visits and class attendances for a given user. 

    Args:
        - email: The email of the user booking the lesson.
        - phone: The phone number of the user booking the lesson.
        - year: Returns only history for this year. 
    """
    
    if len(args) != 3:
        raise ValueError("Usage: visit_history <email> <phone> <year>")

    #Check if person exists, and fetch person id. 
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM person WHERE email = ? AND phone = ?", (args[0], args[1]))
    person_id = cursor.fetchone()
    if not person_id:
        raise ValueError("User not found")
    
    #Fetch gym visits for given year BRAGE: SKal denne fetche gym visits eller group lesson visits???? ELLER BEGGE??
    cursor.execute("""
                   
                   """)

    return "Function not implementet yet"

#Use case 7
def most_group_lessons (args: List, conn: sqlite3.Connection) -> str:
    """
    Returns the user(s) who has had the most group lessons for a given month.

    Args:
        - month: Month in format YYYY-MM (e.g. 2026-03)
    """

    if len(args) != 1:
        raise ValueError("Usage: most_group_lessons <YYYY-MM>")

    month = args[0]
    if not re.match(r"^\d{4}-(0[1-9]|1[0-2])$", month):
        raise ValueError("Month must be in YYYY-MM format")

    cur = conn.cursor()
    cur.execute(
        """
        SELECT person_id, COUNT(*) as cnt
        FROM group_lesson_arrival
        WHERE substr(time,1,7) = ?
        GROUP BY person_id
        """,
        (month,)
    )
    rows = cur.fetchall()

    if not rows:
        return f"No group lesson attendance records found for {month}."

    max_cnt = max(r[1] for r in rows)
    winner_ids = [r[0] for r in rows if r[1] == max_cnt]

    placeholders = ','.join('?' for _ in winner_ids)
    cur.execute(f"SELECT first_name, last_name FROM person WHERE id IN ({placeholders}) ORDER BY last_name, first_name", tuple(winner_ids))
    names = [f"{fn} {ln}" for fn, ln in cur.fetchall()]

    if len(names) == 1:
        return f"Most group lessons in {month}: {names[0]} ({max_cnt})"
    return f"Most group lessons in {month}: {', '.join(names)} ({max_cnt})"