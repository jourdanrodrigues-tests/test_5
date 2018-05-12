from db import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer, unique=False, nullable=False)
    author = db.Column('Author', db.String(20), unique=False, nullable=False)

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.id)


class Story(BaseModel):
    __tablename__ = 'story'

    url = db.Column('URL', db.String(200), unique=False, nullable=False)
    title = db.Column('Title', db.String(200), unique=True, nullable=False)
    points = db.Column('Points', db.Integer, unique=False, nullable=False)


class Comment(BaseModel):
    __tablename__ = 'comment'

    content = db.Column('Content', db.Text(), unique=False, nullable=True)
    dead = db.Column('Dead', db.Boolean(), unique=False, nullable=False, default=False)
    deleted = db.Column('Deleted', db.Boolean(), unique=False, nullable=False, default=False)

    # Not an explicit foreign key because it can come from both models
    parent_id = db.Column('Parent ID', db.Integer, unique=False, nullable=False)
