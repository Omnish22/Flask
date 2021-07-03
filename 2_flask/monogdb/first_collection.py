import pymongo 

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['miniBlogPost']
collection = database['students']

collection.remove({"name":"Natsu"})
collection.insert({"name":"Natsu","anime":"Fairy Tail","age":24})
students = collection.find({})  

for student in students:
    print(student)