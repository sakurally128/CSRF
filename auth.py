from functools import wraps
from flask import session,redirect,url_for

def login_request(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        user = session.get("user_id")
        if user:
            return func(*args,**kwargs)
        else:
            return redirect(url_for("login"))
    return wrapper
