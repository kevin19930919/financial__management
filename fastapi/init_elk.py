import sys
from core.elasticsearch_interface import ElasticsearchHandler

IndexSettings = [
    {
        "name":"job",
        "settings":
            {"mappings": {
                "properties": {
                    "title": {
                        "type": "text"
                    },
                    "payment": {
                        "type": "text"
                    }
                }
            }
        }
    },
]

es_instance = ElasticsearchHandler()
for index_info in IndexSettings:
    es_instance.create_index(index_name=index_info["name"], settings=index_info["settings"])

