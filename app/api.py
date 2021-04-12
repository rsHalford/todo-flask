from app import app, db
from flask import request, make_response, jsonify
from app.models import Todo, TodoSchema
from app.auth import requires_auth


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
