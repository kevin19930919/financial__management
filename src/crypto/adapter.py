from sqlalchemy.orm import Session
from sqlalchemy import func

from . import models
from . import schema

#TODO
def get_CryptoTrades(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Crypto).offset(skip).limit(limit).all()

def create_crypto_trade(transaction: Session, CryptoTrade: schema.CreateCryptoTrade):
    try:
        db_trade = models.Trade(
            price=CryptoTrade.price, 
            quantity=CryptoTrade.quantity,
            total_cost=CryptoTrade.price*CryptoTrade.quantity,
            date=CryptoTrade.date
        )
        transaction.add(db_trade)
        
        db_Crypto = models.Crypto(
            target=CryptoTrade.target,
            exchange=CryptoTrade.exchange,
            trade_hash=db_trade.trade_hash
            )
        transaction.add(db_Crypto)

        transaction.flush()
        transaction.commit()
        transaction.refresh(db_Crypto)
        transaction.refresh(db_trade)
    except Exception as e:
        print('============create peoblem in crud==========',e)
    return CryptoTrade

def delete_CryptoTrade(db: Session, trade_hash: str):
    db_CryptoTrade = db.query(models.Crypto).filter(models.Crypto.trade_hash == trade_hash).first()
    if db_CryptoTrade:
        db.delete(db_CryptoTrade)
        db.commit()
        db.flush()
    return db_CryptoTrade    

def get_all_crypto_costs(db: Session):
    return db.query(models.Crypto.target, func.sum(models.Trade.total_cost)).join(models.Trade).group_by(models.Crypto.target).all()