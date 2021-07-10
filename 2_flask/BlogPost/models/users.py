from typing_extensions import ParamSpec
from database import Database 
import uuid
from flask import session

class User():
    def __init__(self,email,password,_id=None):
        self.email = email 
        self.password = password 
        self._id = uuid.uuid4().hex if _id is None else _id 

    def json(self):
        return {
            'email':self.email,
            'password':self.password,
            '_id':self._id
        }

    def createUser(self):
        Database.add(collection='Users',data=self.json())


    @classmethod
    def getByEmail(cls,Email):
        data = Database.getOne(collection='users',query={'email':Email})
        if data is not None:
            return cls(**data)

    
    @classmethod
    def getById(cls,userID):
        data = Database.getOne(collection='users',query={'_id':userID})
        if data is not None:
            return cls(**data)


    @staticmethod
    def login_valid(Eamil,Password):
        user = User.getByEmail(Email=Eamil)
        if user is not None:
            return Password == user.password
        return False 


    @classmethod
    def register(cls,Email,Password):
        user = User.getByEmail(Email=Email)
        if user is None:
            new_user = User(email=Email,password=Password)
            new_user.createUser()
            session['email']=Email
            return True # Register
        else:
            return False # Not Register


    @staticmethod
    def login(userEmail):
        ''' To login user it will save user email to session '''
        session['email']=userEmail
    
    @staticmethod
    def logout():
        ''' To logout user it will remove user from session '''
        session['email']= None
