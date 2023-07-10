from __future__ import annotations
from typing import ClassVar
from sqlalchemy.orm import Mapped
from datetime import date, timedelta
from ..config.sqlalchemy import db
from ..config.marshmallow import marshmallow
from ..utils.json_serializable_model import JSONSerializableModel
from ..schemas.loan_schema import LoanSchema
from .book import Book
from .customer import Customer


class Loan(db.Model, JSONSerializableModel):
    def __init__(
        self,
        book_id,
        customer_library_card_number,
        date_loaned=None,
        date_due=None,
        date_returned=None,
    ):
        if date_loaned:
            self.date_loaned = date_loaned
        else:
            self.date_loaned = date.today()
        if date_due:
            self.date_due = date_due
        else:
            self.date_due = date.today() + timedelta(weeks=2)
        if date_returned:
            self.date_returned = date_returned
        else:
            self.date_returned = None
        self.book_id = book_id
        self.customer_library_card_number = customer_library_card_number

    id: int = db.Column(db.Integer, primary_key=True)

    book_id: int = db.Column(db.Integer, db.ForeignKey(Book.id), nullable=None)
    book: Mapped[Book] = db.relationship(
        "Book", back_populates="loans", lazy="subquery"
    )

    customer_library_card_number: str = db.Column(
        db.String, db.ForeignKey(Customer.library_card_number), nullable=False
    )
    customer: Mapped[Customer] = db.relationship(
        "Customer", back_populates="loans", lazy="subquery"
    )

    date_loaned: date = db.Column(db.Date, nullable=False)
    date_due: date = db.Column(db.Date, nullable=False)
    date_returned: date | None = db.Column(db.Date, nullable=True)

    schema: ClassVar[marshmallow.Schema] = LoanSchema()
