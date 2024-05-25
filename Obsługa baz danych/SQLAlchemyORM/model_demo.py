import datetime
import enum

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, MetaData, ForeignKey, Table, Column
from sqlalchemy.schema import CreateSchema
from typing import Annotated, Optional, List
from connection import engine, Session

str100 = Annotated[str, 100]
str255 = Annotated[str, 255]
intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]

library_metadata = MetaData(schema='library_orm')


class BookType(enum.Enum):
    CRIME = 'crime'
    CRIMINAL = 'criminal'
    FANTASY = 'fantasy'
    FICTION = 'fiction'
    HISTORICAL = 'historical'
    HORROR = 'horror'
    PERSONAL_DEVELOPMENT = 'personal_development'
    ROMANCE = 'romance'
    SCIENCE_FICTION = 'science_fiction'


class Base(DeclarativeBase):
    type_annotation_map = {
        str100: String(100),
        str255: String(255)
    }
    metadata = library_metadata


events_authors = Table(
    'events_authors',
    Base.metadata,
    Column('event_id', ForeignKey('events.id')),
    Column('author_id', ForeignKey('authors.id'))
)


class Author(Base):
    __tablename__ = 'authors'
    # __table_args__ = {
    #     'schema': 'authors_orm'
    # }

    id: Mapped[intpk]
    first_name: Mapped[str255] = mapped_column('fname')
    last_name: Mapped[str255] = mapped_column('lname')

    books: Mapped[List['Book']] = relationship(backref='author', cascade='all, delete')
    # books = relationship('Book')
    address: Mapped['Address'] = relationship(back_populates='author', cascade='all, delete')

    # events: Mapped[List['Event']] = relationship(secondary=events_authors)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


class Event(Base):
    __tablename__ = 'events'

    id: Mapped[intpk]
    name: Mapped[str255]
    description: Mapped[Optional[str]]
    participants: Mapped[List['Author']] = relationship(backref='events', secondary=events_authors)


class Address(Base):
    __tablename__ = 'addresses'

    id: Mapped[intpk]
    country: Mapped[str255]
    author_id: Mapped[int] = mapped_column(ForeignKey('authors.id'))
    author: Mapped['Author'] = relationship(back_populates='address')


class Book(Base):
    __tablename__ = 'books'

    id: Mapped[intpk]
    title: Mapped[str255]
    description: Mapped[Optional[str]]
    publication_date: Mapped[datetime.date]
    type: Mapped[BookType]

    # <nazwa_tabeli>.<kolumna_pk>
    author_id: Mapped[int] = mapped_column(ForeignKey('authors.id'))
    # author: Mapped['Author'] = relationship(back_populates='books')


# session = Session()
# session.execute(CreateSchema('library_orm'))
# session.commit()

Base.metadata.create_all(engine)
