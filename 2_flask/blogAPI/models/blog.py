from database import Database
from models.post import Post 
from datetime import datetime
import uuid 

class Blog():
    def __init__(self,title,description,author,author_id):
        self.title = title 
        self.description = description
        self.author = author 
        self.author_id = author_id
        self.date = datetime.utcnow()
        self._id = uuid.uuid4().hex 


    def json(self):
        return {
            "title":self.title,
            "description":self.description,
            "author":self.author,
            "date":self.date,
            "author_id":self.author_id,
            "_id":self._id 
        }


    def saveBlog(self):
        ''' This will save One blog '''
        Database.create(collection="blogs",data=self.json())

    @classmethod
    def getBlog(cls,blogID):
        ''' This will get the Blog Object '''
        print("blog Id: ",blogID)
        blog_data = Database.get_one(collection="blogs",query={"_id":blogID})
        print("blog_data; ",blog_data)
        return cls(title=blog_data["title"],description=blog_data["description"],author=blog_data["author"],_id=blog_data["_id"])
        # return cls(**blog_data)

    def getAuthor(self):
        return self.author

    @classmethod
    def getallBlogs(cls):
        ''' This will get all Blogs in blogs collection '''
        blogs = Database.get(collection="blogs",query={})
        return [blog for blog in blogs]

    @classmethod
    def getBlogsAuthorID(cls,authorID):
        blogs = Database.get(collection="blogs",query={"author_id":authorID})
        return [cls(title=blog["title"],description=blog["description"],author=blog["author"],author_id=blog['author_id']) for blog in blogs]
        # return [cls(**blog) for blog in blogs]

    @classmethod
    def updateBlogTitle(cls,blogID,updatedTitle):
        ''' This will update blog Title of specific _id'''
        Database.update(collection="blogs",identifierQuery={"_id":blogID},updatedTitle={"title":updatedTitle})

    @classmethod
    def updateBlogDescription(cls,blogID,updatedDescription):
        ''' This will update blog Description of specific _id'''
        Database.update(collection="blogs",identifierQuery={"_id":blogID},updatedTitle={"title":updatedDescription})
        
    @classmethod
    def deleteBlog(cls,blogID):
        ''' This will delete blog of specific _id'''
        Post.deleteAllPost(blogID=blogID)
        Database.delete(collection="blogs",query={"_id":blogID})



    def newBlogPost(self,title,content):
        ''' This  will create Post for the specific blog '''
        # title = input("enter title of post: ")
        # content = input("enter content of post: ")
        # if Blog.getBlog(self._id):
        author = Blog.getBlog(blogID=self._id).getAuthor()
        # else:
            # author = input("enter the author: ")
        post = Post(blog_id=self._id,title=title,content=content,author=author,date=self.date)
        post.savePost()

    @classmethod
    def getblogPost(cls,blogID):
        ''' This will give all Posts related to particular Blog '''
        return Post.getPosts(blogID=blogID)
