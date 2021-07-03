from database import Database

class Post():
    def __init__(self,id,blog_id,title,content,author,date):
        self.id = id 
        self.blog_id = blog_id
        self.title = title 
        self.content = content
        self.author = author 
        self.date = date 

    def save_to_mongo(self):
        Database.insert(collection="posts",data=self.json())

    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'title':self.title,
            'content': self.content,
            'author': self.author,
            'date': self.author
        }

    @staticmethod
    def from_mongo(id):
        return Database.read(collection='post',query={'id':id})
    
    @staticmethod
    def from_blog(blogID):
        return [post for post in Database.read(collection='post',query={'blog_id':blogID})]
