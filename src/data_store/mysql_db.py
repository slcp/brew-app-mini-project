import pymysql

from src.constants import (
    DRINKS_FILE_PATH,
    PEOPLE_FILE_PATH,
    FAVOURITES_FILE_PATH
)
from src.data_store.file_store import File_Store
from src.models.person import Person
from src.models.drink import Drink

PERSON_ID_INDEX = 0
PERSON_FIRST_NAME_INDEX = 1
PERSON_LAST_NAME_INDEX = 2
PERSON_DRINK_NAME_INDEX = 3

DRINK_ID_INDEX = 0
DRINK_NAME_INDEX = 1


class MySQLDB:
    def __init__(self, host='localhost', db_name="brew_app", port=3306, user="user", password="password"):
        self.__host = host
        self.__db_name = db_name
        self.__port = port
        self.__user = user
        self.__password = password

    def __make_connection(self):
        return pymysql.connect(host=self.__host,
                               user=self.__user,
                               password=self.__password,
                               db=self.__db_name,
                               port=self.__port)

    def load_people(self):
        data = []
        connection = self.__make_connection()
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "SELECT * FROM person"
                cursor.execute(sql)
                print(cursor.fetchall())
            connection.commit()
        finally:
            connection.close()
        # for person_data in self.people_store.read_csv():
        #     data.append(Person(
        #         person_data[PERSON_ID_INDEX],
        #         person_data[PERSON_FIRST_NAME_INDEX],
        #         person_data[PERSON_LAST_NAME_INDEX],
        #         person_data[PERSON_DRINK_NAME_INDEX],
        #     ))
        return data

    def save_people(self, people):
        self.people_store.save_to_csv(
            [[person.id, person.first_name, person.last_name, person.drink] for person in people])

    def load_drinks(self):
        data = []
        for drink in self.drinks_store.read_csv():
            print('row')
            data.append(Drink(
                drink[DRINK_ID_INDEX],
                drink[DRINK_NAME_INDEX]
            ))
        return data

    def save_drinks(self, drinks):
        self.drinks_store.save_to_csv(
            [[drink.id, drink.name] for drink in drinks])

    def load_favourites(self, people, drinks):
        data = {}
        people_ids = [person.id for person in people]
        drink_ids = [drink.id for drink in drinks]
        for item in self.favourites_store.read_lines():
            # Unpacking the items in the list to separate variables
            # https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/
            # I know items.split will return a list with two items, because of the second argument
            # it will only split once even if there are more instances of ':' in the string
            #
            # https://www.programiz.com/python-programming/methods/string/split
            # https://docs.python.org/3/library/stdtypes.html?highlight=split#str.rsplit
            person_id, drink_id = item.split(":", 1)
            valid = True
            if person_id not in people_ids:
                valid = False
                print(f'{person_id} is not a known person')
            if drink_id not in drink_ids:
                valid = False
                print(f'{drink_id} is not a known drink')
            if not valid:
                continue
            data[person_id] = drink_id
        return data

    def save_favourites(self, favourites):
        # Save favourites
        # Defining a consistent structure here so that I can parse/recognise it when loading
        # f'{name}:{drink}'
        # TODO: Save as a CSV?
        self.favourites_store.save_lines(
            [f'{person_id}:{drink_id}' for person_id, drink_id in favourites.items()])