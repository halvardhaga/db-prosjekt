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


def main():
    support.print_banner()

    # Create DB file with schema if not exists
    if not os.path.exists(HERE.parent / db_path):
        conn = sqlite3.connect(HERE.parent / db_path)
        with open(HERE.parent / "SQL" / "db-creator.sql", 'r') as f:
            sql = f.read()
        conn.executescript(sql)
        conn.close()

    # Main command loop
    while True:
        command_line = input("> ")
        result = dispatcher.dispatch(command_line)
        if result is not None:
            print(result)

if __name__ == "__main__":
    main()