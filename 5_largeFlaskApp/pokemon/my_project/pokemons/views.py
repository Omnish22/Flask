from operator import ne
from my_project.pokemons.forms import AddForm, DeleteForm
from flask import Blueprint, render_template, redirect, url_for 
from my_project.models import Pokemon
from my_project import db 

pokemon_blueprint = Blueprint('pokemons',__name__,template_folder='templates/pokemons')

@pokemon_blueprint.route('/add',methods=['GET','POST'])   # register as pokemon/add
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        type = form.type.data 
        new_pokemon = Pokemon(name,type)
        db.session.add(new_pokemon)
        db.session.commit()
        return redirect(url_for('pokemons.list'))

    return render_template('add_pokemon.html',form=form)


@pokemon_blueprint.route('/delete',methods=['GET','POST'])
def delete():
    form = DeleteForm()

    if form.validate_on_submit():
        id = form.id.data 
        rem_pokemon = Pokemon.query.get(id)
        db.session.delete(rem_pokemon)
        db.session.commit()

        return redirect(url_for('pokemons.list'))
    return render_template('delete_pokemon.html',form = form)



@pokemon_blueprint.route('/list',methods=['GET','POST'])
def list():
    
    pokemons = Pokemon.query.all()
    if pokemons:
        return render_template('pokemons_list.html',pokemons=pokemons)
    return render_template('index.html')