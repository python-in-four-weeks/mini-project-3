from marshmallow import fields
from ..config.marshmallow import marshmallow
from .loan_schema import LoanSchema


class BookSchema(marshmallow.Schema):
    id = fields.Int()
    title = fields.Str()
    author = fields.Str()
    description = fields.Str()

    loans = fields.Nested(LoanSchema(many=True), exclude=("book",))
