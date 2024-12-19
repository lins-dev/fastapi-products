import pytest
from app.categories.schemas import Category
from app.database.models import Category as CategoryModel
from app.categories.uses_cases.category_use_cases import CategoryUseCases

def test_if_add_category_use_cases_works(db_session):
    uc = CategoryUseCases(db_session)

    category = Category(
        name="Roupa",
        slug="roupa"
    )
    
    uc.add_category(category)
    categories_on_db = db_session.query(CategoryModel).all()

    assert len(categories_on_db) == 1
    assert categories_on_db[0].name == "Roupa"
    assert categories_on_db[0].slug == "roupa"
    print(f"Result: {categories_on_db[0].__dict__}")

    db_session.delete(categories_on_db[0])
    db_session.commit()
