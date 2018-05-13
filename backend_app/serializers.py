from typing import List

from .db import db
from exceptions import ProgrammingError


class BaseSerializer:
    @property
    def _fields(self):
        raise NotImplemented('"_fields" not set in "{}"'.format(self.__class__.__name__))

    def __init__(self, instance: db.Model or List[db.Model] = None, data: dict = None):
        self.data = data
        self.instance = instance

    def _get_data(self, instance):
        if self.instance is None:
            raise ProgrammingError(
                '"get_data" requires "instance" to be set on "{}" instantiation'.format(self.__class__.__name__)
            )

        return {field: getattr(instance, field) for field in self._fields}

    def get_data(self):
        if isinstance(self.instance, list):
            return [self._get_data(instance) for instance in self.instance]
        return self._get_data(self.instance)


class StorySerializer(BaseSerializer):
    _fields = ['id', 'url', 'title', 'points', 'author']


class CommentSerializer(BaseSerializer):
    _fields = ['id', 'content', 'author', 'dead', 'deleted', 'parent_id']
