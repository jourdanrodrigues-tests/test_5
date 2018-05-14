from flask_sqlalchemy import SQLAlchemy, BaseQuery


class Query(BaseQuery):
    def exists(self, **kwargs):
        return self.filter_by(**kwargs).first() is not None


db = SQLAlchemy(query_class=Query, session_options={'autoflush': False})


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column('id', db.Integer, primary_key=True)
    time = db.Column('time', db.Integer, unique=False, nullable=False)
    content = db.Column('content', db.Text(), unique=False, nullable=True)
    author = db.Column('author', db.String(20), unique=False, nullable=False)

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.id)

    @staticmethod
    def __commit(commit):
        if commit:
            db.session.commit()

    def save(self, commit=True):
        db.session.add(self)
        self.__commit(commit)

    def delete(self, commit=True):
        db.session.delete(self)
        self.__commit(commit)
