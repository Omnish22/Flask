from flask import Flask, session, render_template, redirect, url_for, flash 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField 

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class BreedForm(FlaskForm):
    breed = StringField("What is your Breed:")
    submit = SubmitField()


@app.route("/",methods=['GET','POST'])
def index():
    form = BreedForm()

    if form.validate_on_submit():
        breed = form.breed.data 
        flash(f"Your breed is {breed}")
        return redirect(url_for("index"))

    return render_template("index4.html",form=form)

if __name__=="__main__":
    app.run(debug=True)