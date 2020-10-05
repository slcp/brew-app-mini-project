from src.core.main import build_round
from src.models.round import Round
from src.core.input import select_person_from_menu
from src.core.menu import clear_screen


def make_handle_start_round(file_db, sql_db):
    def handler():
        people = sql_db.load_people()
        drinks = sql_db.load_drinks()
        favourite_drinks = file_db.load_favourites(people, drinks)
        # Whose round is it?
        person = select_person_from_menu(people, 'Whose round is this?')
        if not person:
            print("Please choose a number from the menu")
            handler()

        # Create round with owner, get user input to add drinks to the round
        round = build_round(Round(person), favourite_drinks, people, drinks)

        clear_screen()
        print(f'Time for you to make some drinks {person.get_full_name()}\n')
        round.print_order()
    return handler
