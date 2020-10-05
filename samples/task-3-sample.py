import os

# Define data
# Menu options
GET_PEOPLE_ARG = 1
GET_DRINKS_ARG = 2

# CLI menu
APP_NAME = 'BrIW'
VERSION = '0.1'
MENU_TEXT = f'''
Welcome to {APP_NAME} v{VERSION}!
Please, select an option by entering a number:

[1] Get all people
[2] Get all drinks
[3] Exit
'''


def print_table(title, contents):
    width = get_table_width(contents)
    print_table_header(title, width)
    print_table_body(contents)
    print_table_footer(width)


def clear_screen():
    os.system('clear')


def show_menu():
    clear_screen()
    print(MENU_TEXT)


def get_selection():
    return int(input('Enter your selection: '))


def wait():
    input('\nPress any key to return to the main menu')


def output(text):
    print(f'\n{text}')


drinks = ['Tea', 'Coffee', 'Mocha', 'Cortado']
people = ['Malik', 'Katie', 'Taishan', 'Suman']

while True:
    show_menu()
    try:
        option = get_selection()
        # Handle command
        if option == GET_DRINKS_ARG:
            print_table('drinks', drinks)
            wait()
        elif option == GET_PEOPLE_ARG:
            print_table('people', people)
            wait()
        else:
            output(f'"{option}"" is not an option that I recognise')
            wait()
    except ValueError:
        output("Menu items numbers are the only input I understand")
        wait()


# Table output helper funcs
def get_table_width(items):
    longest = 0
    for item in items:
        if len(item) > longest:
            longest = len(item)
    # Add some spacing to the end of the table
    return longest + 2


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
