import pyodbc

for row in pyodbc.drivers():
    print(row)