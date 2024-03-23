class Employee:
    def __init__(self, firstname, lastname, age, salary):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def get_fullname(self):
        return self.__firstname + " " + self.__lastname

    def get_age(self):
        return self.__age


employees = []
employees.append(Employee("Jan", "Kowalski", 25, 3500))
employees.append(Employee("Edmund", "Krawczyk", 45, 7000))
employees.append(Employee("Tomasz", "Nowak", 60, 15200))

print("Lista płac")
print("-" * 30)

for e in employees:
    print(e.get_fullname(), "wiek:", e.get_age(), "lat, pensja:", e.get_salary(), "zł.")