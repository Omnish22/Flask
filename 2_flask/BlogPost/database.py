import pymongo

class Database():
    uri = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.uri)
        Database.DATABASE = client['miniBlogPost']

    @staticmethod
    def add(collection,data):
        Database.DATABASE[collection].insert(data)
    
    @staticmethod
    def getAll(collection,query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def get(collection,query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection,identifierQuery,updateQuery):
        Database.DATABASE[collection].update(identifierQuery,{"$set":updateQuery})
    
    @staticmethod
    def delete(collection,query):
        Database.DATABASE[collection].remove(query)

    