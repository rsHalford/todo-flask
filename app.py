from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from functools import wraps


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10))
    body = db.Column(db.String(100))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, title, body):
        self.title = title
        self.body = body

    def __repr__(self):
        return f"{self.id}"


class TodoSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Todo
        sqla_session = db.session
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    body = fields.String(required=True)


def check_auth(username, password):
    return username == 'admin' and password == 'secret'

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


@app.route('/api/v1/todo', methods=['POST'])
@requires_auth
def create_todo():
    data = request.get_json()
    todo_schema = TodoSchema()
    todo = todo_schema.load(data)
    result = todo_schema.dump(todo.create())
    return make_response(jsonify({'todo': result}), 200)

@app.route('/api/v1/todo', methods=['GET'])
@requires_auth
def get_all_todos():
    get_todos = Todo.query.all()
    todo_schema = TodoSchema(many=True)
    todos = todo_schema.dump(get_todos)
    return make_response(jsonify({'todos': todos}))

@app.route('/api/v1/todo/<id>', methods=['GET'])
@requires_auth
def get_todo_by_id(id):
    get_todo = Todo.query.get(id)
    todo_schema = TodoSchema()
    todo = todo_schema.dump(get_todo)
    return make_response(jsonify({'todo': todo}))

@app.route('/api/v1/todo/<id>', methods=['PUT'])
@requires_auth
def update_todo_by_id(id):
    data = request.get_json()
    get_todo = Todo.query.get(id)
    if data.get('title'):
        get_todo.title = data['title']
    if data.get('body'):
        get_todo.body = data['body']
    db.session.add(get_todo)
    db.session.commit()
    todo_schema = TodoSchema(only=['id', 'title', 'body'])
    todo = todo_schema.dump(get_todo)
    return make_response(jsonify({'todo': todo}))

@app.route('/api/v1/todo/<id>', methods=['DELETE'])
@requires_auth
def delete_todo_by_id(id):
    get_todo = Todo.query.get(id)
    db.session.delete(get_todo)
    db.session.commit()
    return make_response('', 204)
        




@app.route('/')
def about():
    response = make_response(render_template('about.html'))
    response.mimetype = 'text/plain'
    return response


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
