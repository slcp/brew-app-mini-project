import os
from typing import Dict, List

from src.constants import (
    DRNIKS_MENU_USUAL_OPTION
)
from src.models.round import Round
from src.models.person import Person
from src.models.drink import Drink
from src.core.menu import select_from_menu, clear_screen
from src.core.table import print_table
from src.core.input import select_person_from_menu, select_drink_from_menu


def get_available_drinks_for_round(favourites, drinks, person):
    if person.id in favourites.keys():
        # This is a bit nasty but we need to a list of drinks
        return drinks + [Drink(DRNIKS_MENU_USUAL_OPTION, DRNIKS_MENU_USUAL_OPTION)]
    else:
        return drinks


def build_round(round: Round, favourites: Dict, people: List[Person], drinks: List[Round]):
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
            favourites, drinks, person)

        while not drink:
            drink = select_drink_from_menu(
                available_drinks, f'Please choose a drink for {person.get_full_name()}')
            if not drink:
                print("Please choose a number from the menu")

        if drink.id == DRNIKS_MENU_USUAL_OPTION:
            drink = [drink for drink in drinks if drink.id == favourites[person.id]][0]
        round.add_to_round(favourites, person, drink=drink)
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
