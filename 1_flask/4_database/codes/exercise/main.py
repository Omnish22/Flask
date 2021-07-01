import os
from flask import Flask, render_template, url_for, redirect 
from forms import AddForm, DelForm, OwnerForm
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from sqlalchemy.orm import backref

# ============================================================

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lageraho'

# ============================================================
# ****** DATABASE *******
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TACK_MODIFICATION'] = False 

db = SQLAlchemy(app)
Migrate(app,db)

# ============================================================================================
# ***** MODELS ******
class Puppy(db.Model):

    __tablename__='puppy'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner',backref='puppy',uselist=False)

    def __init__(self,name):
        self.name = name 
    
    def __repr__(self):
        if self.owner:
            return f"Puppy name: {self.name} Owned by {self.owner.name}"
        return f"Puppy name: {self.name} and has not adopted yet!!!"

class Owner(db.Model):

    __tablename__ = 'owner'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppy.id'))

    def __init__(self,name,puppy_id):
        self.name = name 
        self.puppy_id = puppy_id 

    def __repr__(self):
        return f"Owner name: {self.name}"


# ====================================================================================================
# ******** View Functions *********

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/add",methods=['GET','POST'])
def add_puppy():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data 
        new_puppy = Puppy(name)
        db.session.add(new_puppy)
        db.session.commit()
        return redirect(url_for('list'))
    return render_template('add.html',form=form)



@app.route('/del',methods=['GET','POST'])
def del_puppy():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data 
        rem_puppy = Puppy.query.get(id)
        db.session.delete(rem_puppy)
        db.session.commit()

        return redirect(url_for('list'))
    return render_template('delete.html',form=form)

@app.route('/list')
def list():
    puppies = Puppy.query.all()
    return render_template('list.html',puppies=puppies)


@app.route('/owner',methods=['GET','POST'])
def owner():

    form = OwnerForm()
    if form.validate_on_submit():
        name = form.name.data 
        puppy_id = form.puppy_id.data 
        new_owner = Owner(name,puppy_id)
        db.session.add(new_owner)
        db.session.commit()
         
        return redirect(url_for('list'))
    return render_template('owner.html',form=form)


# ===============================================================
if __name__ == "__main__":
    app.run(debug=True)
