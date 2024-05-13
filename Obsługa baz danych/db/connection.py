import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

password = os.environ.get('DATABASE_PASSWORD')
user = 'mimlynar'
database_name = 'mimlynar'
server = 'morfeusz.wszib.edu.pl'

connection_string = (
    'DRIVER={ODBC Driver 18 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database_name};'
    f'UID={user};'
    f'PWD={password};'
    'Encrypt=no'
)

connection = pyodbc.connect(connection_string)