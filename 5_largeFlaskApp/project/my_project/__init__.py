import os 
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = "aisehi"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
Migrate(app,db)


from my_project.owners.views import owners_blueprints
from my_project.puppies.views import puppies_blueprint 

app.register_blueprint(owners_blueprints,url_prefix='/owners')
app.register_blueprint(puppies_blueprint,url_prefix='/puppies')
