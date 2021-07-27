from flask import Blueprint, request, render_template
import json 
from models.items import Item

item_blueprint = Blueprint("items",__name__)

@item_blueprint.route("/new",methods=["GET","POST"])
def new_item():
    if request.method == "POST":
        url = request.form['url']
        tag_name = request.form['tagName']
        # query = request.form['query'] # query is string while it should be dictionary
        query = json.loads(request.form['query']) # but string should be valid json format i.e. {"id":"..."}

        Item(url,tag_name,query).save()
    return render_template("new_item.html")
