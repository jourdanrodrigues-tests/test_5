import json
import os

from flask import Blueprint
from redis import StrictRedis

from .utils import HackerNewsClient, Response

blueprint = Blueprint('views', __name__)

redis_client = StrictRedis.from_url(os.getenv('REDIS_URL'))

hn_client = HackerNewsClient()


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


@blueprint.route('/api/stories/', methods=['GET'])
def stories():
    story_list = _get_clean_item_list(hn_client('/topstories')[:10])
    return Response(story_list).ok()


@blueprint.route('/api/comments/<int:item_id>/', methods=['GET'])
def comments(item_id):
    item = _get_item(item_id)

    no_item_or_no_comments = not item or not bool(item.get('kids', []))
    if no_item_or_no_comments:
        return Response('Not found').not_found()

    _comments = _get_clean_item_list(item['kids'])

    return Response(_comments).ok()
