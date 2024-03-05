import random

class Dice:
    def __init__(self):
        self.__value = None

    def get_value(self): #dodajemy to i podkreślniki w value i pair
        return self.__value

    def throw(self):
        self.__value = random.randint(1,6)

    def __str__(self):
        # return "[{}]".format(self.value)
        return f"[{self.__value}]"

# dice = Dice()
# dice.throw()
# print(dice)

class DicePair():

    def __init__(self):
        self.__pair = [Dice(), Dice()]

    def throw(self):
        self.__pair[0].throw()
        self.__pair[1].throw()

    def is_double(self):
        return self.__pair[0].get_value() == self.__pair[1].get_value()

    def __str__(self):
        return f"{self.__pair[0]} {self.__pair[1]}"

dices = DicePair()
# dices.throw()
# print(dices)
# print(dices.is_double())

while True:
    dices.throw()
    print(dices)
    if dices.is_double():
        break