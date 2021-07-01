import os 
from forms import AddForm, DelForm
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 

# -----------------------------------------------------------------

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aflatoon'

#-----------------------------------------------------------------------------------------
#========== DATABASE =============
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+ os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False 

db = SQLAlchemy(app)
Migrate(app,db)

#--------------------------------------------------------------------------------------------------
# ======= MODELS ===========
class Puppy(db.Model):
    __tablename__ =  'puppies'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    breed = db.Column(db.Text)

    def __init__(self,name,breed):
        self.name = name 
        self.breed = breed 

    def __repr__(self):
        return f"puppy name is {self.name}"


# --------------------------------------------------------
# ======= VIEW FUNCTIONS =========
@app.route("/")
def index():
    return render_template('home.html')

@app.route('/add',methods=['GET','POST'])
def add_puppy():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data 
        breed = form.breed.data 
        new_puppy = Puppy(name,breed)
        db.session.add(new_puppy)
        db.session.commit()

        return redirect(url_for('list_puppies'))
    return render_template('add.html',form=form)

@app.route('/list')
def list_puppies():
    puppies = Puppy.query.all()
    return render_template('list.html',puppies=puppies)

@app.route('/del',methods=['GET','POST'])
def del_puppy():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data 
        rem_puppy = Puppy.query.get(id)
        db.session.delete(rem_puppy)
        db.session.commit()
        return redirect(url_for('list_puppies'))
    return render_template('delete.html',form=form)


# --------------------------------------------------------------------
if __name__=="__main__":
    app.run(debug=True)