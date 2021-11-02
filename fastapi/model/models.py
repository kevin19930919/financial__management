from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date
from .database import Base
from sqlalchemy.orm import Session

class CryptoTrade(Base):
    __tablename__ = 'CryptoTrade'

    id = Column(Integer, primary_key=True, index=True)
    target = Column(String(80), unique=True, nullable=False)
    price = Column(Integer, unique=False, nullable=False)
    quantity = Column(Integer, unique=False, nullable=False)
    date = Column(Date)

    # def get_user(db: Session, user_id: int):
    #     return db.query(models.User).filter(models.User.id == user_id).first()


    # def get_user_by_email(db: Session, email: str):
    #     return db.query(models.User).filter(models.User.email == email).first()


    # def get_users(db: Session, skip: int = 0, limit: int = 100):
    #     return db.query(models.User).offset(skip).limit(limit).all()


    # def create_user(db: Session, user: schemas.UserCreate):
    #     fake_hashed_password = user.password + "notreallyhashed"
    #     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    #     db.add(db_user)
    #     db.commit()
    #     db.refresh(db_user)
    #     return db_user


    # def update_user(db: Session, user_id: int, update_user: schemas.UserUpdate):
    #     db_user = db.query(models.User).filter(models.User.id == user_id).first()
    #     if db_user:
    #         update_dict = update_user.dict(exclude_unset=True)
    #         for k, v in update_dict.items():
    #             setattr(db_user, k, v)
    #         db.commit()
    #         db.flush()
    #         db.refresh(db_user)
    #         return db_user


    # def delete_user(db: Session, user_id: int):
    #     db_user = db.query(models.User).filter(models.User.id == user_id).first()
    #     if db_user:
    #         db.delete(db_user)
    #         db.commit()
    #         db.flush()
    #         return db_user


class USStockTrade(Base):
    
    __tablename__ = 'USStockTrade'
    id = Column(Integer, primary_key=True, index=True)
    target = Column(String(80), unique=True, nullable=False)
    price = Column(Integer, unique=False, nullable=False)
    quantity = Column(Integer, unique=False, nullable=False)
    date = Column(Date)