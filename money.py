"""Represents Money."""
import decimal
import math

TWO_PLACES = decimal.Decimal("0.01")

class Money:
    def __init__(self):
        self.amount = decimal.Decimal(0)

    def __init__(self, amount):
        if isinstance(amount, Money):
            self.amount = amount.amount
        else:
            self.amount = decimal.Decimal(amount)

    def __str__(self):
        return str(self.format())

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __mul__(self, other):
        return Money(self.amount * other.amount)
    
    def __truediv__(self, other):
        return Money(self.amount / other.amount)

    def __floordiv__(self, other):
        return Money(math.floor(self.amount / other.amount))

    def format(self):
        return self.amount.quantize(TWO_PLACES)
