from memoryapp.entities import Category
from memoryapp import db


def get_categories() -> list[Category]:
    return db.session.execute(db.select(Category)).scalars().all()


def get_category_by_id(category_id: int) -> Category:
    return db.get_or_404(Category, category_id)


def create_category(category_name: str) -> Category:
    category = Category(name=category_name)

    db.session.add(category)
    db.session.commit()

    return category


def delete_category(category_id: int):
    category = db.get_or_404(Category, category_id)

    db.session.delete(category)
    db.session.commit()
