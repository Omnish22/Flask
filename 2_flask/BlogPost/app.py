from flask import Flask, render_template, session,request, redirect
from database import Database
from models.blog import Blog
from models.users import User
from flask.helpers import make_response

Database.initialize()

app = Flask(__name__)

app.secret_key = "screate key"


@app.route("/")
def home():
    # print("session: ",session)
    blogs = [Blog.getAllBlogs()[len(Blog.getAllBlogs())-1-i] for i in range(len(Blog.getAllBlogs()))]
    return render_template("home.html",session=session,blogs = blogs,nblogs=len(blogs))

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/auth/login",methods=['GET','POST'])
def loginUser():
    email = request.form['email']
    password = request.form['password']
    if User.login_valid(Eamil=email,Password=password):
        User.login(userEmail=email)
        return home()
    else:
        session['email'] = None
        return register()


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/auth/register",methods=['GET','POST'])
def registerUser():
    email=request.form['email']
    password = request.form['password']
    register_value = User.register(Email=email,Password=password)
    if register_value:
        return home()
    else:
        return login()


@app.route("/logout")
def logout():
    User.logout()
    return make_response(login())


@app.route("/blog/new",methods=['GET','POST'])
def createBlog():
    if session:
        if request.method=='GET':
            print('session:',[(key,value) for key,value in session.items()])
            return render_template('newBlog.html',session=session)
        elif request.method=="POST":
            title = request.form['title']
            description = request.form['description']
            user = User.getByEmail(Email=session['email'])
            if title not in user.blogTitles():
                user.newBlog(title=title,description=description)
            return make_response(home())
    else:
        return login()

@app.route("/posts")
def posts():
    pass



















if __name__ == "__main__":
    app.run(debug=True)

