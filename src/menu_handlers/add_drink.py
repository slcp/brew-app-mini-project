import uuid

from src.models.drink import Drink

# See src.menu_handlers.add_person for comments on what is happening here
def make_handle_add_drink(file_db, sql_db):
    def handler():
        drinks = file_db.load_drinks()
        drink = input("What is the name of the drink? ")
        drinks.append(Drink(uuid.uuid1(), drink))
        file_db.save_drinks(drinks)
    return handler
