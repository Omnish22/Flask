from database import Database 
from datetime import datetime
import uuid
from models.post import Post

class Blog():
    def __init__(self,title,description,author,author_id,date=None,_id=None):
        self.title = title
        self.description = description 
        self.author = author 
        self.author_id = author_id  # this is User ID
        self.date = datetime.utcnow() if date is None else date 
        self._id = uuid.uuid4().hex if _id is None else _id 


    def json(self):
        return {
            "title":self.title,
            "description":self.description,
            "author":self.author,
            "author_id":self.author_id,
            "date":self.date,
            "_id":self._id
        }

    def createBlog(self):
        ''' This will create Blog '''
        Database.add(collection='blogs',data = self.json()) 

    @classmethod
    def getBlog(cls,blogID):
        ''' This will give the One Blog using Blog ID'''
        blog = Database.getOne(collection="blogs",query={"_id":blogID})

        if  blog is not None:
            return cls(**blog)
        return None  
        # return cls(title=blog['title'],description=blog['description'],author=blog['author'],author_id=blog['author_id'],date=blog['date'],_id=blog['_id'])


    @classmethod
    def getBlogAuthorID(cls,authorID):
        ''' Give One Blog using AuthorID'''
        blog = Database.getOne(collection='blogs',query={'author_id':authorID})
        return cls(**blog)
        # return cls(title=blog['title'],description=blog['description'],author=blog['author'],author_id=blog['author_id'],date=blog['date'],_id=blog['_id'])
        
    @staticmethod
    def getAllBlogAuthorID(authorID):
        ''' Give all blogs of particular User '''
        blogs = Database.getAll(collection='blogs',query={'author_id':authorID})
        return [Blog(**blog) for blog in blogs]


    @classmethod
    def getAllBlogs(cls):
        ''' Give all Created Blogs '''
        blogs = Database.getAll(collection='blogs',query={})
        # print("blogs:",blogs)
        return [cls(**blog) for blog in blogs]


    @staticmethod
    def updateBlogTitle(blogID,updateTitle):
        ''' Update the Blog Title '''
        Database.update(collection='blogs',identifierQuery={'_id':blogID}, updateQuery={'title':updateTitle})
    
    @staticmethod
    def updateBlogDescription(blogID,updateDescription):
        ''' Update the Blog Description '''
        Database.update(collection='blogs',identifierQuery={"_id":blogID},updateQuery={'description':updateDescription})

    @staticmethod
    def deleteBlog(blogID):
        ''' Delete the Blog '''
        Post.deleteAllPost(blogID=blogID)
        Database.delete(collection='blogs',query={'_id':blogID})


    
    def newBlogPost(self,title,content):
        ''' This will create new Post and save it in database '''
        blog = Blog.getBlog(blogID = self._id)
        new_post = Post(title=title,content=content,blog_id=self._id)
        new_post.createPost()

    @classmethod
    def getBlogPost(cls,blogID):
        ''' This will get give all Posts related to that Blog '''
        return Post.getPostsByBlog(blogID=blogID)

    @staticmethod
    def postTitles(blogID):
        posts = Blog.getBlogPost(blogID=blogID)
        return [post['title'] for post in posts]