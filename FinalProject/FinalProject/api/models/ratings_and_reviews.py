from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class RatingAndReview(Base):
    __tablename__ = "ratings_and_reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    review_text = Column(String, nullable=True)
    score = Column(Integer, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)


    customer = relationship("Customer", back_populates="ratings_and_reviews")
    order = relationship("Order")