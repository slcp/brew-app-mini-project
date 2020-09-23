import os
from typing import Dict, List

from src.constants import (
    DRNIKS_MENU_USUAL_OPTION
)
from src.models.round import Round
from src.models.person import Person
from src.core.menu import select_from_menu, clear_screen
from src.core.table import print_table
from src.core.input import select_person_from_menu


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
        available_drinks = get_available_drinks_for_round(
            favourites, drinks, person.get_full_name())

        while not drink:
            index = select_from_menu(
                f'Please choose a drink for {person.get_full_name()}', available_drinks)
            if index is False:
                print("Please choose a number from the menu")
            drink = drinks[index]

        if drink == DRNIKS_MENU_USUAL_OPTION:
            drink = favourites[person.get_full_name()]
        round.add_to_round(favourites, person.get_full_name(), drink=drink)
        clear_screen()

        # Ask to add another order with end round option
        while not finish:
            round.print_order()
            options = ['Yes', 'No']
            index = select_from_menu(
                '\nDo you want to add another drink?', options, clear=False)
            if index is False:
                print("Please choose a number from the menu")
                continue
            if options[index] == "No":
                return round
            break
