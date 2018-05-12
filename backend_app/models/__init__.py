from ..db import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column('id', db.Integer, primary_key=True)
    time = db.Column('time', db.Integer, unique=False, nullable=False)
    author = db.Column('author', db.String(20), unique=False, nullable=False)

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.id)


class Story(BaseModel):
    __tablename__ = 'story'

    url = db.Column('url', db.String(200), unique=False, nullable=False)
    title = db.Column('title', db.String(200), unique=True, nullable=False)
    points = db.Column('points', db.Integer, unique=False, nullable=False)


class Comment(BaseModel):
    __tablename__ = 'comment'

    content = db.Column('content', db.Text(), unique=False, nullable=True)
    dead = db.Column('dead', db.Boolean(), unique=False, nullable=False, default=False)
    deleted = db.Column('deleted', db.Boolean(), unique=False, nullable=False, default=False)

    # Not an explicit foreign key because it can come from both models
    parent_id = db.Column('parent_id', db.Integer, unique=False, nullable=False)
