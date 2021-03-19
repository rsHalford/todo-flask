from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))


@app.route('/')
def index():
    todo_list = Todo.query.all()
    response = make_response(render_template('test.html', todo_list=todo_list))
    response.mimetype = 'text/plain'
    return response

@app.route('/a', methods=['POST'])
def add():
    title = request.form.get('title')
    new_todo = Todo(title=title)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/d/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
