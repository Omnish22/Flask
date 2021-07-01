from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField 
from wtforms.validators import DataRequired, Email, EqualTo 
from wtforms import ValidationError 
from my_project.models import User 


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log in')


class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('password_confirmation',message='Password must be same')])
    password_confirmation = PasswordField('ConfirmPassword',validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("This Email is already Registerd!")
    
    def check_username(self,field):
        if User.query.filter_by(username=field).first():
            raise ValidationError("This Username is already taken!...Try another one!")


