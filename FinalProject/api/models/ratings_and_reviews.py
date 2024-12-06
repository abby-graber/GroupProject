from sqlalchemy import Column, ForeignKey, Integer, String, Text, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base
from .menu_items import MenuItem
from .customers import Customer
from .orders import Order


class RatingAndReview(Base):
    __tablename__ = "ratings_and_reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    review_text = Column(Text, nullable=True)
    score = Column(Integer, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), nullable=False)  # Link to menu_items

    # Relationships
    customer = relationship("Customer", back_populates="ratings_and_reviews")
    order = relationship("Order", back_populates="ratings_and_reviews")
    menu_item = relationship("MenuItem", back_populates="ratings_and_reviews")

    def __repr__(self):
        return f"<RatingAndReview(id={self.id}, score={self.score}, customer_id={self.customer_id}, order_id={self.order_id}, menu_item_id={self.menu_item_id})>"