from flask import Flask , render_template, request 
import datetime

app = Flask(__name__)


data = {}
@app.route("/", methods=['GET','POST'])
def home():
    if request.method=="GET":
        print("request: ",request.method)

    elif request.method == 'POST':
        # print("request get ",request.form.get()))
        if request.form.get("title") and request.form.get("content"):
            title = request.form.get('title')
            content = request.form.get('content')
            date = datetime.datetime.today().date()
            time = datetime.datetime.today().time()
            data[title] = [content,date,time]

            

            return render_template('index.html',data=dict(reversed(list(data.items()))))
    return render_template("index.html",data=dict(reversed(list(data.items()))))

if __name__=="__main__":
    app.run(debug=True)