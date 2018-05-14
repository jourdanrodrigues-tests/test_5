import json
import os

from flask import Blueprint
from redis import StrictRedis

from .db import db
from .models import Story
from .serializers import StorySerializer
from .utils import HackerNews, Response

STORIES_LENGTH = 10

blueprint = Blueprint('views', __name__)

redis_client = StrictRedis.from_url(os.getenv('REDIS_URL'))

hn_client = HackerNews()


def _get_item(item_id):
    str_item_id = str(item_id)
    item = redis_client.get(str_item_id)
    if item:
        return json.loads(item)
    else:
        item = hn_client.get_item(item_id)

        if item is None:
            return

        del item['type']  # We don't need it

        redis_client.set(str_item_id, json.dumps(item))

        return item


def _get_clean_item_list(item_list: list) -> list:
    _item_list = []

    for item_id in item_list:
        item = _get_item(item_id)
        item.pop('kids', None)
        _item_list.append(item)

    return _item_list


def _get_stories_ids():
    stories_ids = redis_client.get('stories_ids')
    if stories_ids:
        stories_ids = json.loads(stories_ids)
    else:
        stories_ids = hn_client('/topstories')
        redis_client.set('stories_ids', json.dumps(stories_ids), ex=10)
    return stories_ids


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
            i += 1
            continue

        story_data = StorySerializer(story).get_data()

        data.append(story_data)
        i += 1

    db.session.commit()

    return Response(data).ok()


@blueprint.route('/api/comments/<int:item_id>/', methods=['GET'])
def comments(item_id):
    item = _get_item(item_id)

    no_item_or_no_comments = not item or not bool(item.get('kids', []))
    if no_item_or_no_comments:
        return Response('Not found').not_found()

    _comments = _get_clean_item_list(item['kids'])

    return Response(_comments).ok()
