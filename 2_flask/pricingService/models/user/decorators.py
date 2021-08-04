import functools
from typing import Callable 
from flask import redirect , session, url_for, flash, session

def requires_login(f:Callable)-> Callable:
    # @functools.wraps(f)  this deco. will help decorated_function to have replaced function documentation
    def decorated_function(*args,**kwargs): # this will help to give arguments to actual function
        if not session.get('email'): # you have to login to access further 
            flash("You need to be signed in for this page.","danger")
            return redirect(url_for('users.login_user'))
        return f(*args,**kwargs) # actual function which is doing work
        
    # Renaming the function name:
    decorated_function.__name__ = f.__name__
    return decorated_function