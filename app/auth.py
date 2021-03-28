from flask import request
from functools import wraps
from api_access import USERNAME, PASSWORD

def check_auth(username, password):
    return username == USERNAME and password == PASSWORD

def authenticate():
    message: {'message': 'Authenticate.'}
    resp = jsonify(message)
    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'
    return resp

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return authenticate()
        elif not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated
