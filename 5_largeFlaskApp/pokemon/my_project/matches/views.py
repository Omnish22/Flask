from my_project.matches.forms import AddForm, DeleteForm
from my_project.models import Match,Trainer, Pokemon
from flask import Blueprint , render_template, redirect, url_for 
from my_project import db 


match_blueprint = Blueprint('matches',__name__,template_folder='templates/matches')


#======================================================================================
# @match_blueprint.route('/add',methods=['GET','POST'])
# def add():
#     form = AddForm()
#     if form.validate_on_submit():
#         trainer1_id = form.trainer1_id.data 
#         trainer2_id = form.trainer2_id.data
#         pokemon1_id = form.pokemon1_id.data 
#         pokemon2_id = form.pokemon2_id.data 

#         new_match = Match(trainer1_id,pokemon1_id,trainer2_id,pokemon2_id)
#         db.session.add(new_match)
#         db.session.commit()

#         return redirect(url_for('matches.list'))
#     return render_template('add_match.html',form=form)

@match_blueprint.route('/add',methods=['GET','POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        trainer1 = form.trainer1.data 
        pokemon1 = form.pokemon1.data 
        trainer2 = form.trainer2.data
        pokemon2 = form.pokemon2.data 

        all_trainers = Trainer.query.all()
        all_pokemon = Trainer.query.all()
        print(all_trainers)
        print(all_pokemon)
        if (trainer1 in all_trainers) and (trainer2 in all_trainers) and (pokemon1 in all_pokemon) and (pokemon1 in all_pokemon):
        # if True:


            new_match = Match(trainer1,pokemon1,trainer2,pokemon2)
            db.session.add(new_match)
            db.session.commit()
            return redirect(url_for('matches.list'))

        return redirect(url_for('matches.list'))
    return render_template('add_match.html',form=form)
#======================================================================================


@match_blueprint.route('/delete',methods=['GET','POST'])
def delete():
    form = DeleteForm()
    if form.validate_on_submit():
        id = form.match_id.data 
        rem_match=Match.query.get(id)
        db.session.delete(rem_match)
        db.session.commit()
        return redirect(url_for('matches.list'))
    return render_template('delete_match.html',form=form)


@match_blueprint.route('/list')
def list():
    matches = Match.query.all()
    return render_template('list.html',matches = matches)
    