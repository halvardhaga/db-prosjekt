"""Contains various handler functions for database-related commands."""

import sqlite3
from typing import List
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent # Absolute path to the directory containing this script.
DB_PATH = HERE.parent / 'database.db' #database file location and name. 

def db_init():
    """Initialize the database, if not already initialized."""
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
    """Clear all data from the database by deleting the database file and recreating it."""
    validation = input("Are you sure you want to nuke the database? This will delete the database file and recreate it. (y/n) ")
    if validation.lower() != "y":
        return "Database nuke cancelled."
    os.remove(DB_PATH)
    db_init()
    return "Database cleared and recreated"

def insert_dummy_data(args: List, conn: sqlite3.Connection) -> str:
    """Insert dummy data into the database (for testing purposes)."""
    with open(HERE.parent / "SQL" / "db-inserter.sql", 'r') as f:
        sql = f.read()
    conn.executescript(sql)
    return "Dummy data inserted"

