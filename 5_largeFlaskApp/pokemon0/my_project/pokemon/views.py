from my_project import db,app
from flask import Blueprint, render_template, redirect, url_for
from my_project.pokemon.forms import AddForm, DeleteForm
from my_project.models import Pokemon


pokemon_blueprints = Blueprint('pokemon',__name__,template_folder='templates/pokemon')

@pokemon_blueprints.route('/add',methods=['GET','POST'])
def add_pokemon():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        type = form.type.data
        new_pokemon = Pokemon(name,type)
        db.session.add(new_pokemon)
        db.session.commit()

        return redirect(url_for('pokemon_list'))
    return render_template('add.html',form=form)



@pokemon_blueprints.route('/pokemon_list')
def pokemon_list():
    pokemons = Pokemon.query.all()
    return render_template('list.html',pokemons=pokemons)



@pokemon_blueprints.route('/pokemon_delete')
def pokemon_delete():
    form = DeleteForm()
    if form.validate_on_submit():
        id = form.id.data 
        rem_pokemon = Pokemon.query.get(id)
        db.session.delete(rem_pokemon)
        db.session.commit()

        return redirect(url_for('pokemon.pokemon_list'))
    return render_template('delete.html',form=form)