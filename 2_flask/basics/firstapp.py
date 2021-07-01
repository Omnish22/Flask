from flask import Flask , render_template

app = Flask(__name__)


# from user give get request to render something on page
# by default route method is GET
@app.route("/",methods=['GET'])
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True) 