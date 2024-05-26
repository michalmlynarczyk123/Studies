from flask import Flask
from flask_cors import CORS
from sqlalchemy.orm import DeclarativeBase

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import Engine
from sqlalchemy import event


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///memory.db'
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)

import memoryapp.routes


@event.listens_for(Engine, 'connect')
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute('PRAGMA foreign_keys=ON')
    cursor.close()


with app.app_context():
    db.create_all()
