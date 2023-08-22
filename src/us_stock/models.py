from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date
from database import Base




class USStock(Base):
    __tablename__ = 'us_stock'

    id = Column(Integer, primary_key=True, index=True)
    target = Column(String(80), unique=False, nullable=False)
    price = Column(Float, unique=False, nullable=False)
    quantity = Column(Float, unique=False, nullable=False)
    action = Column(String(80), nullable=False)
    created_at = Column(Date)
