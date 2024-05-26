from memoryapp.entities import Category
from memoryapp import db

def get_categories() -> list[Category]:
    return db.session.execute(db.select(Category)).scalars().all()
