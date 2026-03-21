"""Contains various support functions not critical to the funcitonality of the app"""

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
        elif command == "nuke":
            print("nuke: Clears the database by deleting the file and recreating the schema.")
            print("Usage: nuke")
        elif command == "insert_dummy_data":
            print("insert_dummy_data: Inserts dummy data into the database from db-inserter.sql. For testing purposes.")
            print("Usage: insert_dummy_data")
        elif command == "book_lesson":
            print("book_lesson: Creates a booking for a group lesson.")
            print("Usage: book_lesson <email> <phone> <category> <time>")
            print("  category: e.g. yoga, spinning")
            print("  time: YYYY-MM-DD HH:MM (e.g. 2026-03-15 18:30)")
        elif command == "attend_gym":
            print("attend_gym: Registers that a user attended a gym at the current time.")
            print("Usage: attend_gym <email> <phone> <gym>")
            print("  gym: Name or ID of the gym.")
        elif command == "attend_class":
            print("attend_class: Registers that a user attended a group lesson at the current time.")
            print("Usage: attend_class <email> <phone> <category> <time>")
            print("  category: e.g. yoga, spinning")
            print("  time: YYYY-MM-DD HH:MM (e.g. 2026-03-15 18:30)")
        elif command == "weekly_schedule":
            print("weekly_schedule: Returns all group lessons for the 7-day period starting from a given date.")
            print("Usage: weekly_schedule <date>")
            print("  date: YYYY-MM-DD (e.g. 2026-03-15)")
        elif command == "visit_history":
            print("visit_history: Returns all gym visits and class attendances for a given user in a given year.")
            print("Usage: visit_history <email> <phone> <year>")
        elif command == "most_group_lessons":
            print("most_group_lessons: Returns the user(s) with the most group lesson attendances in a given month.")
            print("Usage: most_group_lessons <month>")
            print("  month: YYYY-MM (e.g. 2026-03)")
        else:
            print(f"No detailed help available for '{command}'. Type 'help' for a list of commands.")