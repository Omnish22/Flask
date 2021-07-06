from database import Database 
import uuid 
import datetime

class Post():
    def __init__(self,blog_id,title,content,author,date=datetime.datetime.utcnow(),_id=None):
        self.blog_id = blog_id 
        self.title = title 
        self.content = content 
        self.author = author 
        self.date = date 
        self._id = uuid.uuid4().hex if _id is None else _id 

    def json(self):
        return  {
            "blog_id":self.blog_id,
            "title":self.title,
            "content":self.content,
            "author":self.author,
            "date":self.date,
            "_id":self._id
        }
    def savePost(self):
        Database.create(collection='posts',data=self.json())

    @classmethod
    def getPost(cls,postID):
        post_data = Database.get_one(collection="posts",query={"_id":postID})
        # return cls(blog_id=post_data['blog_id'],title=post_data["title"],content=post_data["content"],author=post_data["author"],_id=post_data["_id"])
        return cls(**post_data)
    
    @classmethod
    def getPosts(cls,blogID):
        ''' This will return all posts of particular blog'''
        posts = Database.get(collection="posts",query={"blog_id":blogID})
        return  [post for post in posts]
    
    # @classmethod
    # def getallPosts(cls):
    #     return [post for post in Database.get(collection="posts",query={})]

    @staticmethod
    def updatePostTitle(postID,updatedTitle):
        Database.update(collection="posts",identifierQuery={"_id":postID},updateQuery={"title":updatedTitle}) 

    @staticmethod
    def updatePostContent(postID,updatedContent):
        Database.update(collection="posts",identifierQuery={"_id":postID},updateQuery={"content":updatedContent})

    @staticmethod
    def deletePost(postID):
        Database.delete(collection="posts",query={"_id":postID})

    @staticmethod
    def deleteAllPost(blogID):
        Database.delete(collection="posts",query={"blog_id":blogID})

