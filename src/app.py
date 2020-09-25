import os
from typing import List

from src.constants import (
    DRINKS_FILE_PATH,
    PEOPLE_FILE_PATH,
    FAVOURITES_FILE_PATH,
    APP_NAME,
    VERSION,
    DRNIKS_MENU_USUAL_OPTION
)
from src.core.table import print_table
from src.core.main import build_round
from src.core.menu import clear_screen, select_from_menu, get_numeric_menu_input
from src.models.round import Round
from src.models.person import Person
from src.core.output import print_people_table
from src.core.input import select_person_from_menu
from src.data_store.db import FileDB
from src.menu_handlers.add_person import make_handle_add_person
from src.menu_handlers.add_drink import make_handle_add_drink
from src.menu_handlers.print_people import make_handle_get_people
from src.menu_handlers.print_drinks import make_handle_get_drinks
from src.menu_handlers.add_favourite import make_handle_set_favourite_drink
from src.menu_handlers.view_favourites import make_handle_view_favourites
from src.menu_handlers.make_round import make_handle_start_round

# Input helper funcs
def wait():
    input('\nPress any key to return to the main menu')


# Menu handlers
def handle_exit():
    print('Saving data...')
    print(f'Thank you for using {APP_NAME}')
    exit()


# Menu config
# lambdas fake a make handler func when one is not required
menu_config = [
    {'menu_option': 1, 'menu_text': 'Get all people', 'handler': make_handle_get_people},
    {'menu_option': 2, 'menu_text': 'Get all drinks', 'handler': make_handle_get_drinks},
    {'menu_option': 3, 'menu_text': 'Add a person',
        'handler': make_handle_add_person},
    {'menu_option': 4, 'menu_text': 'Add a drink',
        'handler': make_handle_add_drink},
    {'menu_option': 5, 'menu_text': 'Set a favourite drink',
        'handler': make_handle_set_favourite_drink},
    {'menu_option': 6, 'menu_text': 'View favourites',
        'handler': make_handle_view_favourites},
    {'menu_option': 7, 'menu_text': 'Start a round',
        'handler': make_handle_start_round},
    {'menu_option': 8, 'menu_text': 'Exit', 'handler': lambda x: handle_exit},
]


# CLI menu
# Using list comprehension to loop through menu_config and create lines that read
# [1] Option 1
# [2] Option 2
# etc.
def make_menu(config: List[dict]):
    # Backslash "\" is not allowed in in a f-string f'{python} some string' so defining
    # a new line character in variable here to use in the f-string below
    new_line = "\n"
    return f'''
Welcome to {APP_NAME} v{VERSION}!
Please, select an option by entering a number:

{new_line.join([f'[{item.get("menu_option")}] {item.get("menu_text")}' for item in config])}
'''


MENU_TEXT = make_menu(menu_config)


# App
def run_menu(handlers=None): 
    # Enter an infinite loop - the exit option calls exit() which will kill the program
    while True:
        clear_screen()
        print(MENU_TEXT)

        # Ask the user to choose an item from the menu - we want a number
        option = get_numeric_menu_input('Enter your selection:')
        if not option:
            wait()
            continue

        # Find item in menu_config that matches input
        #
        # (item for item in menu_config if item.get('menu_option') == option) list comprehension
        # to create a list all menu_config items that match user inputted option - there should only be one
        #
        # next(list, default_value) - get the next/first item in the list, or None if it is empty
        #
        # https: // www.programiz.com/python-programming/methods/built-in/next
        # https://docs.python.org/3/library/functions.html#next
        option_config = next(
            (item for item in handlers if item.get('id') == option), None)

        # Handle unknown args
        if option_config is None:
            print(f'\n"{option}" is not an option that I recognise')
            wait()
            continue

        # Invoke handler
        option_config.get('handler')()
        wait()
        continue


def start():
    db = FileDB(PEOPLE_FILE_PATH, DRINKS_FILE_PATH, FAVOURITES_FILE_PATH)
    # Loop through the menu_config and build call each handler with the db - eventually these will be funcs
    # that closure over the db and return a handler to be invoked by the menu
    menu_handlers = [{
            "id": config["menu_option"],
            "handler": config["handler"](db)
        } for config in menu_config]
    run_menu(handlers=menu_handlers)


# When this file is run from terminal/cli  as a module __name__ is set to "__main__"
# eg. python -m src.app
# When the file is imported (eg. import app) __name__ is NOT set to "__main__"
# fbgdbgbgf
# Great resource explaining Python modules/packages - https://alex.dzyoba.com/blog/python-import/
if __name__ == "__main__":
    start()

# This was made on test-branch