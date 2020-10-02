from src.core.input import select_person_from_menu, select_drink_from_menu
from src.core.menu import select_from_menu


def make_handle_set_favourite_drink(file_db, sql_db):
    def handler():
        people = sql_db.load_people()
        drinks = sql_db.load_drinks()
        favourite_drinks = file_db.load_favourites(people, drinks)

        person = select_person_from_menu(people, 'Choose a person')
        if not person:
            return

        drink = select_drink_from_menu(
            drinks, f'Choose a drink for {person.get_full_name()}')
        if drink is None:
            return

        favourite_drinks[person.id] = drink.id
        file_db.save_favourites(favourite_drinks)
        print(
            f"\nThank you - {person.get_full_name()}'s favourite drink is now {drink.name}")
    return handler
