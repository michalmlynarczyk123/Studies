import datetime
import sys

import pyodbc
from tabulate import tabulate
from sqlalchemy import *
from connection import db
from models import Address, Employee


def print_menu(options) -> None:
    print("Menu:")
    print(tabulate(options, headers=['Akcja', 'Opis'], tablefmt='rounded_grid'))


def find_all_employees() -> list[Employee]:
    return db.execute(select(Employee)).scalars().all()


def create_address() -> Address:
    country = input("Kraj: ")
    city = input("Miasto: ")
    street = input("Ulica: ")
    postal_code = input("Kod pocztowy: ")
    return Address(country=country, city=city, street=street, postal_code=postal_code)


def add_employee():
    first_name = input("Podaj imię pracownika: ")
    last_name = input("Podaj nazwisko pracownika: ")
    pesel = input("Podaj PESEL: ")
    birthday = input("Podaj datę urodzenia [YYYY-MM-dd]: ")

    print(10 * '-', 'Tworzenie Adresu', 10 * '-')

    try:
        address = create_address()
        employee = Employee(pesel=pesel, first_name=first_name, last_name=last_name,
                            birthday=datetime.datetime.strptime(birthday, '%Y-%m-%d'), address=address)

        db.add(employee)
        db.commit()
    except Exception as ex:
        print(ex)
        error_message = f'Pracownik z nr. PESEL {pesel} już istnieje w systemie'
        print(tabulate([[error_message]], headers=['ERROR'], tablefmt='rounded_grid'))
        db.rollback()


def delete_employee(employee: Employee):
    if employee is None:
        error_message = f'Pracownik nie istnieje.'
        print(tabulate([[error_message]], headers=['ERROR'], tablefmt='rounded_grid'))
    else:
        db.delete(employee)
        db.commit()
        print(f"Pracownik {employee.first_name} {employee.last_name} został usunięty poprawnie")


def edit_employee(e: Employee):
    print("Jeżeli nie ma zmiany danych ENTER")
    first_name = input("Podaj imię pracownika: ") or e.first_name
    last_name = input("Podaj nazwisko pracownika: ") or e.last_name
    birthday = input("Podaj datę urodzenia [YYYY-MM-dd]: ") or e.birthday

    e.last_name = last_name
    e.first_name = first_name
    e.birthday = birthday

    address = e.address

    if address is not None:
        country = input("Kraj: ") or address.country
        city = input("Miasto: ") or address.city
        street = input("Ulica: ") or address.street
        postal_code = input("Kod pocztowy: ") or address.postal_code
        address.country = country
        address.city = city
        address.street = street
        address.postal_code = postal_code

    db.commit()


def search_employee():
    search_pesel = input("Proszę podać PESEL do wyszukiwania: ")
    found: Employee = db.get(Employee, search_pesel)

    if not found:
        error_message = f"Pracownik o numerze PESEL {search_pesel} nie został znaleziony!"
        print(tabulate([error_message], headers=['ERROR'], tablefmt='rounded_grid'))
        return

    print_employee_table([found])

    choice_map = {
        "1": delete_employee,
        "2": edit_employee
    }
    menu_options = [
        ["1", "Usuń Pracownika"],
        ["2", "Edytuj Pracownika"],
        ["0", "Powrót"]
    ]

    while True:
        print_menu(menu_options)
        decision = input('>\t')

        if decision == '0':
            break
        elif decision not in choice_map:
            print("Proszę wybrać poprawną akcję")
        else:
            choice_map[decision](found)
            break


def print_employee_table(employee_list: list[Employee]) -> None:
    table_data = [
        (emp.first_name, emp.last_name, emp.pesel, emp.birthday,
         f"{emp.address.country} {emp.address.city}, {emp.address.street} {emp.address.postal_code}"
         if emp.address is not None else 'Brak adresu')
        for emp in
        employee_list
    ]
    print(
        tabulate(table_data, headers=['Imię', 'Nazwisko', 'PESEl', 'Data urodzenia', 'Adres'], tablefmt='rounded_grid'))


def list_all_employees():
    all_employees = find_all_employees()
    print_employee_table(all_employees)


def filter_employees():
    last_name_filter = input("Proszę podać część nazwiska: ")
    filter_employee_query = select(Employee).filter(Employee.last_name.like(f'%{last_name_filter}%'))
    filtered_by_last_name = db.execute(filter_employee_query).scalars().all()
    # [Employee(), Employee(), Employee()]
    print_employee_table(filtered_by_last_name)


def exit():
    sys.exit()


if __name__ == '__main__':
    menu_options = [
        ["1", "Dodaj Pracownika"],
        ["2", "Wyszukaj Pracownika"],
        ["3", "Wyświetl Wszystkich Pracowników"],
        ["4", "Filtruj Pracowników"],
        ["0", "Exit"]
    ]
    choice_map = {
        "1": add_employee,
        "2": search_employee,
        "3": list_all_employees,
        "4": filter_employees,
        "0": exit
    }

    while True:
        print_menu(menu_options)
        decision = input(">\t")

        if decision not in choice_map:
            print("Proszę wybrać poprawną akcję!")
        else:
            choice_map[decision]()
