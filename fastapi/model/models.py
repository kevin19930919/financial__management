from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date
import sys
sys.path.append('./fastapi/model')
from database import Base, hash_func

class Trade(Base):
    __tablename__ = 'Trade'

    id = Column(Integer, primary_key=True, index=True)
    trade_hash = Column(String(80), default=hash_func, unique=True, nullable=False)
    price = Column(Float, unique=False, nullable=False)
    quantity = Column(Float, unique=False, nullable=False)
    date = Column(Date)
    
    crypto = relationship("Crypto", back_populates="trade")
    us_stock = relationship("USStock", back_populates="trade")


class Crypto(Base):
    __tablename__ = 'Crypto'

    id = Column(Integer, primary_key=True, index=True)
    target = Column(String(80), unique=False, nullable=False)
    exchange = Column(String(80), unique=False, nullable=False)
    # price = Column(Float, unique=False, nullable=False)
    # quantity = Column(Float, unique=False, nullable=False)
    # date = Column(Date)
    trade_hash = Column(Integer, ForeignKey("Trade.trade_hash"))

    trade = relationship("Trade", back_populates="crypto")

class USStock(Base):
    
    __tablename__ = 'USStock'

    id = Column(Integer, primary_key=True, index=True)
    target = Column(String(80), unique=False, nullable=False)
    # price = Column(Float, unique=False, nullable=False)
    # quantity = Column(Float, unique=False, nullable=False)
    # date = Column(Date)
    trade_hash = Column(Integer, ForeignKey("Trade.trade_hash"))

    trade = relationship("Trade", back_populates="us_stock")