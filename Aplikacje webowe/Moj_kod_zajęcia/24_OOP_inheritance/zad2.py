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
        return "hau hau"


class Cat(Animal):
    type = "kot"
    counter = 0

    def __init__(self, name):
        super().__init__()
        self.name = name
        Cat.counter += 1

    def make_sound(self):
        return "miau"

class Bird(Animal):
    type = "ptak"
    counter = 0

    def __init__(self, name):
        super().__init__()
        self.name = name
        Bird.counter += 1

    def make_sound(self):
        return "ćwir"

class Snake(Animal):
    type = "wąż"
    counter = 0

    def __init__(self, name):
        super().__init__()
        self.name = name
        Snake.counter += 1

    def make_sound(self):
        return "sss"

animals = [
    Dog("Pluto"),
    Cat("Filemon"),
    Dog("Azor"),
    Dog("As"),
    Cat("Sylwester"),
    Bird("Kuba"),
    Bird("Tomek"),
    Bird("Garfield"),
    Snake("Baltazar"),
    Snake("Kleks")
]

for a in animals:
    a.introduce()