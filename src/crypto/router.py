from ..database import get_db_session
from typing import List, Optional
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from . import schema
from . import service
from . import adapter


cryptoAPIRouter = APIRouter(prefix="/crypto",tags=["crypto"])

@cryptoAPIRouter.post("/trade", response_model=schema.CreateCryptoTrade)
def create_CryptoTrade(CryptoTrade: schema.CreateCryptoTrade, transaction: Session = Depends(get_db_session)):
    try:
        print('request:',CryptoTrade)
        return adapter.create_crypto_trade(transaction=transaction, CryptoTrade=CryptoTrade)
    except Exception as e:
        print('=======create crypto record fail=========:',e)
        raise HTTPException(status_code = 500, detail =  "server error")
    
@cryptoAPIRouter.get("/price", response_model=dict)
def get_cryptoPrice():
    try:
        return service.CoinMarketAPI.request_price()
    except Exception as e:
        print(e)
        raise HTTPException(status_code = 404, detail =  "source not found")