from datetime import date
from pydantic import BaseModel
from typing import List
import sys
sys.path.append('./fatapi/model')


class Crypto(BaseModel):
    target: str
    exchange: str
    
    class Config:
        orm_mode = True

class CreateCryptoTrade(Crypto):
    pass