from elasticsearch import Elasticsearch
from run import es

class ElasticsearchHandler():
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance
    
    def __init__(self):
        self.__es_instance = es
    
    def insert_in_index_prices(self, data):
        try:
            #use index to generate index automatically
            es.index(index="prices", body=data)
        except Exception as e:
            print(f"insert in index price fail:{e}")   
