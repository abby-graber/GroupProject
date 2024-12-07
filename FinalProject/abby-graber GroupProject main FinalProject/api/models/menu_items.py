from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dish = Column(String(100), nullable=False)
    ingredients = Column(String(300), nullable=False)
    price = Column(DECIMAL, nullable=False)
    calories = Column(Integer, nullable=False)
    food_category = Column(String(50), nullable=False)

    ratings_and_reviews = relationship('RatingAndReview', back_populates='menu_item')
