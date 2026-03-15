"""Simple terminal app for interacting with the database."""

import sys
import dispatcher
import support
import dbfunctions

def exit_app(args: list) -> None:
    """Exit the application."""

    print("Goodbye!")
    sys.exit(0)

def main():
    support.print_banner()
    dbfunctions.db_init()

    # Main command loop
    while True:
        command_line = input("> ")
        result = dispatcher.dispatch(command_line)
        if result is not None:
            print(result)

if __name__ == "__main__":
    main()