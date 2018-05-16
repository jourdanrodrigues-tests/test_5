from .db import BaseModel, db
from .utils import HackerNews

hn_client = HackerNews()


class Story(BaseModel):
    __tablename__ = 'story'

    url = db.Column('url', db.String(200), unique=False, nullable=True)
    points = db.Column('points', db.Integer, unique=False, nullable=False)
    title = db.Column('title', db.String(200), unique=True, nullable=False)


class Comment(BaseModel):
    __tablename__ = 'comment'

    dead = db.Column('dead', db.Boolean(), unique=False, nullable=False, default=False)
    deleted = db.Column('deleted', db.Boolean(), unique=False, nullable=False, default=False)

    # Not an explicit foreign key because it can come from both models
    parent_id = db.Column('parent_id', db.Integer, unique=False, nullable=False)
