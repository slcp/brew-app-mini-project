import csv

class File_Store:
    def __init__(
            self,
            path,
            # Optionally, a function can be passed into the constructor to act on each
            # line being read from the file before it is returned in the list to the caller.
            # See read_lines for where self.load_item is called - each line loaded from the file is
            # passed to the load_processor function defined here
            #
            # This could be used to do build a Person Class for example
            load_processor=lambda line: line,
            # Optionally, a function can be passed into the constructor to act on each item before
            # being saved to the file.
            # See save_lines for where self.save_item is called - each item from is passed to the 
            # save_processor function defined here.
            #
            # This could be used to do extract data from a Person Class for example
            save_processor=lambda item: item):
        self.path = path
        self.load_item = load_processor
        self.save_item = save_processor

    def read_lines(self):
        data = []
        try:
            with open(self.path, 'r') as file:
                for line in file.readlines():
                    # Check if empty - bail/stop/valdiate as early as possible
                    if not line:
                        continue
                    # Trim newline/whitespace
                    # Add to data
                    data.append(self.load_item(line.strip()))
        except FileNotFoundError as e:
            print(
                f'File "{self.path}" cannot be found with error: {str(e)} - exiting')
        return data

    def save_lines(self, data):
        try:
            with open(self.path, 'w') as file:
                # List comprehension - make a new list from an list
                # https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
                # There are other ways to this but list comprehension
                # is an idiomatic use of python
                file.writelines([f'{self.save_item(item)}\n' for item in data])
        except FileNotFoundError as e:
            print(
                f'File "{self.path}" cannot be found with error: {str(e)} - exiting')

    # data is expected to be a list of lists
    def save_to_csv(self, data):
        try:
            with open(self.path, 'w') as file:
                writer = csv.writer(file)
                writer.writerows(data)
        except FileNotFoundError as e:
            print(
                f'File "{self.path}" cannot be found with error: {str(e)} - exiting')

    # Returns list of lists
    def read_csv(self):
        try:
            with open(self.path, 'r') as file:
                data = []
                reader = csv.reader(file, delimiter=',')
                for row in reader:
                    data.append(row)
                return data
        except FileNotFoundError as e:
            print(
                f'File "{self.path}" cannot be found with error: {str(e)} - exiting')
