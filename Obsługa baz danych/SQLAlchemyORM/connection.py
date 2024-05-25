from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker
import os

load_dotenv()
password = os.environ.get('DATABASE_PASSWORD')
user = 'mimlynar'
database = 'mimlynar'
host = 'morfeusz.wszib.edu.pl'
driver = 'ODBC+Driver+18+for+SQL+Server'

engine = create_engine(
    f'mssql+pyodbc://{user}:{password}@{host}/{database}?driver={driver}&Encrypt=no', echo=False
)

# 1 opcja
__session = Session(engine)

# Lepsza opcja
Session = sessionmaker(engine)
