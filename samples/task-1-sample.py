from sys import argv
args = argv

# Define data
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
if args[1] == GET_DRINKS_ARG:
    for drink in drinks:
        print(drink)
elif args[1] == GET_PEOPLE_ARG:
    for person in people:
        print(person)
