from dataclasses import dataclass
from dataclasses_json import dataclass_json

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from memoryapp import db


@dataclass_json
@dataclass
class Category(db.Model):
    __tablename__ = 'categories'

    name: Mapped[str]
    id: Mapped[int] = mapped_column(primary_key=True)


@dataclass_json
@dataclass
class Card(db.Model):
    __tablename__ = 'cards'

    term: Mapped[str]
    definition: Mapped[str]
    id: Mapped[int] = mapped_column(primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey(Category.id, ondelete='CASCADE'), nullable=False)