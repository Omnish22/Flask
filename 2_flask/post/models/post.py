from database import Database
import uuid 
import datetime

class Post():
    def __init__(self,blog_id,title,content,author,date=datetime.datetime.utcnow(),id=None):
        self.id = uuid.uuid4().hex if id is None else id
        self.blog_id = blog_id
        self.title = title 
        self.content = content
        self.author = author 
        self.date = date 

    def save_to_mongo(self):
        Database.create(collection="posts",data=self.json())

    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'title':self.title,
            'content': self.content,
            'author': self.author,
            'date': self.date
        }

    @classmethod
    def from_mongo(cls,id):
        post = Database.read(collection='posts',query={'id':id})
        return cls(blog_id=post['blog_id'],title=post['title'],content=post['content'],author=post['author'],date=post['date'],id=post['id'])
    
    @staticmethod
    def from_blog(blogID):
        return [ post for post in Database.read(collection='posts',query={"blog_id":blogID})]






