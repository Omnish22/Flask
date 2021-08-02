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
        item.load_price() # this will go to website and fetch price of the product and update in instance's price 
        item.save()
        
        Alert(name=alert_name,item_id=item._id,price_limit=price_limit).save()


    return render_template("alerts/new_alert.html")


@alert_blueprint.route("/edit/<string:alert_id>",methods=['GET','POST'])
def edit_alert(alert_id):
    alert = Alert.get_by_id(alert_id)

    if request.method == "POST":
        price_limit = float(request.form['price_limit'])
        alert.price_limit = price_limit
        alert.save()
        return redirect(url_for('.index')) # . for current blueprint 

    return render_template("alerts/edit_alert.html",alert=alert)


@alert_blueprint.route("/route/<string:alert_id>")
def delete_alert(alert_id):
    Alert.get_by_id(alert_id).remove()
    return redirect(url_for(".index"))