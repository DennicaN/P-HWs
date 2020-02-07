class Clothess:

    def __init__(self, size, height):
        self.size = size
        self.height = height

    def overcoat_area(self):
        return round(self.size / 6.5 + 0.5)

    def suit_area(self):
        return round(2 * self.height + 0.3)

    @property
    def full_area(self):
        return (f'Общая площадь ткани: \n'
                   f'{round(self.size / 6.5 + 0.5) + (2 * self.height + 0.3)}')


class Overcat(Clothess):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.overcoat = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани пальто: ~ {self.overcoat} м'


class Suit(Clothess):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.suit = round(2 * self.height + 0.3)

    def __str__(self):
        return f'Площадь ткани костюма: ~ {self.suit} м'


Overcat = Overcat(5, 15)
Suit = Suit (5, 7)
print(Suit.full_area)
print(Overcat)
print(Suit)