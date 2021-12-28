"""
common > util > consolehelpers

Contains helper functions for interacting with the script through the
console, which may assist in debugging.

Authors:
* Miguel Guthridge [hdsq@outlook.com.au]
"""

__all__ = [
    'help',
    'credits',
    'log'
]

import common

from logger import log

class ConsoleCommand:
    """
    Allows a printout to be generated when a user types a command
    """
    
    def __init__(self, printout: str) -> None:
        self.printout = printout
    
    def __repr__(self) -> str:
        return self.printout

    def __call__(self) -> None:
        print(self)

help = ConsoleCommand(
    f"Universal Controller Script\n"
    f"Version: {common.consts.getVersionString()}\n"
    f"---------------------------\n"
    f"For documentation, visit the project's GitHub:\n"
    f"  {common.consts.WEBSITE}\n"
    f"To speak to a human, join our Discord server:\n"
    f"  {common.consts.DISCORD}\n"
    f"---------------------------\n"
    f"List of commands (enter into the console to use it):\n"
    f" * help(): display this message\n"
    f" * log(): log a message\n"
    f"    * log.recall(category): recall log entries from a category\n"
    f"    * log.details(entry_number): print info about a log entry\n"
    f" * credits(): print credits for the script\n"
    f" * reset(): reset the script and reload modular components\n"
)

# Damn this is an awful way of formatting this, but I can't think of anything
# better
_newline = '\n'
_credit_str = "\n".join(
    f"{key}:{_newline}{_newline.join([f' * {p}' for p in value])}"
        for key, value in common.consts.AUTHORS.items()
)
credits = ConsoleCommand(
    f"Credits:\n"
    f"{_credit_str}\n"
    f"---------------------------\n"
    f"This project is free and open source, under the GNU GPL v3 License.\n"
    f"A copy of this is available in the file 'LICENSE'.\n"
)