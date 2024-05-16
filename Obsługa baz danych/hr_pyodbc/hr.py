import sys

import pyodbc
from tabulate import tabulate

from connection import connection
from models import Address, Employee


def print_menu(options) -> None:
    print("Menu:")
    print(tabulate(options, headers=['Akcja', 'Opis'], tablefmt='rounded_grid'))


def find_all_employees() -> list[Employee]:
    employee_list: list[Employee] = []
    find_all_sql = """
         SELECT  pesel,
         first_name,
         last_name,
         birthday,
         a.address_id, 
         country,
         city,
         street,
         postal_code
         FROM employees e 
         JOIN addresses a on e.address_id = a.address_id 
         ORDER BY e.last_name 
    """
    for row in connection.execute(find_all_sql):
        employee_list.append(Employee.from_sql(*row))

    return employee_list


def create_address(cursor: pyodbc.Cursor = connection.cursor()) -> Address:
    country = input("Kraj: ")
    city = input("Miasto: ")
    street = input("Ulica: ")
    postal_code = input("Kod pocztowy: ")

    cursor.execute("INSERT INTO addresses (country,city, street, postal_code) VALUES (?,?,?,?)",
                       (country, city, street, postal_code))
    cursor.execute("SELECT @@IDENTITY AS ID;")

    return Address(cursor.fetchone()[0], country, city, street, postal_code)


def add_employee():
    first_name = input("Podaj imię pracownika: ")
    last_name = input("Podaj nazwisko pracownika: ")
    pesel = input("Podaj PESEL: ")
    birthday = input("Podaj datę urodzenia [YYYY-MM-dd]: ")

    print(10 * '-', 'Tworzenie Adresu', 10 * '-')

    cursor = connection.cursor()

    try:
        address = create_address(cursor)
        cursor.execute(
            "INSERT INTO employees (pesel, first_name, last_name, birthday, address_id) VALUES (?,?,?,?,?)",
            (pesel, first_name, last_name, birthday, address.address_id))
        cursor.commit()
    except Exception as ex:
        print(ex)
        error_message = f'Pracownik z nr. PESEL {pesel} już istnieje w systemie'
        print(tabulate([[error_message]], headers=['ERROR'], tablefmt='rounded_grid'))
        cursor.rollback()
    finally:
        cursor.close()


def delete_employee(employee: Employee):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM employees WHERE pesel = ?", (employee.pesel,))

        if cursor.rowcount < 1:
            error_message = f'Pracownik z numerem PESEL {employee.pesel} nie istnieje.'
            print(tabulate([[error_message]], headers=['ERROR'], tablefmt='rounded_grid'))
        else:
            cursor.commit()
            print(f"Pracownik {employee.first_name} {employee.last_name} został usunięty poprawnie")


def edit_employee(e: Employee):
    print("Jeżeli nie ma zmiany danych ENTER")
    first_name = input("Podaj imię pracownika: ") or e.first_name
    last_name = input("Podaj nazwisko pracownika: ") or e.last_name
    birthday = input("Podaj datę urodzenia [YYYY-MM-dd]: ") or e.birthday
    country = input("Kraj: ") or e.address.country
    city = input("Miasto: ") or e.address.city
    street = input("Ulica: ") or e.address.street
    postal_code = input("Kod pocztowy: ") or e.address.postal_code

    connection.execute("UPDATE addresses SET country=?, city=?, street=?, postal_code=? WHERE address_id=?",
                       (country, city, street, postal_code, e.address.address_id))
    connection.execute("UPDATE employees SET first_name=?, last_name=?, birthday=? WHERE pesel=?",
                       (first_name, last_name, birthday, e.pesel))
    connection.commit()


def search_employee():
    find_employee_sql = """
         SELECT  pesel,
         first_name,
         last_name,
         birthday,
         a.address_id, 
         country,
         city,
         street,
         postal_code
         FROM employees e 
         JOIN addresses a on e.address_id = a.address_id 
         WHERE e.pesel = ?
    """
    search_pesel = input("Proszę podać PESEL do wyszukiwania: ")

    found = connection.execute(find_employee_sql, (search_pesel,)).fetchone()

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
         f"{emp.address.country} {emp.address.city}, {emp.address.street} {emp.address.postal_code}") for emp in
        employee_list
    ]
    print(
        tabulate(table_data, headers=['Imię', 'Nazwisko', 'PESEl', 'Data urodzenia', 'Adres'], tablefmt='rounded_grid'))


def list_all_employees():
    all_employees = find_all_employees()
    print_employee_table(all_employees)


def filter_employees():
    filter_employee_sql = """
             SELECT  pesel,
             first_name,
             last_name,
             birthday,
             a.address_id, 
             country,
             city,
             street,
             postal_code
             FROM employees e 
             JOIN addresses a on e.address_id = a.address_id 
             WHERE e.last_name LIKE ?
             ORDER BY e.last_name
        """
    last_name_filter = input("Proszę podać część nazwiska: ")
    filtered_by_last_name = [Employee.from_sql(*row) for row in
                             connection.execute(filter_employee_sql, (f'%{last_name_filter}%',))]

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
