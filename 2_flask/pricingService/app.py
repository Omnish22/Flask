from flask import Flask , render_template, request
from views.alerts import alert_blueprint
from views.stores import store_blueprint
from views.users import user_blueprint
import os 

''' Items are going to be created internally and not by users '''
# from views.items import item_blueprint

app = Flask(__name__)
app.secret_key = os.urandom(64)
app.config.update(ADMIN=os.environ.get('ADMIN')) # it will update environment variable

# app.register_blueprint(item_blueprint,url_prefix="/items") # /items/new

app.register_blueprint(alert_blueprint,url_prefix="/alerts")
app.register_blueprint(store_blueprint,url_prefix="/stores")
app.register_blueprint(user_blueprint,url_prefix="/users")




if __name__ == "__main__":
    app.run(debug=True)