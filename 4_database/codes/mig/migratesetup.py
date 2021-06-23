from migratedb import Puppy, db 

db.create_all()

sam = Puppy('rohn',8,'huskie')
db.session.add(sam)
db.session.commit()
