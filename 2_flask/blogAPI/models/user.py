import uuid 
from database import Database
from models.blog import Blog
from flask import session
# from flask.sessions import session 


class User():

    def __init__(self,email,password,_id=None):
        self.email = email
        self.password=password
        self._id = uuid.uuid4().hex if _id is None else _id 

    @classmethod
    def get_by_email(cls,Email):
        data = Database.get_one(collection="users",query={"email":Email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls,ID):
        data = Database.get_one(collection="users",query={"_id":ID})
        if data is not None:
            return cls(**data)


    @staticmethod
    def login_valid(Email,Password):
        user = User.get_by_email(Email=Email)
        if user is not None:
            return user.password == Password
        return False

    @classmethod
    def register(cls,Email,Password):
        user = User.get_by_email(Email=Email)
        if user is None:
            #register
            new_user = cls(Email,Password)
            new_user.save()
            session['email'] = Email
            return True 
        else:
            # don't register
            return False 

    @staticmethod
    def login(user_email):
        session['email']=user_email

    @staticmethod
    def logout():
        session['email'] = None 

    

    def get_blogs(self):
        return Blog.getBlogsAuthorID(self._id)

    def new_blog(self,title,description):
        blog = Blog(author=self.email,title=title,description=description,author_id=self._id)
        blog.save()

    @staticmethod
    def new_post(blog_id,title,content):
        blog = Blog.getBlog(blogID=blog_id)
        blog.newBlogPost(title=title,content=content)



    def json(self):
        return {
            "email":self.email,
            "_id":self._id,
            "password":self.password # it's not safe 
        }

    def save(self):
        Database.create("users",self.json())