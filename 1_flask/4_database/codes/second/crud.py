from flaskdb1 import db, Puppy

# CREATE 
# rufus = Puppy('rufus',10)
# db.session.add(rufus)
# db.session.commit() 

all_puppies = Puppy.query.all()
print(all_puppies) 

# SELECT
puppy_one = Puppy.query.get(1)
print(puppy_one)
puppy_two = Puppy.query.get(2)
print(puppy_two)
puppy_three = Puppy.query.get(3)
print(puppy_three)

# UPDATE
first_puppy = Puppy.query.get(1)
first_puppy.age=5
db.session.add(first_puppy)
db.session.commit()
# print(first_puppy.all())
#
# DELETE 
second_puppy = Puppy.query.get(14)
db.session.delete(second_puppy)
db.session.commit()

all_puppies = Puppy.query.all()
print(all_puppies)  