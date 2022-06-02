from item import *
from basereceipt import BaseReceipt

class Receipt(BaseReceipt):
    def __init__(self):
        super().__init__()

        self.add_people()
        self.add_items()

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
            while True:
                names = Receipt.get_input(f'Enter the names of the people who split {item}: ')
                split_price = item.get_split_price(len(names))

                # Todo - Optimize validation
                incorrect_name = False

                for name in names:
                    if name not in self.people:
                        print(f'{name} was not found in previous list. Retrying...')
                        incorrect_name = True
                        break

                if incorrect_name:
                    continue

                for name in names:
                    self.people[name] += split_price

                break

    def set_shared_costs(self):
        costs = Receipt.get_input("Enter the tax and tip separated by a comma: ")
        shared_cost = Money(costs[0]) + Money(costs[1])
        item_total = super().get_item_subtotal()

        print(f'Item total + shared cost is: {item_total + shared_cost}')

        for key, value in self.people.items():
            self.people[key] += shared_cost * Money(value / item_total)

        print(f'People total is: {super().get_people_total()}')
