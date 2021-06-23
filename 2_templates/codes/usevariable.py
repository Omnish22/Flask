from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def index():
    my_name = "Omnish Kumar"
    letters = list(my_name)
    dictionary = {"my_name":my_name}
    return render_template("basic2.html",var_name=my_name,letters_var=letters,dictionary_var=dictionary)

if __name__=="__main__":
    app.run(debug=True)