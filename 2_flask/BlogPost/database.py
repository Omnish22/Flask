import pymongo

class Database():
    uri = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        ''' this will initilize the database '''
        client = pymongo.MongoClient(Database.uri)
        Database.DATABASE = client['miniBlogPost']

    @staticmethod
    def add(collection,data):
        ''' this will add data to given collection '''
        Database.DATABASE[collection].insert(data)
    
    @staticmethod
    def getAll(collection,query):
        ''' this will give all data from given collection '''
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def getOne(collection,query):
        ''' this will give one data from given collection '''
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection,identifierQuery,updateQuery):
        ''' this will update data to given collection '''
        return Database.DATABASE[collection].update(identifierQuery,{"$set":updateQuery})
    
    @staticmethod
    def delete(collection,query):
        ''' this will delete data from given collection '''
        return Database.DATABASE[collection].remove(query)

    