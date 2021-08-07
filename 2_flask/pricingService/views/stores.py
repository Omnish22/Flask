from flask import Blueprint, redirect, render_template,request,url_for 
import json 
from models.store import Store 
from models.user.decorators import requires_admin,requires_login


store_blueprint = Blueprint('stores',__name__)

@store_blueprint.route("/")
@requires_login # if not log in then there is no email in session and stores view page will throw error 
def index():
    stores = Store.getAll()
    return render_template("stores/store_index.html",stores=stores)


@store_blueprint.route("/new",methods=['GET','POST'])
@requires_admin
def new_store():
    if request.method=="POST":
        name = request.form['name']
        url_prefix = request.form['url_prefix']
        tag_name = request.form['tag_name']
        query = json.loads(request.form['query'])
        print("Store created")
        Store(name=name,url_prefix=url_prefix,tag_name=tag_name,query=query).save()
    return render_template("stores/new_store.html")


@store_blueprint.route("/edit/<string:store_id>",methods=['GET','POST'])
@requires_admin
def edit_store(store_id):
    store = Store.get_by_id(store_id)
    if request.method=="POST":
        store_name = request.form['name']
        url_prefix = request.form['url_prefix']
        tag_name = request.form['tag_name']
        query = request.form['query']

        store.name=store_name 
        store.url_prefix=url_prefix
        store.tag_name = tag_name
        store.query = query 

        store.save()
        return redirect(url_for(".index"))

    return render_template("stores/edit_store.html",store=store)




@store_blueprint.route("/delete/<string:store_id>")
@requires_admin
def delete_store(store_id):
    Store.get_by_id(store_id).remove()
    return redirect(url_for(".index"))
    