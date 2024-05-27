from memoryapp.entities import Category, Card
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


def get_cards(category_id: int) -> list[Card]:
    return db.session.execute(db.select(Card).filter_by(category_id=category_id)).scalars().all()


def create_card(category_id: int, term: str, definition: str) -> Card:
    card = Card(category_id=category_id, term=term, definition=definition)

    db.session.add(card)
    db.session.commit()

    return card
