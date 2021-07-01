from sqlalchemy.orm import backref
from my_project import db 


class Pokemon(db.Model):
    __tablename__='pokemons'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    type = db.Column(db.Text)
    trainer = db.relationship('Trainer',backref='pokemon',uselist=False)
    match = db.relationship('Match',backref='pokemon')

    def __init__(self,name,type):
        self.name = name 
        self.type = type 

    def __repr__(self):
        if self.trainer:
            return f"Pokemon: {self.name} Type: {self.type} Trainer: {self.trainer.name}"
        return f"Pokemon: {self.name} Type: {self.type} no trainer"

class Trainer(db.Model):
    __tablename__='trainers'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    pokemon_id = db.Column(db.Integer,db.ForeignKey('pokemons.id'))
    match = db.relationship('Match',backref='trainer')

    def __init__(self,name,pokemon_id):
        self.name=name 
        self.pokemon_id = pokemon_id 

class Match(db.Model):
    __tablename__="matches"
    id = db.Column(db.Integer,primary_key=True)
    pokemon_name1 = db.Column('Pokemon',db.ForeignKey('pokemons.name'))
    trainer_name1 = db.Column('Trainer',db.ForeignKey('trainers.name'))
    pokemon_name2 = db.Column('Pokemon',db.ForeignKey('pokemons.name'))
    trainer_name2 = db.Column('Trainer',db.ForeignKey('trainers.name'))

    def __init__(self,pokemon_name1,trainer_name1,pokemon_name2,trainer_name2):
        self.pokemon_name1 = pokemon_name1
        self.trainer_name1 = trainer_name1 
        self.pokemon_name2 = pokemon_name2
        self.trainer_name2 = trainer_name2 

    def __repr__(self):
        return f"{self.trainer_name1} with pokemon {self.pokemon_name1} VS {self.trainer_name2} with pokemon {self.pokemon_name2}"