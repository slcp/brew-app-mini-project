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

PERSON_TABLE = "person"

PERSON_ID_COLUMN = "person_id"
PERSON_FIRST_NAME_COLUMN = "first_name"
PERSON_LAST_NAME_COLUMN = "surname"
PERSON_AGE_COLUMN = "age"

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
                sql = f'SELECT * FROM {PERSON_TABLE}'
                cursor.execute(sql)
                while True:
                    person_data = cursor.fetchone()
                    if not person_data:
                        break
                    data.append(Person(
                                person_data[PERSON_ID_INDEX],
                                person_data[PERSON_FIRST_NAME_INDEX],
                                person_data[PERSON_LAST_NAME_INDEX],
                                person_data[PERSON_DRINK_NAME_INDEX],
                                ))
            connection.commit()
        finally:
            connection.close()
        return data

    def insert_person(self, person):
        connection = self.__make_connection()
        try:
            with connection.cursor() as cursor:
                data = [str(person.id), person.first_name,
                        person.last_name, person.age]
                sql = f'INSERT INTO {PERSON_TABLE} ({PERSON_ID_COLUMN}, {PERSON_FIRST_NAME_COLUMN}, \
                    {PERSON_LAST_NAME_COLUMN}, {PERSON_AGE_COLUMN}) VALUES (%s, %s, %s, %s)'
                cursor.execute(sql, data)
                connection.commit()
        finally:
            connection.close()

    # Save drinks - match input/output to save to file drinks function

    def insert_drink(self, drink):
        connection = self.__make_connection()
        try:
            with connection.cursor() as cursor:
                data = [drink.id, drink.name]
                sql = 'INSERT INTO drink (id, name) VALUES (%s, %s)'
                cursor.execute(sql, data)
                connection.commit()
        except:
             # Handle error
             pass
        finally:
            connection.close()
