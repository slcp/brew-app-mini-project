from src.core.main import clear_screen

def print_menu(title: str, data: list):
    items = []
    # enumerate() will produce the index/position in the list and the item in
    # the list for use within your loop. If you are not interested in knowing
    # what position you are at in the list then you wouldn't want to use
    # enumerate()
    #
    # https://www.programiz.com/python-programming/methods/built-in/enumerate
    # https://docs.python.org/3/library/functions.html#enumerate
    for i, item in enumerate(data):
        items.append(f'[{i}] {item}')
    clear_screen()
    print(f'{title}\n')
    print('\n'.join(items), '\n')


def get_numeric_menu_input(message: str):
    try:
        return int(input(f'{message} '))
    except ValueError:
        print("\nMenu items - numbers are the only input I understand")
        return False


def validate_numeric_menu_input(index: int, data: list):
    if index < 0 or index >= len(data):
        print(f'"{index}" is not a valid option from that menu\n')
        return False
    return data[index]


def select_from_menu(message: str, data: list):
    print_menu(message, data)
    selection = get_numeric_menu_input(f'{message} ')
    return validate_numeric_menu_input(selection, data)
