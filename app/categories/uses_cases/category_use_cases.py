from app.database.models import Category as CategoryModel
from app.categories.schemas import Category as CategorySchema
from sqlalchemy.orm import Session

class CategoryUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_category(self, category: CategorySchema):
        category_model = CategoryModel(**category.model_dump())
        self.db_session.add(category_model)
        self.db_session.commit()