import sys

import pyodbc
from tabulate import tabulate
from sqlalchemy import *
from connection import db
from models import Address, Employee, address_table, employee_table

__employees_with_address_query = select(employee_table.c['pesel', 'first_name', 'last_name', 'birthday'],
                                        address_table.c['address_id', 'country', 'city', 'street', 'postal_code']).join(
    address_table, isouter=True)


def print_menu(options) -> None:
    print("Menu:")
    print(tabulate(options, headers=['Akcja', 'Opis'], tablefmt='rounded_grid'))


def find_all_employees() -> list[Employee]:
    employee_list: list[Employee] = []
    find_all_sql = __employees_with_address_query.order_by(employee_table.c.last_name)
    for row in db.execute(find_all_sql).fetchall():
        employee_list.append(Employee.from_sql(*row))

    return employee_list


def create_address() -> Address:
    country = input("Kraj: ")
    city = input("Miasto: ")
    street = input("Ulica: ")
    postal_code = input("Kod pocztowy: ")

    insert_address_query = insert(address_table).values(country=country, city=city, street=street,
                                                        postal_code=postal_code)
    result = db.execute(insert_address_query)
    return Address(result.inserted_primary_key[0], country, city, street, postal_code)


def add_employee():
    first_name = input("Podaj imię pracownika: ")
    last_name = input("Podaj nazwisko pracownika: ")
    pesel = input("Podaj PESEL: ")
    birthday = input("Podaj datę urodzenia [YYYY-MM-dd]: ")

    print(10 * '-', 'Tworzenie Adresu', 10 * '-')

    try:
        address = create_address()
        insert_employee_query = insert(employee_table).values(pesel=pesel, first_name=first_name, last_name=last_name,
                                                              birthday=birthday, address_id=address.address_id)
        db.execute(insert_employee_query)
        db.commit()
    except Exception as ex:
        print(ex)
        error_message = f'Pracownik z nr. PESEL {pesel} już istnieje w systemie'
        print(tabulate([[error_message]], headers=['ERROR'], tablefmt='rounded_grid'))
        db.rollback()


def delete_employee(employee: Employee):
    delete_employee_query = delete(employee_table).where(employee_table.c.pesel == employee.pesel)
    result = db.execute(delete_employee_query)

    if result.rowcount < 1:
        error_message = f'Pracownik z numerem PESEL {employee.pesel} nie istnieje.'
        print(tabulate([[error_message]], headers=['ERROR'], tablefmt='rounded_grid'))
    else:
        db.commit()
        print(f"Pracownik {employee.first_name} {employee.last_name} został usunięty poprawnie")


def edit_employee(e: Employee):
    print("Jeżeli nie ma zmiany danych ENTER")
    first_name = input("Podaj imię pracownika: ") or e.first_name
    last_name = input("Podaj nazwisko pracownika: ") or e.last_name
    birthday = input("Podaj datę urodzenia [YYYY-MM-dd]: ") or e.birthday

    update_employee_query = update(employee_table).values(first_name=first_name, last_name=last_name, birthday=birthday) \
        .where(employee_table.c.pesel == e.pesel)
    db.execute(update_employee_query)

    if e.address is not None:
        country = input("Kraj: ") or e.address.country
        city = input("Miasto: ") or e.address.city
        street = input("Ulica: ") or e.address.street
        postal_code = input("Kod pocztowy: ") or e.address.postal_code

        update_address_query = update(address_table).values(country=country, city=city, street=street,
                                                            postal_code=postal_code)
        db.execute(update_address_query)

    db.commit()


def search_employee():
    search_pesel = input("Proszę podać PESEL do wyszukiwania: ")

    search_employee_query = __employees_with_address_query.where(employee_table.c.pesel == search_pesel)
    found = db.execute(search_employee_query).fetchone()

    if not found:
        error_message = f"Pracownik o numerze PESEL {search_pesel} nie został znaleziony!"
        print(tabulate([error_message], headers=['ERROR'], tablefmt='rounded_grid'))
        return

    found_employee = Employee.from_sql(*found)
    print_employee_table([found_employee])

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
            choice_map[decision](found_employee)
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
    filter_employee_query = __employees_with_address_query \
        .where(employee_table.c.last_name.like(f'%{last_name_filter}%')) \
        .order_by(employee_table.c.last_name)
    filtered_by_last_name = [Employee.from_sql(*row) for row in
                             db.execute(filter_employee_query).fetchall()]

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
