import pymongo
from typing import Dict 


class Database:
    uri = "mongodb://127.0.0.1:27017/pricing"
    DATABASE = pymongo.MongoClient(uri).get_database()

    @staticmethod
    def insert(collection:str,data:Dict):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection:str, query:Dict)->pymongo.cursor:
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection:str, query:Dict):
        return Database.DATABASE[collection].find_one(query)
        
    @staticmethod
    def update(collection: str, query: Dict, data: Dict)->None:
        # upsert will create new entry if we get no element
        Database.DATABASE[collection].update(query,data,upsert=True)

    @staticmethod
    def remove(collection:str, query:Dict)->Dict:
        return Database.DATABASE[collection].remove(query)

