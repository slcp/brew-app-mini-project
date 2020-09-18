from typing import List

from src.models.person import Person
from src.core.table import print_table
from src.core.menu import print_menu

def print_people_table(people: List[Person]):
    data = [person.name for person in people]
    print_table('people', data)


def print_people_menu(people: List[Person]):
    data = [person.name for person in people]
    print_menu('people', data)
