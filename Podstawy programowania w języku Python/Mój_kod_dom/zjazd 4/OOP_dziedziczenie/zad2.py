class Animal:
    all_counter = 0

    def __init__(self):
        Animal.all_counter += 1

    def introduce(self):
        print(f"Jestem {self.type}, mam na imię {self.name}, jest nas {self.counter}, a wszystkich zwierząt {self.all_counter}, {self.make_sound()}!")

class Dog(Animal):
    type = "pies"
    counter = 0

    def __init__(self, name):
        super().__init__()
        self.name = name
        Dog.counter += 1

    def make_sound(self):
        return "Hau hau"


class Cat(Animal):
    type = "kot"
    counter = 0

    def __init__(self, name):
        super().__init__()
        self.name = name
        Cat.counter += 1

    def make_sound(self):
        return "miau miaau"

class Pig(Animal):
    type = "świnka"
    counter = 0

    def __init__(self, name):
        super().__init__()
        self.name = name
        Pig.counter += 1

    def make_sound(self):
        return "chrum chrum"

class Horse(Animal):
    type = "koń"
    counter = 0

    def __init__(self, name):
        super().__init__()
        self.name = name
        Horse.counter += 1

    def make_sound(self):
        return "ihaaa"

animals = [
    Dog("Pluto"),
    Cat("Filemon"),
    Dog("Azor"),
    Dog("As"),
    Cat("Sylwester"),
    Pig("Piggy"),
    Horse("Karino"),
    Pig("Pepe")
]

for a in animals:
    a.introduce()