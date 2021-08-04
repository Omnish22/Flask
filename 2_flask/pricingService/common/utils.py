import re 
from passlib.hash import pbkdf2_sha256
from werkzeug.security import generate_password_hash, check_password_hash


class Utils:
    @staticmethod
    def email_is_valid(email:str)->bool:
        email_matcher = re.compile(r'^[\w-]+@([\w-]+\.)+[\w]+$')
        return True if email_matcher.match(email) else False

    @staticmethod
    def hash_password(password:str)->str:
        return generate_password_hash(password)
    
    @staticmethod
    def check_hashed_password(password:str, hashed_password:str)->bool:
        return check_password_hash(hashed_password,password)