from src.core.output import print_drinks_table

def make_handle_get_drinks(db):
    def handler():
        drinks = db.load_drinks()
        print_drinks_table(drinks)
    return handler
