from typing import ClassVar
from ..config.marshmallow import marshmallow


class JSONSerializableModel:
    schema: ClassVar[marshmallow.Schema]

    def __repr__(self):
        return str(iter(self))

    def __iter__(self):
        for key_value_pair in self.schema.dump(self).items():
            yield key_value_pair
