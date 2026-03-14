"""Contains various support functions not critical to the funcitonality of the app"""

import app
import dispatcher

def print_banner() -> None:
    """Prints a startup banner."""

    banner = r"""
  _________.______________ ________          __        ___.                         
 /   _____/|   \__    ___/ \______ \ _____ _/  |______ \_ |__ _____    ______ ____  
 \_____  \ |   | |    |     |    |  \\__  \\   __\__  \ | __ \\__  \  /  ___// __ \ 
 /        \|   | |    |     |    `   \/ __ \|  |  / __ \| \_\ \/ __ \_\___ \\  ___/ 
/_______  /|___| |____|    /_______  (____  /__| (____  /___  (____  /____  >\___  >
        \/                         \/     \/          \/    \/     \/     \/     \/ 

Simple terminal app for interacting with SIT database – type "help" for a list of commands.
"""

    print(banner)


def show_help(args: list) -> None:
    """Shows available commands or detailed help for a specific command."""

    if not args:
        # No arguments: show list of commands
        print("Available commands:")
        for cmd in sorted(dispatcher.COMMANDS):
            print(f"  {cmd}")
        print("For more detailed help, type \"help <command>\".")

    else:
        # First argument: show detailed help for that command
        command = args[0].lower()
        if command == "help":
            print("help: Shows available commands or detailed help for a specific command.")
            print("Usage: help [command]")
        elif command == "exit":
            print("exit: Exits the application.")
            print("Usage: exit")
        else:
            print(f"No detailed help available for '{command}'. Type 'help' for a list of commands.")