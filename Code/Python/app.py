"""Simple terminal app for interacting with the database."""

import sys
import dispatcher
import support


def exit_app(args: list) -> None:
    """Exit the application."""

    print("Goodbye!")
    sys.exit(0)


def main():
    support.print_banner()

    while True:
        command_line = input("> ")
        dispatcher.dispatch(command_line)

if __name__ == "__main__":
    main()