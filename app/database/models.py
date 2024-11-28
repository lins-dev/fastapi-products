from sqlalchemy import Column, Integer, String, DateTime, func
from app.database.base import Base


class Category(Base):
    __tablename__ = 'categories'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    slug = Column('slug', String, nullable=False)
    created_at = Column('created_at', DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column('updated_at', DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)