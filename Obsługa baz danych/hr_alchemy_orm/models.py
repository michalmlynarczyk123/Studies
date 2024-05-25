import datetime

from sqlalchemy import *
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from typing import Annotated, Optional
from connection import engine

hr_metadata = MetaData(schema='hr_orm_project')

str255 = Annotated[str, 255]
str25 = Annotated[str, 25]
intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]


class Base(DeclarativeBase):
    type_annotation_map = {
        str255: String(255),
        str25: String(25)
    }
    metadata = hr_metadata


class Address(Base):
    __tablename__ = 'addresses'

    address_id: Mapped[intpk]
    country: Mapped[str255]
    city: Mapped[str255]
    street: Mapped[str255]
    postal_code: Mapped[str25]
    # employee: List[Employee]


class Employee(Base):
    __tablename__ = 'employees'

    pesel: Mapped[str] = mapped_column(String(11), primary_key=True)
    first_name: Mapped[str255]
    last_name: Mapped[str255]
    birthday: Mapped[datetime.date]
    address_id: Mapped[Optional[int]] = mapped_column(ForeignKey('addresses.address_id'))
    address: Mapped[Optional['Address']] = relationship(backref='employee')


Base.metadata.create_all(engine)
