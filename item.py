"""Represents Purchased Item."""

from money import *

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = Money(price)
        self.splitters = []

    def __str__(self):
        return str(f'{self.name} : ${self.price}')

    def get_split_price(self, splitter_count):
        if splitter_count == 0:
            raise f'Number of splitters must be at least 1 for {self.get_desc()}'

        return Money(self.price / Money(splitter_count))
