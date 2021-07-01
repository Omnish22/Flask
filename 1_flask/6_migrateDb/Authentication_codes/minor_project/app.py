from flask.globals import request
from my_project import db, app 
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from my_project.models import User 
# import requests as r
# import flask 
from my_project.forms import LoginForm, RegistrationForm 

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You Logged Out")
    return redirect(url_for('home'))

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash("Logged in Successfully!")

            next = request.args.get('next') # if user try to get the page which require login flask will save that requested page as next and throw a login page to login first then we will grab that requested page
            print(next)
            if next == None or not next[0]=='/':
                next = url_for('welcome_user')
                print(next)
            
            return redirect(next)
    return render_template('login.html',form=form)


@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,username=form.username.data,password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash("Thanks for registeration")
        return redirect(url_for('login'))
    return render_template('register.html',form=form)

if __name__=='__main__':
    app.run(debug=True)