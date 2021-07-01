from flask_wtf import FlaskForm
from wtforms import  StringField,SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user 
from companyblog.models import User

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = StringField('Password',validators=[DataRequired()])
    submit = SubmitField('Log In')



class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('User Name',validators=[DataRequired()])
    password = StringField('Password',validators=[DataRequired(),EqualTo('confirm_password')])
    confirm_password = StringField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This Email has been already Registered!!!')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This Username has already been taken!!!')

    

class UpdateUserForm(FlaskForm):
    email = StringField('Update Email',validators=[DataRequired(),Email()])
    username = StringField('Update Username', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("This Email address has been already taken!!!")

    def check_username(self,field):
        if User.query.filter_by(username=field.data):
            raise ValidationError("This Username has been already taken!!!")