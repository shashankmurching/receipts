from item import *

class Receipt:
    def __init__(self):
        self.people = {}
        self.items = []
        self.add_people()
        self.add_items()

    def __str__(self):
        reprs = ""
        for key, value in self.people.items():
            reprs += str(f'{key} owes {value}\n')

        return reprs

    @staticmethod
    def get_input(prompt):
        return input(prompt).split(",")

    def add_people(self):
        names = Receipt.get_input("Enter people's names separated by commas: ")

        for name in names:
            self.people[name] = Money(0)

    def add_items(self):
        while True:
            item_content = input("Enter item name and price separated by a comma.\nOr 'q' to stop: ")

            if item_content == "" or item_content == "q":
                break

            item_content = item_content.split(",")
            item = Item(item_content[0], item_content[1])
            self.items.append(item)

    def find_splitters(self):
        for item in self.items:
            names = Receipt.get_input(f'Enter the names of the people who split {item}: ')
            split_price = item.get_split_price(len(names))

            for name in names:
                if name not in self.people:
                    raise f'{name} was not found in previous list'
                
                self.people[name] += split_price

    def set_shared_costs(self):
        costs = Receipt.get_input("Enter the tax and tip separated by a comma: ")
        shared_cost = Money(costs[0]) + Money(costs[1])
        item_total = self.get_item_subtotal()

        print(f'Item total + shared cost is: {item_total + shared_cost}')

        for key, value in self.people.items():
            self.people[key] += shared_cost * Money(value / item_total)

        print(f'People total is: {self.get_people_total()}')

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

