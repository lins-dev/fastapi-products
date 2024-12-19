import pytest
from app.categories.schemas import Category
from app.database.models import Category as CategoryModel

def test_category_schema():
    result = Category(
        name = 'Roupa',
        slug = 'roupa'
    )

    expected = {
        'name' : 'Roupa',
        'slug' : 'roupa'
    }
    print(f"Result: {result.model_dump()}, Expected: {expected}")
    assert result.model_dump() == {
        'name' : 'Roupa',
        'slug' : 'roupa'
    }

def test_category_schema_invalid_slug():
    with pytest.raises(ValueError):
        category = Category(
            name = 'Roupa',
            slug = 'roupa error'
        ),
    with pytest.raises(ValueError):
        category = Category(
            name = 'Roupa',
            slug = 'çça error'
        ),
    with pytest.raises(ValueError):
        category = Category(
            name = 'Roupa',
            slug = 'Roupa error'
        )