"""Contains dispatcher function, which reads input line and dipatches to correct handler function."""

from typing import Dict, Callable, List, Any
import app
import support
import dbfunctions
import sqlite3

#Defines all allowable commands and their handler functions.
COMMANDS: Dict[str, Callable[[List[str]], str]] = {
    "help": support.show_help,
    "exit": app.exit_app,
    "nuke": dbfunctions.nuke,
    "insert_dummy_data": dbfunctions.insert_dummy_data,
    "book_lesson": dbfunctions.book_lesson,
    "attend_gym": dbfunctions.attend_gym,
    "attend_class": dbfunctions.attend_class,
    "weekly_schedule": dbfunctions.weekly_schedule,
    "visit_history": dbfunctions.visit_history,
    "most_group_lessons": dbfunctions.most_group_lessons
} 

def dispatch(command_line: str) -> str:
    """Parse a command line and dispatch to correct handler. Returns results.
    If command is database related, a connection is established and passed to the handler function, then closed. 
    If command is unknown, prints error message and returns None."""

    parts = command_line.split()
    command = parts[0].lower()
    args = parts[1:]

    if command not in COMMANDS:
        print(f"Unknown command: {command} – type \"help\" for a list of commands.")
        return None

    if COMMANDS[command].__module__ == 'dbfunctions':
        #Database command
        con = sqlite3.connect(dbfunctions.DB_PATH)
        result = COMMANDS[command](args, con)
        con.close()
        return result
    else:
        #App command
        return COMMANDS[command](args)