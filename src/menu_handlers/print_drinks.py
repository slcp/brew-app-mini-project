from src.core.table import print_table

def make_handle_get_drinks(db):
    def handler():
        drinks = db.load_drinks()
        print_table('drinks', drinks)
    return handler
