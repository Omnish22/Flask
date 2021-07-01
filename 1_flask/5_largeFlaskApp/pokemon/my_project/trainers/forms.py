from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, IntegerField
# from wtforms.fields.core import IntegerField 


class AddForm(FlaskForm):
    name = StringField('Name of the Trainer: ')
    pokemon_id = IntegerField('Enter Pokemon ID')
    submit = SubmitField('Submit')


