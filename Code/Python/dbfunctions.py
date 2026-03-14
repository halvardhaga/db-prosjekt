"""Contains various handler functions for database-related commands."""

import sqlite3
from typing import List

def init_db(args: List) -> str:
    """Create tables if they don't exist."""
    #TODO
    return "Database initialized"

def clear_db(args: List) -> str:
    """Clear all data from the database (for testing purposes)."""
    valdiation = input("Are you sure you want to clear the database? This action cannot be undone. (y/n) ")
    if valdiation.lower() != "y":
        return "Database clear cancelled."
    #TODO
    return "Database cleared"

def insert_dummy_data(args: List) -> str:
    """Insert some dummy data into the database (for testing purposes)."""
    #TODO
    return "Dummy data inserted"

