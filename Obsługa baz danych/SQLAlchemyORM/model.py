from sqlalchemy import *
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, registry
from typing import Optional, Annotated

str100 = Annotated[str, 100]
str255 = Annotated[str, 255]


class Base(DeclarativeBase):
    type_annotation_map = {
        str100: String(100),
        str255: String(255)
    }


intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]


class User(Base):
    __tablename__ = 'users'

    id: Mapped[intpk]
    name: Mapped[str]
    full_name: Mapped[str255]
    login: Mapped[str100] = mapped_column(default='NO_LOGIN')
    other: Mapped[Optional[str]]


# Imperatywnie/Klasyczny
mapped_registry = registry()

user_table = Table(
    'users',
    mapped_registry.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('full_name', String(255)),
    Column('login', String(100), default='NO_LOGIN'),
    Column('other', String, nullable=True),
)


class User:
    pass


mapped_registry.map_imperatively(User, user_table)

Capital = Annotated[str, 'To jest string z dużej litery', 'sadasd', 'asdasdas']
name: Capital = 'andrzej'
print(type(name))


def test(name: Capital):
    pass


print(test.__annotations__['name'].__metadata__)
