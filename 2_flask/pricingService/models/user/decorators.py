import functools
from typing import Callable 
from flask import redirect , session, url_for, flash, session , current_app

def requires_login(f:Callable)-> Callable:
    # @functools.wraps(f)  this deco. will help decorated_function to have replaced function documentation
    def wrapper_function(*args,**kwargs): # this will help to give arguments to actual function
        if not session.get('email'): # you have to login to access further 
            flash("You need to be signed in for this page.","danger")
            return redirect(url_for('users.login_user'))
        return f(*args,**kwargs) # actual function which is doing work

    # Renaming the function name:
    wrapper_function.__name__ = f.__name__
    return wrapper_function



def requires_admin(f:callable)->Callable:
    # @functools.wraps(f)
    def wrapper_function(*args,**kwargs):
        if session.get('email')!=current_app.config.get("ADMIN",""): # if session email is not equal to the ADMIN key's value in currently loaded app
            flash("You need to be ADMIN to access this page")
            return redirect(url_for("users.login_user"))
        return f(*args,**kwargs)

    wrapper_function.__name__=f.__name__
    return wrapper_function