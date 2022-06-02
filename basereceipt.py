from item import *

class BaseReceipt:
    def __init__(self):
        self.people = {}
        self.items = []

    def get_item_subtotal(self):
        subtotal = Money(0)

        for item in self.items:
            subtotal += item.price

        return subtotal

    def get_people_total(self):
        subtotal = Money(0.0)

        for _, value in self.people.items():
            subtotal += value

        return subtotal

    def __str__(self):
        reprs = ""
        for key, value in self.people.items():
            reprs += str(f'{key} owes {value}\n')

        return reprs

    # "Interface" methods
    def add_people(self):
        raise NotImplementedError

    def add_item(self):
        raise NotImplementedError

    def find_splitters(self):
        raise NotImplementedError

    def set_shared_costs(self):
        raise NotImplementedError