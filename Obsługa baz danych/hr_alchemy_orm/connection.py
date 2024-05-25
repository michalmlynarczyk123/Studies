from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

load_dotenv()
password = os.environ.get('DATABASE_PASSWORD')
user = 'mimlynar'
database = 'mimlynar'
host = 'morfeusz.wszib.edu.pl'
driver = 'ODBC+Driver+18+for+SQL+Server'

# dialect+driver://username:password@host:port/database?dodatkowe_opcje
engine = create_engine(
    f'mssql+pyodbc://{user}:{password}@{host}/{database}?driver={driver}&Encrypt=no'
)

__Session = sessionmaker(engine)

db = __Session
