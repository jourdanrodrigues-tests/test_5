import json
import os
from typing import List

from flask import Blueprint
from redis import StrictRedis

from .db import db
from .models import Story, Comment
from .serializers import StorySerializer, CommentSerializer
from .utils import HackerNews, Response

STORIES_LENGTH = 10

blueprint = Blueprint('views', __name__)

redis_client = StrictRedis.from_url(os.getenv('REDIS_URL'))

hn_client = HackerNews()


def _get_stories_ids():
    stories_ids = redis_client.get('stories_ids')
    if stories_ids:
        stories_ids = json.loads(stories_ids)
    else:
        stories_ids = hn_client('/topstories')
        redis_client.set('stories_ids', json.dumps(stories_ids), ex=10)
    return stories_ids


def _get_comments_from_item(item_id: int) -> List[int]:
    item_id_str = str(item_id)
    comment = redis_client.hget('comments', item_id_str)
    if comment:
        comment = json.loads(comment)
    else:
        comment = hn_client.get_item(item_id)
        redis_client.hset('comments', item_id_str, json.dumps(comment))
        redis_client.expire(name='comments', time=20)
    return comment.pop('kids', [])


@blueprint.route('/api/stories/', methods=['GET'])
def stories():
    stories_ids = _get_stories_ids()

    stories_query = Story.query.filter(Story.id.in_(stories_ids[:STORIES_LENGTH]))
    if stories_query.count() == STORIES_LENGTH:
        data = StorySerializer(stories_query.all()).get_data()
        return Response(data).ok()

    data = []
    i = 0
    while len(data) < STORIES_LENGTH:
        try:
            story, _ = Story.query.get_or_fetch(stories_ids[i], commit=False)
        except HackerNews.WrongItemType:
            pass
        else:
            data.append(StorySerializer(story).get_data())
        finally:
            i += 1

    db.session.commit()

    return Response(data).ok()


@blueprint.route('/api/comments/<int:item_id>/', methods=['GET'])
def comments(item_id):
    comments_ids = _get_comments_from_item(item_id)

    if not comments_ids:
        return Response([]).ok()

    comments_query = Comment.query.filter(Comment.id.in_(comments_ids))
    if comments_query.count() == len(comments_ids):
        data = CommentSerializer(comments_query.all()).get_data()
        return Response(data).ok()

    data = []
    for comment_id in comments_ids:
        try:
            comment, _ = Comment.query.get_or_fetch(comment_id, commit=False)
        except HackerNews.Error:
            pass
        else:
            data.append(CommentSerializer(comment).get_data())

    db.session.commit()

    return Response(data).ok()
