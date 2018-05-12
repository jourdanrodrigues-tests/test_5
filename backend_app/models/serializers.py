from db import db
from exceptions import ProgrammingError


class BaseSerializer:
    @property
    def _fields(self):
        raise NotImplemented('"_fields" not set in "{}"'.format(self.__class__.__name__))

    def __init__(self, data: dict = None, instance: db.Model = None):
        self.data = data
        self.instance = instance

    def __getattribute__(self, item):
        if item == 'get_data' and self.instance is None:
            raise ProgrammingError(
                '"get_data" requires "instance" to be set on "{}" instantiation'.format(self.__class__.__name__)
            )


class StorySerializer(BaseSerializer):
    _fields = ['id', 'url', 'title', 'points', 'author']

    def get_data(self):
        return {field: getattr(self.instance, field) for field in self._fields}


class CommentSerializer(BaseSerializer):
    _fields = ['id', 'content', 'author', 'dead', 'deleted', 'parent_id']

    def get_data(self):
        if not self.instance:
            raise ProgrammingError('Serializer must be instantiated with "instance" parameter')

        return {field: getattr(self.instance, field) for field in self._fields}
