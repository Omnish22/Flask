from flask import Flask, render_template
from database import Database
from models.post import Post 
from models.blog import Blog

Database.initialize()

# blog = Blog('aise hi','bahot kaam he','omnish','omi@omi.com')

blog_id = Blog.getAllBlogs()[0]._id



Blog.deleteBlog(blog_id)

# app = Flask(__name__)


# @app.route("/")
# def home():
#     return render_template("home.html")


# if __name__ == "__main__":
#     app.run(debug=True)

