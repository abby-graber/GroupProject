from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    tracking_number = Column(String(100))
    order_status = Column(String(100))
    total_price = Column(DECIMAL(10, 2))
    description = Column(String(100))

    order_details = relationship("OrderDetail", back_populates="order")
    ratings_and_reviews = relationship("RatingAndReview", back_populates="order")
