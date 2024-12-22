from enum import Enum
from typing import Dict

class Command(Enum):
    ADD = "add"
    CHANGE = "change"
    PHONE = "phone"
    ALL = "all"
    HELLO = "hello"
    EXIT = "exit"
    CLOSE = "close"
    HELP = "help"
    ADD_BIRTHDAY = "add_birthday"
    SHOW_BIRTHDAY = "show_birthday"

COMMAND_DESCRIPTIONS: Dict[Command, str] = {
    Command.ADD: "Add a new contact. Usage: add <name> <phone>",
    Command.CHANGE: "Change an existing contact's phone number. Usage: change <name> <phone>",
    Command.PHONE: "Show the phone number of a contact. Usage: phone <name>",
    Command.ALL: "Show all contacts.",
    Command.HELLO: "Greet the assistant.",
    Command.EXIT: "Exit the assistant.",
    Command.CLOSE: "Exit the assistant.",
    Command.HELP: "Show all available commands.",
    Command.ADD_BIRTHDAY: "Add a birthday to a contact. Usage: add_birthday <name> <birthday> (format: DD.MM.YYYY)", 
    Command.SHOW_BIRTHDAY: "Show the birthday of a contact. Usage: show_birthday <name>"
}