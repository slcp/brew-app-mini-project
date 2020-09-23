from src.models.person import Person
import uuid

# Can process a list of any objects with an id property
def get_last_id(people: list) -> int:
    last_id = None
    for person in people:
        if last_id == None:
            last_id = person.id
            continue
        if last_id < person.id:
            last_id = person.id
    return last_id

# Functions can return a function - this what is happenening here.
# When a function being returned uses a variable in the upper scope - db in this case it forms
# a closure, this means that the function being returned will keep access to the db variable.
#
# I am doing this here to give the handler access to the database (db) without my main menu
# running in src.app having to a) know about my db and b) having to pass it when calling a handler.
#
# https://www.programiz.com/python-programming/closure
# https://www.w3schools.com/python/python_scope.asp
def make_handle_add_person(db):
    # TODO: Until all handler use a make handler func they need to take one arg as db is
    # passed to all handlers when called
    def handler():
        name = input("What is the name of the user? ")
        parts = name.split(" ", maxsplit=1)
        first_name = parts[0]
        last_name = None if len(parts) != 2 else parts[1]
        people = db.load_people()
        people.append(Person(uuid.uuid1(), first_name, last_name, None))
        db.save_people(people)
    return handler


