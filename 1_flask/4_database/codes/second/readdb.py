import sqlite3 
db = sqlite3.connect("firstdata.sqlite")


q = ''' 
    SELECT * FROM Puppy;
    '''

cursor = db.cursor()
cursor.execute(q)

# row1 = cursor.fetchone()
# print(row1)


for row in cursor:
    print(row)