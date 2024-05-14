from connection import connection

cursor = connection.cursor()
cursor.execute("SELECT * FROM users")

for row in cursor:
    print(row)