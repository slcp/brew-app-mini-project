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
drinks = ['Tea', 'Coffee', 'Mocha', 'Cortado']
people = ['Malik', 'Katie', 'Taishan', 'Suman']
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
    return True


def select_from_menu(message, data):
    print_menu(message, data)
    index = get_menu_input('Enter your selection:')
    if not validate_menu_input(index, data):
        return False
    return data[index]


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
    for i, item in enumerate(data, start=1):
        items.append(f'[{i}] {item}')
    clear_screen()
    print(f'{title}\n')
    print('\n'.join(items), '\n')


def print_favourites(data):
    items = []
    for name, drink in data.items():
        items.append(f'{name}: {drink}')
    print_table('Favourites', items)


# Entry point
while True:
    print_main_menu()
    option = get_menu_input('Enter your selection:')
    # There is no 0 menu option so this works, not ideal
    if not option:
        wait()
        continue

    # Handle command
    if option == GET_DRINKS_ARG:
        print_drinks()
        wait()
    elif option == GET_PEOPLE_ARG:
        print_people()
        wait()
    elif option == EXIT_ARG:
        print(f'Thank you for using {APP_NAME}')
        exit()
    elif option == ADD_PERSON_ARG:
        name = get_raw_input("What is the name of the user?")
        if name not in people:
            people.append(name)
        wait()
    elif option == ADD_DRINK_ARG:
        drink = get_raw_input("What is the name of the drink?")
        if drink not in drinks:
            drinks.append(drink)
        wait()
    elif option == SET_FAVOURITE_ARG:
        person = select_from_menu('Choose a person', people)
        if not person:
            output(f'{person} is mo')
            wait()

        drink = select_from_menu(f'Choose a drink for {person}', drinks)
        if not drink:
            wait()

        favourite_drinks[person] = drink
        print(f"\nThank you - {person}'s favourite drink is now {drink}")
        wait()
    elif option == VIEW_FAVOURITES_ARG:
        print_favourites(favourite_drinks)
        wait()
    else:
        output(f'"{option}"" is not an option that I recognise')
        wait()
