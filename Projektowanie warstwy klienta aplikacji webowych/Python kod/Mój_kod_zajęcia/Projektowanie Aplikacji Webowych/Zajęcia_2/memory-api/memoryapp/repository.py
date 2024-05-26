from memoryapp.entities import Category
from memoryapp import db

def get_categories() -> list[Category]:
    return db.session.execute(db.select(Category)).scalars().all()

def create_category(category_name: str) -> Category:
    category = Category(name=category_name)

    db.session.add(category)
    db.session.commit()

    return category
