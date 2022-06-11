from elasticsearch import Elasticsearch
#initial elasticsearch
es = Elasticsearch(hosts='localhost', port=9200)
#show elasticsearch info
print("elasticsearch info",es.info())
class ElasticsearchHandler():
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance
    
    def __init__(self):
        self.__es_instance = es
    
    def create_index(self, index_name, settings):
        self.__es_instance.indices.create(index=index_name, ignore=400, body=settings)
    
    def insert_in_index_prices(self, data):
        try:
            #use index to generate index automatically
            self.__es_instance.index(index="prices", body=data)
        except Exception as e:
            print(f"insert in index price fail:{e}")   
