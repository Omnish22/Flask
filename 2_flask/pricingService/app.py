
# url="https://www.flipkart.com/apple-ipad-pro-2021-3rd-generation-8-gb-ram-256-rom-11-inches-wi-fi-only-space-grey/p/itm6dd0764296f1e?pid=TABG2DM4AJNPEJUZ&lid=LSTTABG2DM4AJNPEJUZKIVYR7&marketplace=FLIPKART&q=ipad+pro&store=tyy%2Fhry&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_4_na_na_na&fm=SEARCH&iid=9aca1736-73e0-4952-aad9-06475381a4dc.TABG2DM4AJNPEJUZ.SEARCH&ppt=hp&ppn=homepage&ssid=vm0qn17b000000001626721049641&qH=03e7257babd850e9"

from flask import Flask , render_template, request
from views.alerts import alert_blueprint
''' Items are going to be created internally and not by users '''
# from views.items import item_blueprint


app = Flask(__name__)


# app.register_blueprint(item_blueprint,url_prefix="/items") # /items/new
app.register_blueprint(alert_blueprint,url_prefix="/alerts")





if __name__ == "__main__":
    app.run(debug=True)