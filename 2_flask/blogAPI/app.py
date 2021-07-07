from flask.helpers import make_response
from database import Database
from models.blog import Blog
from flask import Flask , render_template, request, session
from models.user import  User
from models.post import Post


app = Flask(__name__)

app.secret_key = "secret key"
#  Database.initialize()
@app.before_first_request
def database_initialize():
    return Database.initialize()


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/auth/login",methods=['GET','POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']
    if User.login_valid(email,password):
        User.login(email)
        return  render_template("profile.html",email=session['email'])
    else:
        session['email']=None
        return register()
    


@app.route("/auth/register",methods=['GET','POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']

    User.register(Email=email,Password=password)
    return render_template("profile.html",email=session['email'])


@app.route("/blogs/<string:user_id>")
@app.route("/blogs")
def user_blogs(user_id=None):
    user_id = User.get_by_email(session['email'])._id
    print("User ID: ",user_id)
    print("User Email: ",session["email"])
    if user_id is not None:
        user = User.get_by_id(user_id)
    else:
        user = User.get_by_email(session['email'])
    print("New User: ",user)
    blogs = user.get_blogs()

    return render_template("user_blogs.html",blogs=blogs,email=user.email)


@app.route('/blogs/new',methods=['GET','POST'])
def create_new_blog():
    if request.method == 'GET':
        return render_template("new_blog.html")
    else:
        title = request.form['title']
        description = request.form['description']
        user = User.get_by_email(session['email'])
        new_Blog = Blog(title,description,user.email,user._id)
        new_Blog.saveBlog()
        return make_response(user_blogs(user_id=user._id))
        # return render_template("user_blogs.html",blogs=user.get_blogs(),email=user.email)


@app.route('/posts/<string:blog_id>')
def blog_posts(blog_id):
    print("Blog_id: ",blog_id)
    print("user: ",session['email'])
    blog = Blog.getBlog(blogID=blog_id)
    posts = Blog.getblogPost(blog._id)
    return render_template('post.html',posts=posts,blog_title=blog.title,blog_id = blog._id)

@app.route('/posts/new/<string:blog_id>',methods=['POST','GET'])
def create_new_post(blog_id):
    if request.method=='GET':
        return render_template('new_post.html',blog_id=blog_id)
    else:
        title = request.form['title']
        content = request.form['content']
        user = User.get_by_email(session['email'])
        new_post = Post(blog_id=blog_id,title=title,content=content,author=user.email)
        new_post.savePost()

        return make_response(user_blogs(blog_id))



if __name__ == "__main__":
    app.run(debug=True)