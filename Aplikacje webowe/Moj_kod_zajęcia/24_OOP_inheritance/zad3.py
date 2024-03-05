class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"imię: {self.__name}"

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def __str__(self):
        return super().__str__() + f", zarobki: {self.__salary}"

class Menager(Employee):
    def __int__(self, name, salary, project):
        super().__init__(name, salary)
        self.__project = project

    def get_project(self):
        return self.__project

    def __str__(self):
        return super().__str__() + f", projekt: {self.__project}"

persons = [Person("Tomek"),
           Employee("Dorota", 6000),
           Menager("Edward", 9000, "aplikacja mobilna"),
           Person("Alicja")
           ]

menager_cnt = 0
for p in persons:
    if isinstance(p, Menager):
        menager_cnt += 1
    print(p)
print("Liczba menadżerów:".format(menager_cnt))