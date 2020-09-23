from typing import List

from src.models.person import Person
from src.models.drink import Drink
from src.core.table import print_table
from src.core.menu import print_menu

def print_people_table(people: List[Person]):
    data = [person.get_full_name() for person in people]
    print_table('people', data)


def print_people_menu(people: List[Person]):
    data = [person.get_full_name() for person in people]
    print_menu('people', data)


def print_drinks_table(drinks: List[Drink]):
    data = [drink.name for drink in drinks]
    print_table('drinks', data)


def print_drinks_menu(drinks: List[Drink]):
    data = [drink.name for drink in drinks]
    print_menu('drinks', data)


def print_favourites_table(favourites: dict, people: List[Person], drinks: List[Drink]):
    people_dict = {person.id:person for person in people}
    drink_dict = {drink.id:drink for drink in drinks}
    print_table('Favourites', [
        f'{people_dict[person_id].get_full_name()}: {drink_dict[drink_id].name}' for person_id, drink_id in favourites.items()])
