from flaskdb1 import db, Puppy 

db.create_all() 

sam = Puppy('sammy',12)
bruno = Puppy('Bruno',8)

db.session.add(sam)
db.session.add(bruno)
db.session.commit()

print(sam)