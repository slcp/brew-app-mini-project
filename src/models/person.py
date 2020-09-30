class Person:
    def __init__(self, id, first_name, last_name, drink=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.drink = drink
        self.age = 18

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'