from src.core.input import select_person_from_menu
from src.core.menu import select_from_menu

def make_handle_set_favourite_drink(db):
    def handler():
        people = db.load_people()
        drinks = db.load_drinks()
        favourite_drinks = db.load_favourites(people, drinks)
        person = select_person_from_menu(people, 'Choose a person')
        if not person:
            return

        index = select_from_menu(
            f'Choose a drink for {person.get_full_name()}', drinks)
        if index is False:
            return
        drink = drinks[index]

        favourite_drinks[person.get_full_name()] = drink
        db.save_favourites(favourite_drinks)
        print(
            f"\nThank you - {person.get_full_name()}'s favourite drink is now {drink}")
    return handler
