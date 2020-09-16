import os

from src.constants import DRINKS_FILE_PATH, PEOPLE_FILE_PATH, FAVOURITES_FILE_PATH
from src.data_store.files import read_lines, save_lines


def clear_screen():
    os.system('clear')

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
