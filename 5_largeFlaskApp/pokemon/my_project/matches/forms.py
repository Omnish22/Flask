from flask_wtf import FlaskForm 
from wtforms import SubmitField, IntegerField,StringField


# class AddForm(FlaskForm):
#     trainer1_id = IntegerField('Enter Trainer1 ID: ')
#     pokemon1_id = IntegerField('Enter Pokemon1 ID: ')
#     trainer2_id = IntegerField('Enter Trainer2 ID: ')
#     pokemon2_id = IntegerField('Enter Pokemon2 ID: ')

#     submit = SubmitField('Submit')


class AddForm(FlaskForm):
    trainer1 = StringField('Enter Trainer1 Name : ')
    pokemon1 = StringField('Enter Pokemon1 Name : ')
    trainer2 = StringField('Enter Trainer2 Name : ')
    pokemon2 = StringField('Enter Pokemon2 Name : ')

    submit = SubmitField('Submit')


class DeleteForm(FlaskForm):
    match_id = IntegerField('Enter Match ID: ')

    submit = SubmitField('Submit')