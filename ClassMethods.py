# Class Method, Static Method Demo

import math


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza('
                f'{self.ingredients!r})')

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


if __name__ == '__main__':
    my_pizza = Pizza(['cheese', 'tomato sauce'])
    print(my_pizza)
    print(my_pizza.margherita())
    print("Area Of Circle With 2 Radius: %5.2f" % Pizza.circle_area(2))
    