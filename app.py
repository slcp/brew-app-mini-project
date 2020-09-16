from sys import argv as args


def get_table_width(items):
    longest = 0
    for item in items:
        if len(item) > longest:
            longest = len(item)
    return longest + 2


def print_table(title, contents):
    width = get_table_width(contents)
    print_table_header(title, width)
    print_table_body(contents)
    print_table_footer(width)


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


GET_PEOPLE_ARG = 'get-people'
GET_DRINKS_ARG = 'get-drinks'

drinks = ['Tea', 'Coffee', 'Mocha', 'Cortado']
people = ['Malik', 'Katie', 'Taishan', 'Suman']

# Check args
if len(args) < 2:
    print("I'm not sure what you are expecting me to do, \
         you gave me no instructions")
    exit()
if len(args) > 2:
    print("I can only do one thing at a time which is it?!")
    exit()
if args[1] not in [GET_DRINKS_ARG, GET_PEOPLE_ARG]:
    print(f'"{args[1]}"" is not a command that I rcognise')
    exit()

# Handle command
command = args[1]
if command == GET_DRINKS_ARG:
    print_table('drinks', drinks)
elif command == GET_PEOPLE_ARG:
    print_table('people', people)
