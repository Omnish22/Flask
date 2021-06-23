# my_project > owners > forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField("Name of the Owner: ")
    puppy_id = IntegerField("Id of Puppy: ")
    submit = SubmitField("Get Puppy")

