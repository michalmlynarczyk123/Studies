from sqlalchemy import *
from connection import db, engine

metadata = MetaData()

# VARCHAR(MAX)
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

query_join = select(employee_table.join(address_table))
result = db.execute(query_join)
result.fetchall()

# 1
join = employee_table.join(address_table)
query_join = select(employee_table.c.first_name, address_table.c.country).select_from(join)
result = db.execute(query_join)
result.fetchall()

# 2
query_join = select(employee_table.c.first_name, address_table.c.country).join_from(employee_table, address_table)
result = db.execute(query_join)
result.fetchall()

# 3
query_join = select(employee_table.c.first_name, address_table.c.country).join(address_table)
result = db.execute(query_join)
result.fetchall()

query_join = select(employee_table.c.first_name, address_table.c.country) \
    .join(address_table, employee_table.c.address_id == address_table.c.address_id)

result = db.execute(query_join)
result.fetchall()

query_join = select(employee_table, address_table.c.country) \
    .join(address_table, employee_table.c.address_id == address_table.c.address_id)
result = db.execute(query_join)
result.fetchall()

# Default INNER JOINT
query_join = select(employee_table, address_table.c.country) \
    .join(address_table, employee_table.c.address_id == address_table.c.address_id, isouter=True) \
    .where(employee_table.c.last_name == 'Bułka')
result = db.execute(query_join)
result.fetchall()

# Aliasy
e = employee_table.alias()
a = address_table.alias()
query_join = select(e.c.first_name, a.c.country).join(a)
result = db.execute(query_join)
result.fetchall()

# Insert
# insert_sql = insert(employee_table)
# db.execute(insert_sql, [
#     {'pesel': '22222', 'first_name': 'Alchemy2', 'last_name': 'Alchemy2', 'birthday': '2000-01-01'},
#     {'pesel': '33333', 'first_name': 'Alchemy3', 'last_name': 'Alchemy3', 'birthday': '2000-01-01'},
# ])
# db.commit()

# Update
update_query = update(employee_table).values(first_name='Update Alchemy').where(employee_table.c.pesel == '22222')
db.execute(update_query)
db.commit()

# Delete
delete_query = delete(employee_table).where(employee_table.c.pesel.in_(['11111', '22222', '33333']))
db.execute(delete_query)
db.commit()

# Full add
insert_address_query = insert(address_table).values(country='Brazylia', city='Buenos', street='Ulica', postal_code='123456')
result = db.execute(insert_address_query)
# SELECT @@IDENTITY
address_id = result.inserted_primary_key[0]
insert_sql = insert(employee_table)
db.execute(insert_sql, [
    {'pesel': '22222', 'first_name': 'Alchemy2', 'last_name': 'Alchemy2', 'birthday': '2000-01-01', 'address_id': address_id},
])
db.commit()
