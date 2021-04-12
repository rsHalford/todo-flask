from flask import make_response, request
from functools import wraps
from api_access import USERNAME, PASSWORD

def requires_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == USERNAME and auth.password == PASSWORD:
            return f(*args, **kwargs)
        return make_response('Unauthorized Access', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
    return wrapper
