from flask import Response, request
from functools import wraps
from api_access import ACCESS_TOKEN

def check_auth(access_token):
    return access_token == ACCESS_TOKEN

def requires_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = request.authorization
        if not auth.access_token or not check_auth(auth.access_token):
            return Response('Login', 401, {'WWW-Authenticate': 'Basic realm="Login"'})
        return f(*args, **kwargs)
    return wrapper
