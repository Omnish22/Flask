import uuid 
from datetime import datetime 
from database import Database

class Post():
    def __init__(self,title,content,blog_id,date=None ,_id=None):
        self.title = title 
        self.content = content 
        self.date = datetime.utcnow() if date is None else date
        self.blog_id = blog_id  # To identify to which blog it belongs
        self._id = uuid.uuid4().hex if _id is None else _id 


    def json(self):
        ''' To store data in monogo db, first it need to convert into json '''
        return {
            "title":self.title,
            "content": self.content,
            "blog_id": self.blog_id,
            "date": self.date,
            "_id": self._id 
        }

    def createPost(self):
        ''' This will add Post to database. It is instance method '''
        Database.add(collection='posts',data=self.json())

    @staticmethod
    def getPostsByBlog(blogID):
        ''' This will give all Posts of Particular Blog by giving Blog ID. It is static method.
            It will return list of Post data '''
        return [post for post in Database.getAll(collection='posts',query={"blog_id":blogID})]

    @classmethod 
    def getPostById(cls,postID):
        ''' Using postID it will fetch Post '''
        post = Database.getOne(collection='posts',query={"_id":postID})
        # return cls(title= post['title'],content=post['content'],blog_id=post["blog_id"],date=post['date'],_id=post["_id"])
        return cls(**post)

    @staticmethod
    def updatePostTitle(postID,updatedTitle):
        ''' This will update the Title of the Post '''
        Database.update(collection='posts',identifierQuery={"_id":postID},updateQuery={"title":updatedTitle})
        
    @staticmethod
    def updatePostContent(postID,updateContent):
        ''' This will update the Content of the Post '''
        Database.update(collection='posts',identifierQuery={"_id":postID},updateQuery={"content":updateContent})

    @staticmethod    
    def deletePost(postID):
        ''' This will remove the post from Database '''
        Database.delete(collection='posts',query={"_id":postID})

    @staticmethod
    def deleteAllPost(blogID):
        ''' This will delete all the Post related to particular Blog'''
        Database.delete(collection='posts',query={})


    @staticmethod
    def postTitles(blogID):
        posts = Post.getPostsByBlog(blogID=blogID)
        return [post.title for post in posts]