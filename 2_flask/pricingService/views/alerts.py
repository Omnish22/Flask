from flask import Blueprint, render_template, redirect,url_for,request
from models.store import Store 
from models.alert import Alert 
from models.items import Item 

alert_blueprint = Blueprint('alerts',__name__)


@alert_blueprint.route("/")
def index():
    alerts = Alert.getAll()
    return render_template("alerts/index.html",alerts=alerts)


@alert_blueprint.route("/new",methods=['GET','POST'])
def new_alert():
    if request.method=="POST":
        alert_name = request.form['name']
        item_url = request.form['item_url']
        # print("item_url entered:",item_url)
        price_limit = float(request.form['price_limit'])
        
        # after geting item url and price limit it will find store and then create item
        store = Store.find_by_url(item_url)
        # print("store",store)
        item = Item(item_url,store.tag_name,store.query)
        item.save()
        
        Alert(alert_name,item._id,price_limit).save()


    return render_template("alerts/new_alert.html")