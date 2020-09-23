from src.core.input import select_person_from_menu, select_drink_from_menu
from src.core.menu import select_from_menu

def make_handle_set_favourite_drink(db):
    def handler():
        people = db.load_people()
        drinks = db.load_drinks()
        print('handler: ', drinks)
        favourite_drinks = db.load_favourites(people, drinks)
        person = select_person_from_menu(people, 'Choose a person')
        if not person:
            return

        print('handler2: ', drinks)
        drink = select_drink_from_menu(
            drinks, f'Choose a drink for {person.get_full_name()}')
        if drink is None:
            return

        favourite_drinks[person.get_full_name()] = drink.name
        db.save_favourites(favourite_drinks)
        print(
            f"\nThank you - {person.get_full_name()}'s favourite drink is now {drink.name}")
    return handler
