from src.core.output import print_favourites_table


def make_handle_view_favourites(file_db, sql_db):
    def handler():
        people = sql_db.load_people()
        drinks = sql_db.load_drinks()
        favourite_drinks = file_db.load_favourites(people, drinks)
        print_favourites_table(favourite_drinks, people, drinks)
    return handler
