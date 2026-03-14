"""Contains various handler functions for database-related commands."""

import sqlite3

from pathlib import Path
import app
from typing import List
import os
    

def nuke(args: List, conn: sqlite3.Connection) -> str:
    """Clear all data from the database by deleting the database file and recreating it."""
    validation = input("Are you sure you want to nuke the database? This will delete the database file and recreate it. (y/n) ")
    if validation.lower() != "y":
        return "Database nuke cancelled."
    
    conn.close()
    os.remove(app.HERE.parent / app.db_path)
    conn = sqlite3.connect(app.HERE.parent / app.db_path)
    with open(app.HERE.parent / "SQL" / "db-creator.sql", 'r') as f:
        sql = f.read()
    conn.executescript(sql)
    return "Database cleared and recreated"

def insert_dummy_data(args: List, conn: sqlite3.Connection) -> str:
    """Insert dummy data into the database (for testing purposes)."""
    with open(app.HERE.parent / "SQL" / "db-inserter.sql", 'r') as f:
        sql = f.read()
    conn.executescript(sql)
    return "Dummy data inserted"

