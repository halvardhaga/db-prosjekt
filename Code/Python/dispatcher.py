"""Contains dispatcher function, which reads input line and dipatches to correct handler function."""

from typing import Dict, Callable, List, Any
import app
import support
import dbfunctions

#Defines all allowable commands and their handler functions.
COMMANDS: Dict[str, Callable[[List[str]], Any]] = {
    "help": support.show_help,
    "exit": app.exit_app,
} 

def dispatch(command_line: str) -> Any:
    """Parse a command line and dispatch to correct handler. Returns results."""

    parts = command_line.split()
    command = parts[0].lower()
    args = parts[1:]

    if command not in COMMANDS:
        print(f"Unknown command: {command} – type \"help\" for a list of commands.")
        return

    return COMMANDS[command](args)