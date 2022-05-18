import sys
sys.path.append('../model')
#from ModelInterface import Base, engine
import models, schemas
from database import engine

if __name__ == '__main__':
    models.Base.metadata.create_all(bind=engine)