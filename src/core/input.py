from typing import List

from src.models.person import Person
from src.core.menu import select_from_menu
from src.core.output import print_people_menu

def select_person_from_menu(people: List[Person], message="Choose a person"):
    options = [person.name for person in people]
    index = select_from_menu(message, options, clear=False)
    if index is False:
        return None
    return people[index]
