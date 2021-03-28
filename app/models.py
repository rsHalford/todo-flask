from app import app, db
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema


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
