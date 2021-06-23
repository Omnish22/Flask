from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def index():
    puppies = ["Golden Retriver","Huskie","German Shefford","PuG","Pamerian","Lebra","Great Den"]

    return render_template("controlflowtemplate.html",puppylist=puppies)


if __name__=="__main__":
    app.run(debug=True)