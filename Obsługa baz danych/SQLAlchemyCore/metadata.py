from sqlalchemy import *
from connection import db, engine

metadata = MetaData()

# VARCHAR(MAX)
employee_table = Table('employees', metadata,
                       Column('pesel', String(11), primary_key=True),
                       Column('first_name', String(255), nullable=False),
                       Column('last_name', String(255), nullable=False),
                       Column('birthday', Date, nullable=False),
                       Column('address_id', Integer)
                       )

# metadata.create_all(engine)

query = select(employee_table)
result = db.execute(query)
result.fetchall()

# print(employee_table.c.first_name)
#
# print('Andrzej' == 'Maciej')
# print(employee_table.c.first_name == 'Andrzej')
#
# expresion: BinaryExpression = employee_table.c.first_name == 'Andrzej'
# print(type(expresion))
# print(expresion.compile().params)

employees_query = select(employee_table.c.first_name, employee_table.c.last_name)
result = db.execute(employees_query)
result.fetchall()

employees_query = select(employee_table.c['first_name', 'last_name', 'pesel'])
result = db.execute(employees_query)
result.fetchall()

# SELECT TOP 3 *
limit_query = select(employee_table).limit(3)
result = db.execute(limit_query)
result.fetchall()

sort_query = select(employee_table).order_by(employee_table.c.last_name.desc()).order_by(employee_table.c.first_name)
result = db.execute(sort_query)
result.fetchall()

offset_query = select(employee_table).order_by(employee_table.c.last_name.desc()).offset(2).limit(2)
result = db.execute(offset_query)
result.fetchall()

# Filtrowanie
filter_query = select(employee_table).where(employee_table.c.pesel == '80070298761')
result = db.execute(filter_query)
result.fetchall()

# 1 sposób na AND
filter_query = select(employee_table) \
    .where((employee_table.c.address_id > 5) & (employee_table.c.address_id < 10)) \
    .order_by(employee_table.c.address_id.desc())
result = db.execute(filter_query)
result.fetchall()

# 2 sposób na AND
filter_query = select(employee_table) \
    .where(employee_table.c.address_id > 5, employee_table.c.address_id < 10) \
    .order_by(employee_table.c.address_id.desc())
result = db.execute(filter_query)
result.fetchall()

# 3 sposób na AND
filter_query = select(employee_table) \
    .where(and_(employee_table.c.address_id > 5, employee_table.c.address_id < 10)) \
    .order_by(employee_table.c.address_id.desc())
result = db.execute(filter_query)
result.fetchall()

# 1 sposób na OR
filter_query = select(employee_table) \
    .where((employee_table.c.address_id > 18) | (employee_table.c.address_id < 3)) \
    .order_by(employee_table.c.address_id.desc())
result = db.execute(filter_query)
result.fetchall()

# 2 sposób na OR
filter_query = select(employee_table) \
    .where(or_(employee_table.c.address_id > 18, employee_table.c.address_id < 3)) \
    .order_by(employee_table.c.address_id.desc())
result = db.execute(filter_query)
result.fetchall()

filter_query = select(employee_table).where(
    and_(
        employee_table.c.address_id > 10,
        or_(employee_table.c.first_name == 'Andrzej', employee_table.c.first_name == 'Małgorzata')
    )
)
result = db.execute(filter_query)
result.fetchall()

# IN
in_query = select(employee_table).where(employee_table.c.first_name.in_(['Andrzej', 'Małgorzata']))
result = db.execute(in_query)
result.fetchall()

# Like
like_query = select(employee_table).where(employee_table.c.first_name.like('And%'))
result = db.execute(like_query)
result.fetchall()

# Funkcje agregujące
count_query = select(func.count()).select_from(employee_table)
result = db.execute(count_query)
result.scalar()

# Min/Max
query_min = select(func.min(employee_table.c.birthday))
result = db.execute(query_min)
result.scalar()

group_query = select(func.year(employee_table.c.birthday), func.count().label('Liczba urodzonych w danym roku')) \
    .group_by(func.year(employee_table.c.birthday)) \
    .having(func.count() > 1) \
    .order_by(Column('Liczba urodzonych w danym roku').desc())
print(group_query)
result = db.execute(group_query)
print(result.fetchall())
