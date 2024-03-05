class Animal:
    def introduce(self):
        print(f"Jestem {self.type}, mam na imię {self.name}, jest nas {self.counter}!")


class Dog(Animal):
    type = "pies"
    counter = 0

    def __init__(self, name):
        self.name = name
        Dog.counter += 1

class Cat(Animal):
    type = "kot"
    counter = 0

    def __init__(self, name):
        self.name = name
        Cat.counter += 1

animals = [
    Dog("Pluto"),
    Cat("Filemon"),
    Dog("Azor"),
    Dog("As"),
    Cat("Sylwester")
]

for a in animals:
    a.introduce()