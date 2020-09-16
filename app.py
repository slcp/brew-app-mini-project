import os

# Define data
# Menu options
GET_PEOPLE_ARG = 1
GET_DRINKS_ARG = 2
ADD_PERSON_ARG = 3
ADD_DRINK_ARG = 4
SET_FAVOURITE_ARG = 5
VIEW_FAVOURITES_ARG = 6
EXIT_ARG = 7

# CLI menu
APP_NAME = 'BrIW'
VERSION = '0.1'
MENU_TEXT = f'''
Welcome to {APP_NAME} v{VERSION}!
Please, select an option by entering a number:

[1] Get all people
[2] Get all drinks
[3] Add a person
[4] Add a drink
[5] Set a favourite drink
[6] View favourites
[7] Exit
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


# App
def run_menu():
    print_main_menu()
    option = get_menu_input('Enter your selection:')
    if not option:
        wait()
        run_menu()

    # Handle command
    if option == GET_DRINKS_ARG:
        print_drinks()
        wait()
        run_menu()
    elif option == GET_PEOPLE_ARG:
        print_people()
        wait()
        run_menu()
    elif option == EXIT_ARG:
        print('Saving data...')
        save_to_file(DRINKS_FILE_PATH, drinks)
        save_to_file(PEOPLE_FILE_PATH, people)
        save_favourites(favourite_drinks)
        print(f'Thank you for using {APP_NAME}')
        exit()
    elif option == ADD_PERSON_ARG:
        name = get_raw_input("What is the name of the user?")
        if name not in people:
            people.append(name)
        wait()
        run_menu()
    elif option == ADD_DRINK_ARG:
        drink = get_raw_input("What is the name of the drink?")
        if drink not in drinks:
            drinks.append(drink)
        wait()
        run_menu()
    elif option == SET_FAVOURITE_ARG:
        person = select_from_menu('Choose a person', people)
        if not person:
            wait()
            run_menu()

        drink = select_from_menu(f'Choose a drink for {person}', drinks)
        if not drink:
            wait()
            run_menu()

        favourite_drinks[person] = drink
        print(f"\nThank you - {person}'s favourite drink is now {drink}")
        wait()
        run_menu()
    elif option == VIEW_FAVOURITES_ARG:
        print_favourites(favourite_drinks)
        wait()
        run_menu()
    else:
        output(f'"{option}"" is not an option that I recognise')
        wait()
        run_menu()


def start():
    load_data()
    run_menu()


# Entry point
start()
