from typing import List
#Suman made this change
from src.models.person import Person
from src.models.drink import Drink
from src.core.menu import select_from_menu
from src.core.output import print_people_menu

def select_person_from_menu(people: List[Person], message="Choose a person"):
    options = [person.get_full_name() for person in people]
    index = select_from_menu(message, options, clear=False)
    if index is False:
        return None
    return people[index]


def select_drink_from_menu(drinks: List[Drink], message="Choose a drink"):
    print('drinks: ', drinks)
    options = [drink.name for drink in drinks]
    index = select_from_menu(message, options, clear=False)
    if index is False:
        return None
    return drinks[index]
