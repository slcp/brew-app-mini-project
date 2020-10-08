import csv
import pymysql
import uuid

data = []

# Load the file
# Extract the data
FILE_PATH = './etl.csv'
with open(FILE_PATH) as file:
    rows = []
    reader = csv.reader(file)
    for row in reader:
        rows.append(row)
    # Lose the headers row from the CSV (column names)
    data = rows[1:]

# Transform the data - get first/last name
# My data in second column represents a person's name and looks like "[first  name] [last name]"
transformed = []
NAME_INDEX = 1
for person in data:
    first_name, last_name = person[NAME_INDEX].split(" ")
    first_name, last_name = (first_name.title(), last_name.title())
    transformed.append([first_name, last_name])

# My db table has an id column - make an id
for index, person in enumerate(transformed):
    transformed[index].append(uuid.uuid1())

# Load the data into the db
connection = pymysql.connect(host="db",
                        user="root",
                        password="password",
                        db="brew_app",
                        port=3306)

try:
    with connection.cursor() as cursor:
        # uuid (id) value is a uuid object - we need it be a string
        raw = [[f, l, str(id)] for f, l, id in transformed]
        cursor.executemany('INSERT INTO etl (first_name, last_name, id) VALUES (%s, %s, %s)', raw)
        connection.commit()
finally:
    connection.close()