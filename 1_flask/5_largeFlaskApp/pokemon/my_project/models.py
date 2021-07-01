# from sqlalchemy.orm import backref
from my_project import db 




class Pokemon(db.Model):
    __tablename__ = 'pokemons'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    type = db.Column(db.Text)
    trainer = db.relationship('Trainer',backref='pokemon',uselist=False)
    # match = db.relationship('Match',backref='pokemon',lazy='dynamic')
    # match2 = db.relationship('Match',backref='pokemon',lazy='dynamic')

    # pokemon1_id = db.Column(db.Integer, db.ForeignKey('pokemons.id'))
    # pokemon2_id = db.Column(db.Integer, db.ForeignKey('pokemons.id'))
    # pokemon1_id = db.relationship('Pokemon', foreign_keys=[pokemon1_id])
    # pokemon2_id = db.relationship('Pokemon', foreign_keys=[pokemon2_id])



    def __init__(self,name,type):
        self.name = name
        self.type = type 

    def __repr__(self):
        if self.trainer:
            return f"{self.name} is a {self.type} type of pokemon trained by {self.trainer.name}"
        return f"{self.name} is a {self.type} type of pokemon has no trainer yet!!!"

class Trainer(db.Model):
    __tablename__='trainers'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    pokemon_id = db.Column(db.Integer,db.ForeignKey('pokemons.id')) # pokemons.id is tablename.column
    # match = db.relationship('Match',backref='trainer',lazy='dynamic')
    # match2 = db.relationship('Match',backref='trainer',lazy='dynamic')

    # trainer1_id = db.Column(db.Integer,db.ForeignKey('trainers.id'))
    # trainer2_id = db.Column(db.Integer,db.ForeignKey('trainers.id'))
    # trainer1 = db.relationship('Match', foreign_keys=[trainer1_id])
    # trainer2 = db.relationship('Match', foreign_keys=[trainer2_id])


    def __init__(self,name,pokemon_id):
        self.name = name 
        self.pokemon_id = pokemon_id 


# class Match(db.Model):
#     __tablename__= 'matches'

#     id = db.Column(db.Integer,primary_key=True)
#     trainer1_id = db.Column(db.Integer,db.ForeignKey('trainers.id'))
#     trainer2_id = db.Column(db.Integer,db.ForeignKey('trainers.id'))

#     pokemon1_id = db.Column(db.Integer, db.ForeignKey('pokemons.id'))
#     # pokemon2_id = db.Column(db.Integer, db.ForeignKey('pokemons.id'))

#     # pokemon1_id = db.relationship('Pokemon', foreign_keys=[pokemon1_id])
#     # pokemon2_id = db.relationship('Pokemon', foreign_keys=[pokemon2_id])
#     # trainer1_id = db.relationship('Trainer', foreign_keys=[trainer1_id])
#     # trainer2_id = db.relationship('Trainer', foreign_keys=[trainer2_id])



#     def __init__(self,trainer1_id,pokemon1_id,trainer2_id,pokemon2_id):
#         self.trainer1_id = trainer1_id
#         self.pokemon1_id = pokemon1_id
#         self.trainer2_id = trainer2_id
#         self.pokemon2_id = pokemon2_id

#     def __repr__(self):
#         # return f"{self.trainer1.name} with {self.pokemon1.name} VS {self.trainer2.name} with {self.pokemon2.name}"
#         # return f"{self.trainer1_id.name} VS {self.trainer2_id.name}"
#         return f"{self.trainer1_id} vs {self.pokemon2_id}"



class Match(db.Model):
    __tablename__= 'matches'

    id = db.Column(db.Integer,primary_key=True)
    trainer1 = db.Column(db.Text)
    trainer2 = db.Column(db.Text)

    pokemon1 = db.Column(db.Text)
    pokemon2 = db.Column(db.Text)



    def __init__(self,trainer1,pokemon1,trainer2,pokemon2):
        self.trainer1 = trainer1
        self.pokemon1 = pokemon1
        self.trainer2 = trainer2
        self.pokemon2 = pokemon2

    def __repr__(self):
        return f"{self.trainer1} with {self.pokemon1} VS {self.trainer2} with {self.pokemon2}"
        # return f"{self.trainer1_id.name} VS {self.trainer2_id.name}"
        # return f"{self.trainer1} vs {self.trainer}"
