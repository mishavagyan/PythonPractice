"""
Description
Implement class Currency and inherited classes Euro, Dollar, Pound.
Course is 1 EUR == 2 USD == 100 GBP
You need to implement the following methods:

course - classmethod which returns string in the following pattern: {float value} {currency to} for 1 {currency for}

to_currency - method transforms currency from one currency to another. Method should return
instance of a required currency.

+ - returns an instance of a new value

other comparison methods: > < ==

"""

from __future__ import annotations
from typing import Type


class Currency:
    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """

    conversion_rates = {
        "EUR": {"USD": 2.0, "GBP": 100.0},
        "USD": {"EUR": 0.5, "GBP": 50.0},
        "GBP": {"USD": 0.02, "EUR": 0.01},
    }

    name = "Currency"

    def __init__(self, value: float):
        self.value = value

    def __str__(self):
        return f"{float(self.value)} {self.name}"

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        try:
            if cls == other_cls:
                return f"1.0 {cls.name} for 1 {cls.name}"
            return f"{cls.conversion_rates[cls.name][other_cls.name]} {other_cls.name} for 1 {cls.name}"
        except KeyError:
            return "Invalid value"

    def to_currency(self, other_cls: Type[Currency]):
        try:
            if isinstance(self, other_cls):
                return self
            res = self.conversion_rates[self.name][other_cls.name] * self.value
            return other_cls(res)
        except KeyError:
            raise ValueError(f"Cannot convert {self.name} to {other_cls.name}")

    def __add__(self, other):
        try:
            if isinstance(other, self.__class__):
                return self.__class__(other.value + self.value)
            others_value = other.to_currency(self.__class__)
            return self.__class__(self.value + others_value.value)
        except Exception as ex:
            raise ValueError(f"Addition failed between {self.name} and {other.name}: {ex}")

    def __eq__(self, other):
        try:
            if isinstance(other, self.__class__):
                return self.value == other.value
            others_value = other.to_currency(self.__class__)
            return self.value == others_value.value
        except Exception as ex:
            raise ValueError(f"Comparison failed between {self.name} and {other.name}: {ex}")

    def __lt__(self, other):
        try:
            if isinstance(other, self.__class__):
                return self.value < other.value
            others_value = other.to_currency(self.__class__)
            return self.value < others_value.value
        except Exception as ex:
            raise ValueError(f"Comparison failed between {self.name} and {other.name}: {ex}")

    def __gt__(self, other):
        return not (self.__lt__(other) or self.__eq__(other))

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)


class Euro(Currency):
    name = "EUR"


class Dollar(Currency):
    name = "USD"

class Pound(Currency):
    name = "GBP"


if __name__ == "__main__":
    print(
        f"Euro.course(Pound)   ==> {Euro.course(Pound)}\n"
        f"Euro.course(Euro)   ==> {Euro.course(Euro)}\n"
        f"Dollar.course(Pound) ==> {Dollar.course(Pound)}\n"
        f"Pound.course(Euro)   ==> {Pound.course(Euro)}\n"
    )

    e = Euro(100.123)
    ee = Euro(100)
    r = Pound(100)
    d = Dollar(200)
    print(
        f"e = {e}\n"
        f"e.to_currency(Dollar) = {e.to_currency(Dollar)}\n"
        f"e.to_currency(Pound) = {e.to_currency(Pound)}\n"
        f"e.to_currency(Euro)   = {e.to_currency(Euro)}\n"
    )

    print(
        f"r = {r}\n"
        f"r.to_currency(Dollar) = {r.to_currency(Dollar)}\n"
        f"r.to_currency(Euro)   = {r.to_currency(Euro)}\n"
        f"r.to_currency(Pound) = {r.to_currency(Pound)}\n"
    )
    print(
        f"e + r  =>  {e + r}\n"
        f"r + d  =>  {r + d}\n"
        f"d + e  =>  {d + e}\n"
        f"ee == e  =>  {ee >= e}\n"
    )
