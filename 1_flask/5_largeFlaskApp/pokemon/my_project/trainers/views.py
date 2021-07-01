from my_project.trainers.forms import AddForm 
from flask import Blueprint, render_template, redirect, url_for 
from my_project.models import  Trainer
from my_project import db 

trainer_blueprint = Blueprint('trainer',__name__,template_folder='templates/trainers')

@trainer_blueprint.route('/add',methods=['GET','POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        name=form.name.data 
        pokemon_id = form.pokemon_id.data 
        new_trainer = Trainer(name,pokemon_id)
        db.session.add(new_trainer)
        db.session.commit()
        return redirect(url_for('pokemons.list'))
    return render_template('add_trainer.html',form=form)

