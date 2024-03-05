class Person:

    def __init__(self, name, age):
        self.__name  = name
        self.__age = age

    def introduce(self):
        print("Cześć, jestem", self.__name, "i mam", self.__age, "lat/a.")

persons = []
persons.append((Person("Janek", 20)))
persons.append((Person("Agata", 34)))
persons.append((Person("Tomek", 55)))
persons.append((Person("Monika", 14)))
persons.append((Person("Michał", 20)))
persons.append((Person("Zbyszek", 7)))

for p in persons:
    p.introduce()