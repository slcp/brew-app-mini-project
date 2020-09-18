from src.core.table import print_table

class Round:
    def __init__(self, brewer, order={}):
        self.order = order
        self.brewer = brewer

    def add_to_round(self, preferences, name, drink=None):
        drink = drink if drink else preferences[name]
        self.order[name] = drink

    def print_order(self):
        content = [f'{name} ordered {drink}' for name,
                   drink in self.order.items()]
        print_table(f"{self.brewer}'s round", content)
