from database import Database
from models.blog import Blog

class Menu():
    def __init__(self):
        # Ask user for author name
        # check if they've already got an account
        # if not , prompt them to create one 

        self.user = input("Enter your author name: ")
        self.user_blog = None # while creating post that post have blog and to give that blog from new user this will help
        if self._user_has_account():
            print(f"Welcome back {self.user}")
        else:
            self._prompt_user_for_account()
        
    

    def _user_has_account(self):
        blog = Database.read_one(collection='blogs',query={"author":self.user})
        if blog is not None:
            self.user_blog= Blog.get_from_mongo(blog['id'])
            return True
        else:
            return False 



    def _prompt_user_for_account(self):
        title = input("Enter Blog title: ")
        description = input("Enter Blog description: ")
        blog = Blog(title=title,description=description,author=self.user)
        blog.save_to_mongo()
        self.user_blog = blog



    def run_menu(self):
        # user read or write blogs?
        # if read:
        #     list blogs in db
        #     allow user to pick one 
        #     diplay posts 

        # if write:
        #     prompt to write a post and this post should have blog_id 


        read_or_write = input("Do you want to read(R) or Write(W): ")
        if read_or_write=="R":
            self._list_blogs()
            self._view_blogs()


        elif read_or_write=="W":
            self.user_blog.new_post()
        else:
            print("Thank you for blogging")

    def _list_blogs(self):
        blogs = Database.read(collection='blogs',query={})
        for blog in blogs:
            print(f"ID:{blog['id']} Title:{blog['title']} Description:{blog['description']} Author:{blog['author']}")

    def _view_blogs(self):
        blog_to_see = input("Enter the ID of the blog you'd like to read: ")
        blog = Blog.get_from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print(f"\nDate:{post['date']}, Title:{post['title']}\n{post['content']}\n")