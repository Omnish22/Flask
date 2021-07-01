from flask import Flask , render_template, request

app = Flask(__name__)


@app.route("/")
def ind():
    return render_template("index.html")

@app.route("/result")
def result():
    username = request.args.get("username")
    upper = 0
    lower = 0 

    failed = []
    for i in username:
        if i.isupper():
            upper = upper + 1
        if i.islower():
            lower = lower + 1
        
    if upper ==0:
        failed.append("Must have an upper case letter somewhere.")
    if lower ==0:
        failed.append("Must have an lower case letter somewhere.")
    try:
        type(int(username[-1]))==int
    except:
        failed.append("Must have a number at the end.")

    length = len(failed)
    return render_template("result.html",username=username,failed=failed , length=length)

if __name__=="__main__":    
    app.run(debug=True,port=1000)