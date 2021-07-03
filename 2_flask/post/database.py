import pymongo

class Database():
    uri = "mongodb://127.0.0.1:27017"
    DATABASE = None 

    @staticmethod 
    def initilize():
        client = pymongo.MongoClient(Database.uri)
        Database.DATABASE = client['miniBlogPost']
    
    @staticmethod
    def create(collection, data):
        Database.DATABASE[collection].insert(data)
    
    @staticmethod
    def read(collection,query):
        return Database.DATABASE[collection].find(query)
    
    @staticmethod
    def read_one(collection,query):
        return Database.DATABASE[collection].find_one(query)

    