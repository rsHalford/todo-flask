#from flask import Response, request
#from functools import wraps
#from api_access import USERNAME, PASSWORD
#
#def check_auth(username, password):
#    return username == USERNAME and password == PASSWORD
#
#def requires_auth(f):
#    @wraps(f)
#    def wrapper(*args, **kwargs):
#        auth = request.authorization
#        if not auth.username or not auth.password or not check_auth(auth.username, auth.password):
#            return Response('Login', 401, {'WWW-Authenticate': 'Basic realm="Login"'})
#        return f(*args, **kwargs)
#    return wrapper
