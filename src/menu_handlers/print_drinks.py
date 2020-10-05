from src.core.output import print_drinks_table


def make_handle_get_drinks(file_db, sql_db):
    def handler():
        drinks = sql_db.load_drinks()
        print_drinks_table(drinks)
    return handler
