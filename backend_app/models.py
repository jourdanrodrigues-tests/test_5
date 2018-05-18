from .db import BaseModel, db
from .utils import HackerNews

hn_client = HackerNews()


class Model(BaseModel):
    __abstract__ = True

    id = db.Column('id', db.Integer, primary_key=True)
    time = db.Column('time', db.Integer, unique=False, nullable=False)
    content = db.Column('content', db.Text(), unique=False, nullable=True)
    author = db.Column('author', db.String(20), unique=False, nullable=False)


class Story(Model):
    __tablename__ = 'story'

    url = db.Column('url', db.String(200), unique=False, nullable=True)
    points = db.Column('points', db.Integer, unique=False, nullable=False)
    title = db.Column('title', db.String(200), unique=True, nullable=False)


class Comment(Model):
    __tablename__ = 'comment'

    # Not an explicit foreign key because it can come from both models
    parent_id = db.Column('parent_id', db.Integer, unique=False, nullable=False)
