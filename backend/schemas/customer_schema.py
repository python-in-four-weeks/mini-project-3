from marshmallow import fields
from ..config.marshmallow import marshmallow
from .loan_schema import LoanSchema


class CustomerSchema(marshmallow.SQLAlchemyAutoSchema):
    library_card_number = fields.Str()
    name = fields.Str()
    email = fields.Str()

    loans = fields.Nested(LoanSchema(many=True), exclude=("customer",))
