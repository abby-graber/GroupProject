from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promotion_code = Column(String(50), nullable=False)
    expiration_date = Column(DATETIME, nullable=False)