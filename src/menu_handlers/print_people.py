from src.core.output import print_people_table


# See src.menu_handlers.add_person for comments on what is happening here
def make_handle_get_people(file_db, sql_db):
    def handler():
        people = sql_db.load_people()
        print_people_table(people)
    return handler
