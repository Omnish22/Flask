from flask import Flask, render_template, session, flash, redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField 

app = Flask(__name__)

app.config['SECRET_KEY'] = 'key' 

class SimpleForm(FlaskForm):
    submit = SubmitField("Submit")


@app.route("/",methods=['GET','POST'])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        flash("You just clicked submit button!!!")
        return redirect(url_for('index'))

    return render_template("index3.html",form=form)

if __name__=="__main__":
    app.run(debug=True)