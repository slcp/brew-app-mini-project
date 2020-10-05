import os

# Define data
# Menu options
EXIT_ARG = 1
GET_PEOPLE_ARG = 2
GET_DRINKS_ARG = 3
ADD_PERSON_ARG = 4
ADD_DRINK_ARG = 5
SET_FAVOURITE_ARG = 6
VIEW_FAVOURITES_ARG = 7
START_ROUND_ARG = 8

# CLI menu
APP_NAME = 'BrIW'
VERSION = '0.1'
MENU_TEXT = f'''
Welcome to {APP_NAME} v{VERSION}!
Please, select an option by entering a number:

[1] Exit
[2] Get all people
[3] Get all drinks
[4] Add a person
[5] Add a drink
[6] Set a favourite drink
[7] View favourites
[8] Start a round
'''

# App data
DRINKS_FILE_PATH = './data/drinks.txt'
PEOPLE_FILE_PATH = './data/people.txt'
FAVOURITES_FILE_PATH = './data/favourites.txt'
drinks = []
people = []
favourite_drinks = {}


# Table output helper funcs
def get_table_width(title, data):
    longest = len(title)
    additional_spacing = 2
    for item in data:
        if len(item) > longest:
            longest = len(item)
    return longest + additional_spacing


def print_table_body(contents):
    for item in contents:
        print(f'| {item}')


def print_divider(length):
    print(f'+{"=" * length}+')


def print_table_header(title, width):
    print_divider(width)
    print(f'| {title.upper()}')
    print_divider(width)


def print_table_footer(width):
    print_divider(width)


def print_table(title, contents):
    width = get_table_width(title, contents)
    print_table_header(title, width)
    print_table_body(contents)
    print_table_footer(width)


def clear_screen():
    os.system('clear')


def print_main_menu():
    clear_screen()
    print(MENU_TEXT)


# Input helper funcs
def get_menu_input(message):
    try:
        return int(input(f'{message} '))
    except ValueError:
        output("Menu items - numbers are the only input I understand")
        wait()
        return False


def get_raw_input(message):
    return input(f'{message} ')


def wait():
    input('\nPress any key to return to the main menu')


# Output helper funcs
def output(text):
    print(f'\n{text}')


def print_people():
    print_table('people', people)


def print_drinks():
    print_table('drinks', drinks)


def print_menu(title, data):
    items = []
    # enumerate() will produce the index/position in the list and the item in
    # the list for use within your loop. If you are not interested in knowing
    # what position you are at in the list then you wouldn't want to use
    # enumerate()
    for i, item in enumerate(data):
        items.append(f'[{i}] {item}')
    clear_screen()
    print(f'{title}\n')
    print('\n'.join(items), '\n')


def print_favourites(data):
    items = []
    for name, drink in data.items():
        items.append(f'{name}: {drink}')
    print_table('Favourites', items)


# Input helper funcs
def validate_menu_input(index, data):
    if index < 0 or index >= len(data):
        print(f'"{index}" is not a valid option from that menu\n')
        wait()
        return False
    return data[index]


def select_from_menu(message, data):
    print_menu(message, data)
    selection = get_menu_input(f'{message} ')
    return validate_menu_input(selection, data)


# Data persistence helper funcs
def exit_with_error(e, msg=None):
    msg = msg if msg else 'Something went wrong'
    print(f'{msg} with error: {str(e)} - exiting')
    exit()


def load_from_file(path):
    data = []
    try:
        with open(path, 'r') as file:
            for line in file.readlines():
                # Check if empty - bail/stop/valdiate as early as possible
                if line == '':
                    continue
                # Trim newline/whitespace
                # Add to data
                data.append(line.strip())
    except FileNotFoundError as e:
        exit_with_error(e, f'File "{path}" cannot be found')
    except Exception as e:
        exit_with_error(e, f'Unable to open file "{path}"')
    return data


def load_favourites(people, drinks):
    for item in load_from_file(FAVOURITES_FILE_PATH):
        # Unpacking the items in the list to separate variables
        # https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/
        # I know items.split will return a list with two items, because of the second argument
        # it will only split once even if there are more instances of ':' in the string
        name, drink = item.split(":", 1)
        if name in people and drink in drinks:
            favourite_drinks[name] = drink
        else:
            print('Unexpected data returned when loading favourites.')
            print(f'Drink is known: {drink in drinks}')
            print(f'Name is known: {name in people}')


def load_data():
    for person in load_from_file(PEOPLE_FILE_PATH):
        people.append(person)
    for drink in load_from_file(DRINKS_FILE_PATH):
        drinks.append(drink)
    load_favourites(people, drinks)


def save_to_file(path, data):
    try:
        with open(path, 'w') as file:
            # List comprehension - make a new list from an list
            # https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
            # There are other ways to this but list comprehension
            # is an idiomatic use of python
            file.writelines([f'{item}\n' for item in data])
    except FileNotFoundError as e:
        exit_with_error(e, f'File "{path}" cannot be found')
    except Exception as e:
        exit_with_error(e, f'Unable to open file "{path}"')


def save_favourites(data):
    items = []
    for item in data.items():
        name, drink = item
        # Defining a consistent structure here so that I can parse/recognise it when loading
        items.append(f'{name}:{drink}')
    save_to_file(FAVOURITES_FILE_PATH, items)


# Menu option handlers
def handle_set_favourite_drink():
    person = select_from_menu('Choose a person', people)
    if person is False:
        wait()
        return

    drink = select_from_menu(f'Choose a drink for {person}', drinks)
    if drink is False:
        wait()
        return

    favourite_drinks[person] = drink
    print(f"\nThank you - {person}'s favourite drink is now {drink}")
    wait()


def handle_add_person():
    name = get_raw_input("What is the name of the user?")
    if name not in people:
        people.append(name)
    wait()


def handle_add_drink():
    drink = get_raw_input("What is the name of the drink?")
    if drink not in drinks:
        drinks.append(drink)
    wait()


def handle_exit():
    print('Saving data...')
    save_to_file(DRINKS_FILE_PATH, drinks)
    save_to_file(PEOPLE_FILE_PATH, people)
    save_favourites(favourite_drinks)
    print(f'Thank you for using {APP_NAME}')


def run_round():
    # Whose round is it?
    # Print table names
    # Get input
    name = select_from_menu('Whose round is this?', people)
    if name is False:
        print("Please choose a number from the menu")
        run_round()

    # Create round with owner
    round = Round(name)
    should_add_to_order = True
    while should_add_to_order:
        name = None
        while not name:
            name = select_from_menu('Please choose a person', people)
            if name is False:
                print("Please choose a number from the menu")
                continue

        has_favourite = name in favourite_drinks.keys()
        favourite_option = 'Usual'
        available_drinks = drinks
        if has_favourite:
            available_drinks = drinks + [favourite_option]

        drink = None
        while not drink:
            drink = select_from_menu('Please choose a drink', available_drinks)
            if drink is False:
                print("Please choose a number from the menu")
                continue
        if drink == favourite_option:
            drink = favourite_drinks[name]
        round.add_to_round(favourite_drinks, name, drink=drink)
        # TODO: Ask to add another order with end round option
        should_add_to_order = False

        clear_screen()
        round.print_order()
        wait()


# Classes
class Round:
    def __init__(self, brewer, order={}):
        self.order = order
        self.brewer = brewer

    def add_to_round(self, preferences, name, drink=None):
        drink = drink if drink else preferences[name]
        self.order[name] = drink

    def print_order(self):
        print(self.brewer)
        for name, drink in self.order.items():
            output(f"Make {drink} for {name}")

# App
def run():
    while True:
        print_main_menu()
        option = get_menu_input('Enter your selection:')
        if option is False:
            print("Please choose a number from the menu")
            wait()
            continue

        # Handle command
        if option == GET_DRINKS_ARG:
            print_drinks()
            wait()
            continue
        elif option == GET_PEOPLE_ARG:
            print_people()
            wait()
            continue
        elif option == ADD_PERSON_ARG:
            handle_add_person()
            continue
        elif option == ADD_DRINK_ARG:
            handle_add_drink()
            continue
        elif option == SET_FAVOURITE_ARG:
            handle_set_favourite_drink()
            continue
        elif option == VIEW_FAVOURITES_ARG:
            print_favourites(favourite_drinks)
            wait()
            continue
        elif option == START_ROUND_ARG:
            print('starting a round')
            run_round()
        elif option == EXIT_ARG:
            handle_exit()
            exit()
        else:
            output(f'"{option}"" is not an option that I recognise')
            wait()
            continue


def start():
    load_data()
    run()


# Entry point
start()
