from flask.json.provider import JSONProvider
from json import JSONEncoder, dumps, loads
from .json_serializable_model import JSONSerializableModel


class CustomJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, JSONSerializableModel):
            try:
                return dict(obj)
            except TypeError:
                return super().default(obj)
        else:
            return super().default(obj)


class CustomJsonProvider(JSONProvider):
    def dumps(self, obj, **kwargs):
        return dumps(obj, **kwargs, cls=CustomJsonEncoder)

    def loads(self, s: str | bytes, **kwargs):
        return loads(s, **kwargs)
