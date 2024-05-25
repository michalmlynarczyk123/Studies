from sqlalchemy import *


class Address:
    def __init__(self, address_id, country: str, city: str, street: str,
                 postal_code: str):
        self.address_id = address_id
        self.country = country
        self.city = city
        self.street = street
        self.postal_code = postal_code


class Employee:
    def __init__(self, first_name: str, last_name: str, birthday: str,
                 pesel: str, address: Address):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.pesel = pesel
        self.address = address

    @staticmethod
    def from_sql(pesel, first_name, last_name, birthday, address_id,
                 country, city, street, postal_code):
        if address_id is None:
            address = None
        else:
            address = Address(address_id, country, city, street, postal_code)
        return Employee(first_name, last_name, birthday, pesel, address)


metadata = MetaData()

employee_table = Table('employees', metadata,
                       Column('pesel', String(11), primary_key=True),
                       Column('first_name', String(255), nullable=False),
                       Column('last_name', String(255), nullable=False),
                       Column('birthday', Date, nullable=False),
                       Column('address_id', Integer, ForeignKey('addresses.address_id'))
                       )

address_table = Table('addresses', metadata,
                      Column('address_id', Integer, primary_key=True, autoincrement=True),
                      Column('country', String(255), nullable=False),
                      Column('city', String(255), nullable=False),
                      Column('street', String(255), nullable=False),
                      Column('postal_code', String(25), nullable=False),
                      )
