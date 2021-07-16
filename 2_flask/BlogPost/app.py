from flask import Flask, render_template, session,request,url_for
from werkzeug.utils import redirect
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
    # print("blogs: ",[blog.title for blog in blogs])
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
        return redirect(url_for("home"))
    else:
        session['email'] = None
        return redirect(url_for("register"))


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/auth/register",methods=['GET','POST'])
def registerUser():
    email=request.form['email']
    password = request.form['password']
    register_value = User.register(Email=email,Password=password)
    if register_value:
        return redirect(url_for("home"))
    else:
        return redirect(url_for("login"))


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
            return redirect(url_for('home'))
            
    else:
        return login()



@app.route("/post/<string:blog_id>")
def post(blog_id):
    blog = Blog.getBlog(blogID=blog_id)
    posts = Blog.getBlogPost(blogID=blog_id)
    posts = [posts[len(posts)-1-i] for i in range(len(posts))]
    return render_template("post.html",posts=posts,blog=blog,blogTitle = blog.title,blogID=blog_id,nposts=len(posts),session=session)


@app.route("/post/new/<string:blog_id>",methods=['GET','POST'])
def createPost(blog_id):
    blog = Blog.getBlog(blogID=blog_id)
    if session['email']==blog.author:
        if request.method=="GET":
            return render_template("createPost.html",blog_id=blog_id)
        elif request.method=="POST":
            title = request.form['title']
            content = request.form['content']
            user = User.getByEmail(Email=session['email'])
            if title not in Blog.postTitles(blog_id):
                user.newPost(blogID=blog_id,title=title,content=content)
            return redirect(url_for("post",blog_id=blog_id))
    else:
        return login()

@app.route("/blog/delete/<string:blog_id>")
def deleteBlog(blog_id):
    print("run!")
    if session:
        blog = Blog.getBlog(blogID=blog_id)
        if session['email']==blog.author:
            Blog.deleteBlog(blogID=blog_id)
            print("Delete Pressed")
            return redirect(url_for("home"))
    return redirect(url_for("login"))


@app.route("/blog/edit/<string:blog_id>",methods=['GET','POST'])
def editBlog(blog_id):
    if session:
        blog = Blog.getBlog(blogID=blog_id)
        if session['email']==blog.author:
            if request.method=="GET":
                return render_template("editBlog.html",blog=blog)
            elif request.method=="POST":
                updateTitle = request.form['title']
                updateDescription = request.form['description']
                print("title: ",updateTitle)
                Blog.updateBlogTitle(blogID=blog_id,updateTitle=updateTitle)
                Blog.updateBlogDescription(blogID=blog_id,updateDescription=updateDescription)
                return redirect(url_for("home"))
    return redirect(url_for("login"))



@app.route("/post/delete/<string_id:post_id>")
def postDelete(blog_id,post_id):
    if session:
        blog = Blog.getBlog(blogID=blog_id)
        if session['email']==blog.author:
            pass

    return redirect(url_for('login'))








if __name__ == "__main__":
    app.run(debug=True)

