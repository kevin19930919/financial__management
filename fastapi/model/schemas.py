# pydantic models,using to filter data for transact with database
from datetime import date
from pydantic import BaseModel

from typing import List

from pydantic import BaseModel


class CryptoTrade(BaseModel):
    id: int
    date: date
    target: str
    price: int
    quantity: int
    
    class Config:
        orm_mode = True

class CreateCryptoTrade(CryptoTrade):
    pass

class UpdateCryptoTrade(CryptoTrade):
    pass


class USStockTrade(BaseModel):
    id: int
    date: date
    target: str
    price: int
    quantity: int

    class Config:
        orm_mode = True        

class CreateUSStockTrade(USStockTrade):
    pass

class UpdateUSStockTrade(USStockTrade):
    pass