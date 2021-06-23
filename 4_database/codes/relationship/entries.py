from model import db, Puppy, Toy, Owner 

# CREATING PUPPIES
bruno = Puppy('Bruno')
rufus = Puppy('Rufus')
sharon = Puppy('Sharon')

db.session.add_all([bruno,rufus,sharon])
db.session.commit()

print(Puppy.query.all())

# CREATE OWNER 
omi = Owner('Omnish',Puppy.query.filter_by(name='Bruno').first().id)
jose = Owner('Jose',Puppy.query.filter_by(name='Rufus').first().id)
shalini = Owner('Shalini',Puppy.query.filter_by(name='Sharon').first().id)

# CREATE TOY 
toy1 = Toy('Chew Toy',Puppy.query.filter_by(name='Bruno').first().id)
toy2 = Toy('Ball',Puppy.query.filter_by(name='Bruno').first().id)
toy3 = Toy('Boomerang',Puppy.query.filter_by(name='Rufus').first().id)

db.session.add_all([omi,jose,shalini,toy1,toy2,toy3])
db.session.commit()

bruno = Puppy.query.filter_by(name='Bruno').first()
print(bruno)
bruno.report_toys()