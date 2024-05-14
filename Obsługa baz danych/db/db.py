from connection import connection

# Transaction 1
# connection.execute("CREATE TABLE users (id int identity, name varchar(100), age int)")
# connection.execute("INSERT INTO users (name, age) VALUES ('Andrzej', 30)")
# connection.execute("INSERT INTO users (name, age) VALUES ('Maciej', 28)")
# connection.commit()
print("commit")

# Transaction 2
old_name = input("Proszę podać stare imię: ")
new_name = input("Proszę podać nowe imię: ")

cursor = connection.cursor()
cursor.execute(f"UPDATE users SET name= ? WHERE name = ?", (new_name, old_name))
connection.commit()

print(f"{cursor.rowcount} wierszy zmieniono")

cursor.close()
connection.close()
