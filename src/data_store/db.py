from src.constants import (
    DRINKS_FILE_PATH,
    PEOPLE_FILE_PATH,
    FAVOURITES_FILE_PATH
)
from src.data_store.file_store import File_Store
from src.models.person import Person

PERSON_ID_INDEX = 0
PERSON_FIRST_NAME_INDEX = 1
PERSON_LAST_NAME_INDEX = 2
PERSON_DRINK_NAME_INDEX = 3

class FileDB:
    def __init__(self, people_path, drinks_path, favourites_path):
        self.people_store = File_Store(people_path)
        self.drinks_store = File_Store(drinks_path)
        self.favourites_store = File_Store(favourites_path)


    def load_people(self):
        data = []
        for person_data in self.people_store.read_csv():
            data.append(Person(
                person_data[PERSON_ID_INDEX],
                person_data[PERSON_FIRST_NAME_INDEX],
                person_data[PERSON_LAST_NAME_INDEX],
                person_data[PERSON_DRINK_NAME_INDEX],
            ))
        return data

    def save_people(self, people):
        self.people_store.save_to_csv(
            [[person.id, person.first_name, person.last_name, person.drink] for person in people])

    def load_drinks(self):
        data = []
        for drink in self.drinks_store.read_lines():
            data.append(drink)
        return data

    def save_drinks(self, drinks):
        self.drinks_store.save_lines(drinks)

    def load_favourites(self, people, drinks):
        data = {}
        people_names = [person.get_full_name() for person in people]
        for item in self.favourites_store.read_lines():
            # Unpacking the items in the list to separate variables
            # https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/
            # I know items.split will return a list with two items, because of the second argument
            # it will only split once even if there are more instances of ':' in the string
            #
            # https://www.programiz.com/python-programming/methods/string/split
            # https://docs.python.org/3/library/stdtypes.html?highlight=split#str.rsplit
            name, drink = item.split(":", 1)
            valid = True
            if name not in people_names:
                valid = False
                print(f'{name} is not a known person')
            if drink not in drinks:
                valid = False
                print(f'{drink} is not a known drink')
            if not valid:
                continue
            data[name] = drink
        return data

    def save_favourites(self, favourites):
        # Save favourites
        # Defining a consistent structure here so that I can parse/recognise it when loading
        # f'{name}:{drink}'
        # TODO: Save as a CSV?
        self.favourites_store.save_lines(
            [f'{name}:{drink}' for name, drink in favourites.items()])
