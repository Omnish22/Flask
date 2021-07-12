from flask import Flask, render_template
from database import Database
from models.post import Post 
from models.blog import Blog
from models.users import User
# from typing_extensions import ParamSpec

Database.initialize()






app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)

