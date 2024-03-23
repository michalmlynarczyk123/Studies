class Person:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"Imię: {self.__name}"

class Employee(Person):

    def __init__(self, name, salary):
        super().__init__(name)
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def __str__(self):
        return super().__str__() + f", zarobki: {self.__salary}"


class Manager(Employee):

    def __init__(self, name, salary, project):
        super().__init__(name, salary)
        self.__project = project

    def get_project(self):
        return self.__project

    def __str__(self):
        return super().__str__() + f", projekt: {self.__project}"


persons = [
    Person("Tomek"),
    Employee("Dorota", 6000),
    Manager("Edward", 9000, "Aplikacja mobilna"),
    Person("Alicja")
    ]

manager_counter = 0
for p in persons:
    if isinstance(p, Manager):
        manager_counter += 1
    print(p)
print("Liczba managerów:", manager_counter)
