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
from src.models.person import Person
from src.core.menu import select_from_menu, clear_screen
from src.core.table import print_table
from src.core.input import select_person_from_menu


def load_data(people: list, drinks: list, favourites: dict):
    # Load people
    for person in read_lines(PEOPLE_FILE_PATH):
        people.append(Person(person))
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
        valid = True
        if name not in [person.name for person in people]:
            valid = False
            print(f'{name} is not a known person')
        if drink not in drinks:
            valid = False
            print(f'{drink} is not a known drink')
        if not valid:
            continue
        
        favourites[name] = drink


def save_people(people: List[Person]):
    data = [person.name for person in people]
    save_lines(PEOPLE_FILE_PATH, data)


def save_data(people: list, drinks: list, favourites: dict):
    # Save people
    save_people(people)
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
        person = drink = finish = None
        while not person:
            person = select_person_from_menu(
                people, '\nWhose drink would like to set?')
            if not person:
                print("Please choose a number from the menu")

        # If the person has a stored favourite drink add an option to the drinks menu
        available_drinks = get_available_drinks_for_round(favourites, drinks, person.name)

        while not drink:
            index = select_from_menu(
                f'Please choose a drink for {person.name}', available_drinks)
            if index is False:
                print("Please choose a number from the menu")
            drink = drinks[index]

        if drink == DRNIKS_MENU_USUAL_OPTION:
            drink = favourites[person.name]
        round.add_to_round(favourites, person.name, drink=drink)
        clear_screen()

        # Ask to add another order with end round option
        while not finish:
            round.print_order()
            options = ['Yes', 'No']
            index = select_from_menu('\nDo you want to add another drink?', options, clear=False)
            if index is False:
                print("Please choose a number from the menu")
            if options[index] == "No":
                return round
