from typing import List

from .db import db
from .exceptions import ProgrammingError
from .models import Comment, Story


class BaseSerializer:
    _fields_map = {}

    @property
    def _fields(self):
        raise NotImplemented('"_fields" not set in "{}"'.format(self.__class__.__name__))

    @property
    def _model(self):
        raise NotImplemented('"_model" not set in "{}"'.format(self.__class__.__name__))

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

    def get_instance(self):
        if self.data is None:
            raise ProgrammingError(
                '"get_instance" requires "data" to be set on "{}" instantiation'.format(self.__class__.__name__)
            )
        data = {}

        for key, value in self.data.items():
            _key = self._fields_map.get(key, key)
            if _key in self._fields:
                data[_key] = value

        return self._model(**data)


class StorySerializer(BaseSerializer):
    _fields = ['id', 'url', 'title', 'points', 'author', 'content', 'time']
    _fields_map = {
        'by': 'author',
        'text': 'content',
        'score': 'points',
    }
    _model = Story


class CommentSerializer(BaseSerializer):
    _fields = ['id', 'content', 'author', 'dead', 'deleted', 'parent_id', 'time']
    _model = Comment


# For convenience

Story.serializer_class = StorySerializer
Comment.serializer_class = CommentSerializer
