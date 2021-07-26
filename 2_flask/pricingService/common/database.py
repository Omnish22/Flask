import collections
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
        