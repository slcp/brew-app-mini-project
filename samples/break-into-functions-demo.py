import csv
PEOPLE_FILE_PATH = '../data/people.csv'
people = []

DRINKS_FILE_PATH = '../data/drinks.csv'
drinks = []

### Writes to people and drink list
# Getting user input
def add_people_drinks():
    # with open(PEOPLE_FILE_PATH, 'w', newline="") as people_files, open(DRINKS_FILE_PATH, 'w', newline="") as drink_files:
    #     people_writer = csv.writer(people_files, quoting=csv.QUOTE_ALL)
    #     drink_writer = csv.writer(drink_files, quoting=csv.QUOTE_ALL)
    b = int(input("Number of people: "))
    for _ in range(b):
        # This for loop looks at the amount entered in Number of people and repeats the process below that many times.
        name = input("Please enter the name of the person: ")
        # people_writer.writerow([name])
        drink = input("Please enter drink name: ")
        # drink_writer.writerow([drink])
        # do_the_file_stuff(PEOPLE_FILE_PATH, DRINKS_FILE_PATH, name, drink)
        add_drink_person_to_csv_file(PEOPLE_FILE_PATH, [name])
        add_drink_person_to_csv_file(DRINKS_FILE_PATH, [drink])
        print("Name and drink has been added.")


def add_drink_person_to_csv_file(path, data):
    with open(path, 'w', newline="") as file:
        # people_writer = csv.writer(people_files, quoting=csv.QUOTE_ALL)
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        # people_writer.writerow([name])
        writer.writerow(data)

# # Using files - writing to files
# def do_the_file_stuff(people_file_path, drink_file_path, name, drink):
#     # Opening two files and adding data to them
#     # with open(people_file_path, 'w', newline="") as people_files, open(drink_file_path, 'w', newline="") as drink_files:
#     #     people_writer = csv.writer(people_files, quoting=csv.QUOTE_ALL)
#     #     drink_writer = csv.writer(drink_files, quoting=csv.QUOTE_ALL)
#     #     people_writer.writerow([name])
#     #     drink_writer.writerow([drink])
#     add_drink_person_to_csv_file(people_file_path, [name])
#     add_drink_person_to_csv_file(drink_file_path, [drink])