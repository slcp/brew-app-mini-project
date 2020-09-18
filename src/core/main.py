import os
from typing import Dict, List

from src.constants import (
    DRINKS_FILE_PATH,
    PEOPLE_FILE_PATH,
    FAVOURITES_FILE_PATH,
    DRNIKS_MENU_USUAL_OPTION
)
from src.data_store.files import read_lines, save_lines
from src.models.round import Round
from src.core.menu import select_from_menu, clear_screen
from src.core.table import print_table


def load_data(people: list, drinks: list, favourites: dict):
    # Load people
    for person in read_lines(PEOPLE_FILE_PATH):
        people.append(person)
    # Load drinks
    for drink in read_lines(DRINKS_FILE_PATH):
        drinks.append(drink)
    # Load favourites
    for item in read_lines(FAVOURITES_FILE_PATH):
        # Unpacking the items in the list to separate variables
        # https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/
        # I know items.split will return a list with two items, because of the second argument
        # it will only split once even if there are more instances of ':' in the string
        #
        # https://www.programiz.com/python-programming/methods/string/split
        # https://docs.python.org/3/library/stdtypes.html?highlight=split#str.rsplit
        name, drink = item.split(":", 1)
        if name in people and drink in drinks:
            favourites[name] = drink
        else:
            print('Unexpected data returned when loading favourites.')
            print(f'Drink "{drink}" is known: {drink in drinks}')
            print(f'Name "{name}" is known: {name in people}')


def save_data(people: list, drinks: list, favourites: dict):
    # Save people
    save_lines(PEOPLE_FILE_PATH, people)
    # Save drinks
    save_lines(DRINKS_FILE_PATH, drinks)
    # Save favourites
    # Defining a consistent structure here so that I can parse/recognise it when loading
    # f'{name}:{drink}'
    save_lines(FAVOURITES_FILE_PATH, [
               f'{name}:{drink}' for name, drink in favourites.items()])


def get_available_drinks_for_round(favourites, drinks, name):
    if name in favourites.keys():
        return drinks + [DRNIKS_MENU_USUAL_OPTION]
    else:
        return drinks


def build_round(round: Round, favourites: Dict, people: List[str], drinks: List[str]):
    while True:
        clear_screen()
        round.print_order()
        # Set name, drink and finish to the same value, None
        name = drink = finish = None
        while not name:
            name = select_from_menu('\nWhose drink would like to set?', people, clear=False)
            if name is False:
                print("Please choose a number from the menu")

        # If the person has a stored favourite drink add an option to the drinks menu
        available_drinks = get_available_drinks_for_round(favourites, drinks, name)

        while not drink:
            drink = select_from_menu(
                f'Please choose a drink for {name}', available_drinks)
            if drink is False:
                print("Please choose a number from the menu")

        if drink == DRNIKS_MENU_USUAL_OPTION:
            drink = favourites[name]
        round.add_to_round(favourites, name, drink=drink)
        clear_screen()

        # Ask to add another order with end round option
        while not finish:
            round.print_order()
            finish = select_from_menu('\nDo you want to add another drink?', ['Yes', 'No'], clear=False)
            if finish is False:
                print("Please choose a number from the menu")
            if finish == "No":
                return round
