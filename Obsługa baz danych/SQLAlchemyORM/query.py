import datetime

from connection import Session
from sqlalchemy import select
from model_demo import Author, Address, Event, Book, BookType

session = Session()

# select_authors_query = select(Author)
# result = session.execute(select_authors_query).scalars()
#
# for a in result:
#     print(f'{a.first_name} {a.last_name} mieszka w {a.address.country} i napisał {len(a.books)} książek.')
#     for b in a.books:
#         print(f'\t{b.title}')

select_authors_query = select(Author.first_name, Address.country).join(Author.address)
result = session.execute(select_authors_query).all()

select_filter = select(Author).filter_by(id=10)
result = session.execute(select_filter).scalar_one()

author: Author = session.get(Author, 1)

# select_events = select(Event)
# result = session.execute(select_events).scalars()
#
# for e in result:
#     for p in e.participants:
#         print(type(p))


# DODAWANIE
# new_author = Author(first_name='Jacek', last_name='Placek')
# print(new_author.id)
# session.add(new_author)
# session.commit()
# print(new_author.id)

# new_author = Author(first_name='Dwa', last_name='Dwa')
# address = Address(country='Dwa Dwa Dwa')
#
# session.add(new_author)
# session.commit()
#
# address.author_id = new_author.id
#
# session.add(address)
# session.commit()

# new_author = Author(first_name='Final', last_name='Final')
# new_author.address = Address(country='FINAL FINAL')
# new_author.books = [
#     Book(title='FINAL', publication_date=datetime.date.today(), type=BookType.HORROR),
#     Book(title='FINAL 2', publication_date=datetime.date.today(), type=BookType.ROMANCE),
# ]
#
# event = Event(name='FINAL EVENT', description='JAKIŚ OPIS')
# event.participants = [new_author]
#
# session.add_all([new_author, event])
# session.commit()

# ID 15
# found = session.get(Author, 15)
# found.first_name = 'Update'
# found.last_name = 'Update'
# for book in found.books:
#     book.description = 'Jakiś opis po edycji'
# session.add(found)
# session.commit()

found = session.get(Author, 15)
session.delete(found)
session.commit()
