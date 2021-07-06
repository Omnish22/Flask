import pymongo 


class Database():
    uri = "mongodb://127.0.0.1:27017"
    DATABASE = None 

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.uri)
        Database.DATABASE = client['miniBlogPost']

    @staticmethod
    def create(collection,data):
        ''' data = {keys:values}'''
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def get(collection,query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def get_one(collection,query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection,identifierQuery, updateQuery):
        return Database.DATABASE[collection].update(identifierQuery,{"$set":updateQuery})
    
    @staticmethod
    def delete(collection,query):
        return Database.DATABASE[collection].remove(query)

