from src.models.person import Person

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

def make_handle_add_person(db):
    # TODO: Until all handler use a make handler func they need to take one arg as db is
    # passed to all handlers when called
    def handler(_):
        name = input("What is the name of the user? ")
        parts = name.split(" ", maxsplit=1)
        first_name = parts[0]
        last_name = None if len(parts) != 2 else parts[1]
        people = db.load_people()
        last_id = get_last_id(people)
        people.append(Person(last_id + 1, first_name, last_name, None))
        db.save_people(people)
    return handler


