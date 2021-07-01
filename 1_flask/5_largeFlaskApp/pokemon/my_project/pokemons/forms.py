from flask import Flask
from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, SubmitField, SelectField

class AddForm(FlaskForm):
    name = StringField('Name of Pokemon: ')
    type = SelectField("Type of Pokemon", choices=[('Fire','fire'),('Lightning','light'),('Grass','grass'),('Stone','stone'),('Water','water'),('Ghost','ghost'),('Legendary','legend'),('Other','other')])

    submit = SubmitField('Submit')


class DeleteForm(FlaskForm):
    id = IntegerField('Pokemon ID: ')
    submit = SubmitField('Submit')

