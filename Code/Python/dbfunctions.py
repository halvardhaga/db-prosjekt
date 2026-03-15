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

def book_lesson (args: List, conn: sqlite3.Connection) -> str:
    """
    Create booking for group lesson.

    Args:
        - username: 
        - activity:
        - time:
    """
    #TODO
    return "Function not implementet yet"

#Use case 3
def attend_gym (args: List, conn: sqlite3.Connection) -> str:
    """
    Registers that given user attended given gym at current time. 

    Args:
        - username: 
        - gym:
    """
    #TODO
    return "Function not implementet yet"

#Use case 3
def attend_class (args: List, conn: sqlite3.Connection) -> str:
    """
    Registers that given user attended given class at current time. 

    Args:
        - username: 
        - class:
    """
    #TODO
    return "Function not implementet yet"

#Use case 4
def weekly_schedule (args: List, conn: sqlite3.Connection) -> str:
    """
    Returns all group lessons for a given week.

    Args:
        - week: In the format YYYY-WW
    """
    #TODO
    return "Function not implementet yet"

#Use case 5
def visit_history (args: List, conn: sqlite3.Connection) -> str:
    """
    Returns all gym visits and class attendances for a given user. 

    Args:
        - username:
        - year: Optional, if not given, returns all history. If given, returns only history for that year.
    """
    #TODO
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