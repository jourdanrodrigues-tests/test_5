from .db import BaseModel, db, Query
from .utils import HackerNews

hn_client = HackerNews()


class StoryQuery(Query):
    def get_or_fetch(self, item_id, commit=True):
        story = self.filter_by(id=item_id).scalar()
        if story:
            return story, False

        hn_story = hn_client.get_item(item_id)

        if not hn_story or hn_story['type'] != 'story':
            raise HackerNews.WrongItemType()

        story = Story(
            id=item_id,
            url=hn_story.get('url'),
            time=hn_story.get('time'),
            author=hn_story.get('by'),
            title=hn_story.get('title'),
            points=hn_story.get('score'),
            content=hn_story.get('text')
        )
        story.save(commit=commit)

        return story, True


class Story(BaseModel):
    __tablename__ = 'story'
    query_class = StoryQuery

    url = db.Column('url', db.String(200), unique=False, nullable=True)
    points = db.Column('points', db.Integer, unique=False, nullable=False)
    title = db.Column('title', db.String(200), unique=True, nullable=False)


class Comment(BaseModel):
    __tablename__ = 'comment'

    dead = db.Column('dead', db.Boolean(), unique=False, nullable=False, default=False)
    deleted = db.Column('deleted', db.Boolean(), unique=False, nullable=False, default=False)

    # Not an explicit foreign key because it can come from both models
    parent_id = db.Column('parent_id', db.Integer, unique=False, nullable=False)
