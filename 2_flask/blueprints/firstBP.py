from flask import Flask
from firstBP_model import blueprint


app = Flask(__name__)

# @app.route("/")
# def home():
#     return "hello World"

app.register_blueprint(blueprint=blueprint,url_prefix="/greetings") # it's route will be /greetings/name



if __name__=="__main__":
    app.run(debug=True)