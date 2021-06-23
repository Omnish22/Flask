from flask import Flask, session, render_template,redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators 
from wtforms import ( StringField, BooleanField, DateTimeField,
                      RadioField, SelectField, TextField, TextAreaField,
                      SubmitField
)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'key'

class InfoForm(FlaskForm):
    breed = StringField("What's your breed",validators=[DataRequired()])
    neutered = BooleanField("Have you been neutered")
    mood = RadioField('Please choose your mood:', choices=[('mood_one','Good'),('mood_two','Excited')])
    food_choices = SelectField(u"Pick the food you like:",choices=[('chi','Chicken'),('mut','Mutton'),('fish','Fish')])
    feedback = TextAreaField()
    submit = SubmitField("Submit")


@app.route("/",methods=['GET','POST'])
def index():
    form = InfoForm()

    if form.validate_on_submit():
        session['breed']= form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data 
        session['food_choice'] = form.food_choices.data
        session['feedback'] = form.feedback.data 

        return redirect(url_for("thank_you"))

    return render_template("index2.html",form=form,session=session)

@app.route("/thankyou")
def thank_you():
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(debug=True,port=5000)

