import uuid 
from dataclasses import dataclass, field 
from models.model import Model
from common.utils import Utils
import models.user.errors as UserErrors
# from models.user import UserErrors
from typing import Dict


@dataclass
class User(Model):
    collection: str = field(init=False, default="users")
    email: str 
    password:str 
    _id: str = field(default_factory=lambda:uuid.uuid4().hex)


    @classmethod
    def find_by_email(cls,email:str) -> 'User':
        ''' It will find email and if 
            didn't get it will execute the 
            except block and throw an error '''
        try:
            return cls.find_one_by('email',email)
        except TypeError:
            # raise error with error message if user not found 
            raise UserErrors.UserNotFoundError("A user with this mail was not found")

    @classmethod
    def register_user(cls,email:str,password:str)->bool:
        # this if block check weather email is for valid format or not 
        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError("The email doesn't have right format")

        # now to check weather user is already exists or not use try except method
        try:
            user = cls.find_by_email(email) # if user is in DB throw and error 
            raise UserErrors.UserAlreadyRegisteredError("the email you registered already exists")
        except UserErrors.UserNotFoundError: # if user not in DB find_by_email throw UserNotFound Error and this except block will run 
            User(email=email,password=password).save()
        
        return True 


    def json(self)->Dict:
        return {
            '_id':self._id,
            'email':self.email,
            'password':self.password 
        }


