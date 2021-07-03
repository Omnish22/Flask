from models.menu import Menu
from models.post import Post 
from database import Database
from models.blog import Blog

Database.initilize()

menu = Menu()
menu.run_menu()