from marshmallow import fields
from ..config.marshmallow import marshmallow


class LoanSchema(marshmallow.SQLAlchemyAutoSchema):
    id = fields.Int()

    book_id = fields.Int()
    book = fields.Nested("BookSchema", exclude=("loans",))

    customer_library_card_number = fields.Str()
    customer = fields.Nested("CustomerSchema", exclude=("loans",))

    date_loaned = fields.Date()
    date_due = fields.Date()
    date_returned = fields.Date()
