"""Simple terminal app for interacting with the database."""

import sys
import dispatcher
import support
import sqlite3
import os
from pathlib import Path

db_path = 'database.db' #Name of the database file
HERE = Path(__file__).resolve().parent # Absolute path to the directory containing this script

def exit_app(args: list) -> None:
    """Exit the application."""

    print("Goodbye!")
    sys.exit(0)

def db_init():
    """Initialize the database, if not already initialized."""
    if not os.path.exists(HERE.parent / db_path):
        conn = sqlite3.connect(HERE.parent / db_path)
        with open(HERE.parent / "SQL" / "db-creator.sql", 'r') as f:
            sqlschema = f.read()
        conn.executescript(sqlschema)
        with open(HERE.parent / "SQL" / "trigger-creator.sql", 'r') as f:
            sqltrigger = f.read()
        conn.executescript(sqltrigger)
        conn.close()


def main():
    support.print_banner()
    db_init()

    # Main command loop
    while True:
        command_line = input("> ")
        result = dispatcher.dispatch(command_line)
        if result is not None:
            print(result)

if __name__ == "__main__":
    main()