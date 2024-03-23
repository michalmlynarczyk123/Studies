# program symulujący rzut dwoma kostkami do gry - podejscie obiektowe
# rzucamy dwiema kostkami do momentu aż nie wyrzucimy dubletu

import random

class Dice:

    def __init__(self):
        self.value = None

    def throw(self):
        self.value = random.randint(1, 6)

    def __str__(self):
        # return "[{}]".format(self.value)
        return f"[{self.value}]"

# dice = Dice()
# dice.throw()
# print(dice)

class DicePair:

    def __init__(self):
        self.pair = [Dice(), Dice()]

    def throw(self):
        self.pair[0].throw()
        self.pair[1].throw()

    def is_double(self):
        return self.pair[0].value == self.pair[1].value

    def __str__(self):
        return f"{self.pair[0]} {self.pair[1]}"

dices = DicePair()
# dices.throw()
# print(dices)
# print(dices.is_double())

while True:
    dices.throw()
    print(dices)
    if dices.is_double():
        break