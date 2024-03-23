class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def intorduce(self):
        print("Cześć, jestem", self.__name, "i mam", self.__age, "lat/a.")


persons = []
persons.append(Person("Janek", 20))
persons.append(Person("Agata", 25))
persons.append(Person("Michał", 41))
persons.append(Person("Tomek", 14))
persons.append(Person("Maciej", 18))
persons.append(Person("Monika", 67))

for p in persons:
    p.intorduce()
