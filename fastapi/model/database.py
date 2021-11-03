#Here is the file that defines database connection using SQLAlchemy



import sqlalchemy
# from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import yaml
from contextlib import contextmanager

# ================ AIDMS configer =====================
with open(r'./fastapi/config/config.yaml', 'r') as file:
    config = yaml.full_load(file)
# ================orm setting==========================
DATABASE_URL = f'sqlite:///{config["db_path"]}'
engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# get sqlalchemy base class
Base = declarative_base()


# Sessionmaker is a factory for initializing new Session objects. 
# Sessionmaker initializes these sessions by requesting a connection from the engine's connection pool and attaching a connection to the new Session object.
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
sessionLocal = Session()

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
# class DataBase(Base):
#     # creating a session object then initial it
#     Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#     session = Session()

#     @contextmanager
#     def auto_commit_db(self):
#         try:
#             yield
#         except Exception as e:
#             self.session.rollback()
#             raise e
#         else:
#             self.session.commit()
    
#     # ==========CRUD method==========
#     def create(self):
#         with auto_commit_db():
#             self.session.add(self)

#     def update(self):
#         with auto_commit_db():
#             pass

#     def delete(self):
#         with auto_commit_db():
#             self.session.delete(self)        







