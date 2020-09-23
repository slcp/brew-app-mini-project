from src.core.table import print_table

def make_handle_view_favourites(db):
    def handler():
        people = db.load_people()
        drinks = db.load_drinks()
        favourite_drinks = db.load_favourites(people, drinks)
        # Using list comprehension to loop through favourites dictionary (dict.items())
        # Using tuple unpacking to dict (key, value) pairs into separate name, drink variables
        # Creating a list where each item is the result of f'{name}: {drink}'
        print_table('Favourites', [
                    f'{name}: {drink}' for name, drink in favourite_drinks.items()])
    return handler
