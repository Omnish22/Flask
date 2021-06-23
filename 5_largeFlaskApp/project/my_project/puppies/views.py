# my_project > puppies > views.py

from flask import Blueprint, render_template, redirect, url_for 
from my_project.puppies.forms import AddForm, DelForm # from puppies folder then from views.py file Add and Del class imported
from my_project import db # db from __init__.py 
from my_project.models import Puppy # Puppy class from models.py 

puppies_blueprint = Blueprint('puppies',__name__,template_folder='templates/puppies') # Puppies_blueprint created


@puppies_blueprint.route('/add',methods=['GET','POST'])
def add_puppy():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data 
        new_puppy = Puppy(name)
        db.session.add(new_puppy)
        db.session.commit()
        return redirect(url_for('puppies.list')) # list ---> puppies.list
    return render_template('add.html',form=form)

@puppies_blueprint.route('/del',methods=['GET','POST'])
def del_puppy():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data 
        rem_puppy = Puppy.query.get(id)
        db.session.delete(rem_puppy)
        db.session.commit()

        return redirect(url_for('puppies.list')) # list --> puppies.list
    return render_template('delete.html',form=form)


@puppies_blueprint.route('/list')
def list():
    puppies = Puppy.query.all()
    return render_template('list.html',puppies=puppies)
