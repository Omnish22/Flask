from flask import Flask 

app = Flask(__name__)


@app.route("/")
def index():
    return f"<h1>Welcome! Go to /puppy_latin/name to see your name in puppy latin!</h1>"


@ app.route("/puppy_latin/<name>")
def latinName(name):
    if name[-1]=='y':
        return f"<h1>Hi! {name}! Your Puppy Latin name is {name[:-1]}iful</h1>"
    else:
        return f"<h1>Hi! {name}! Your Puppy Latin name is {name}y</h1>"


if __name__ == "__main__":
    app.run(debug=True)

