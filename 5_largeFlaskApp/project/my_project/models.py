# my_projects > models.py

from my_project import db 

class Puppy(db.Model):
    
    __tablename__='puppy'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner',backref='puppy',uselist=False) # Owner as class name 

    def __init__(self,name):
        self.name = name 
    
    def __repr__(self):
        if self.owner:
            return f"Puppy name: {self.name} Owned by {self.owner.name}"
        return f"Puppy name: {self.name} and has not adopted yet!!!"

class Owner(db.Model):

    __tablename__ = 'owner'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppy.id'))

    def __init__(self,name,puppy_id):
        self.name = name 
        self.puppy_id = puppy_id 

    def __repr__(self):
        return f"Owner name: {self.name}"
