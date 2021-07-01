import os 
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(basedir,"firstdata.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app) 

class Puppy(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self,name,age):
        self.age = age 
        self.name = name 

    def __repr__(self):
        return f"name: {self.name}  age: {self.age}"