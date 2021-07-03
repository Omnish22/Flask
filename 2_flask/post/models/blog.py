from database import Database
import datetime
import uuid 
from models.post import Post

class Blog():
    def __init__(self,title,description,author,id=None):
        self.title = title 
        self.description = description 
        self.author = author 
        self.id = uuid.uuid4().hex if id is None else id 

    def new_post(self):
        title = input("Enter Post title: ")
        content = input("Enter Post content: ")
        date = input("Enter post date, or leave blank for today (in format DDMMYYYY): ")
        if date=="":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date,"%d%m%Y")
        post = Post(blog_id=self.id, title=title,content=content, author=self.author,date=date)
        post.save_to_mongo() 


    def get_posts(self):
        ''' This will return all posts related to blog id '''
        return Post.from_blog(blogID=self.id)   

    def save_to_mongo(self):
        Database.create(collection='blogs',data=self.json())

    def json(self):
        return {
            'title':self.title,
            'description':self.description,
            'author':self.author,
            'id':self.id 

        }

    @classmethod
    def get_from_mongo(cls,id):
        blog_data = Database.read_one(collection='blogs',query={'id':id}) 
        # return blog_data
        # this blog_data contains only title, description, author, id
        # we can't call get_posts using blog_data

        # therefore create instance of Blog using blog_data
        return cls(title=blog_data['title'],description=blog_data['description'],author=blog_data['author'],id=blog_data['id'])
