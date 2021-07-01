import os 
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 


app = Flask(__name__)

app.config['SECRET_KEY'] = 'aisehi'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
Migrate(app,db)


from my_project.pokemons.views import pokemon_blueprint
from my_project.trainers.views import trainer_blueprint
from my_project.matches.views import match_blueprint

app.register_blueprint(pokemon_blueprint,url_prefix='/pokemons')
app.register_blueprint(trainer_blueprint,url_prefix='/trainers')
app.register_blueprint(match_blueprint,url_prefix='/matches')
