from http import HTTPStatus

import requests
from flask import jsonify


class HackerNews:
    __api = 'https://hacker-news.firebaseio.com/v0{endpoint}.json'

    def __call__(self, endpoint):
        return self.__get(endpoint)

    def __get(self, endpoint):
        return requests.get(self.__api.format(endpoint=endpoint)).json()

    def get_item(self, item_id):
        return self.__get('/item/{}'.format(item_id))

    class Error(Exception):
        pass

    class NullItem(Error):
        pass

    class DeadItem(Error):
        pass

    class DeletedItem(Error):
        pass

    class WrongItemType(Error):
        pass


class Response:
    def __init__(self, data: list or dict or str):
        self.data = data

    def ok(self):
        return jsonify({'data': self.data})

    def not_found(self):
        return jsonify({'message': self.data}), HTTPStatus.NOT_FOUND

    def bad_request(self):
        return jsonify({'message': self.data}), HTTPStatus.BAD_REQUEST
