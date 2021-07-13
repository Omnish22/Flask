from flask import Flask, render_template, session
from database import Database
from models.post import Post 
from models.blog import Blog
from models.users import User

Database.initialize()

app = Flask(__name__)




@app.route("/")
def home():
    # print("session: ",session)
    blogs = [Blog.getAllBlogs()[len(Blog.getAllBlogs())-1-i] for i in range(len(Blog.getAllBlogs()))]
    return render_template("home.html",sess=session,blogs = blogs,nblogs=len(blogs))

# @app.login("/login")
# def login():



if __name__ == "__main__":
    app.run(debug=True)

