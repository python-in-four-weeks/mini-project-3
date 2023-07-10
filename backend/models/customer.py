from __future__ import annotations
from typing import TYPE_CHECKING, List, ClassVar
from sqlalchemy.orm import Mapped
from ..config.sqlalchemy import db
from ..config.marshmallow import marshmallow
from ..utils.json_serializable_model import JSONSerializableModel
from ..schemas.customer_schema import CustomerSchema
from ..utils.library_card_number_generator import generate_library_card_number

if TYPE_CHECKING:
    from .loan import Loan
else:
    Loan = "Loan"


class Customer(db.Model, JSONSerializableModel):
    def __init__(self, name, email, library_card_number=None):
        if library_card_number:
            self.library_card_number = library_card_number
        else:
            self.library_card_number = generate_library_card_number(name)
        self.name = name
        self.email = email

    library_card_number: str = db.Column(db.String, primary_key=True)
    name: str = db.Column(db.String, nullable=False)
    email: str = db.Column(db.String, nullable=False, unique=True)

    loans: Mapped[List[Loan]] = db.relationship(
        "Loan", back_populates="customer", cascade="all, delete", lazy="subquery"
    )

    schema: ClassVar[marshmallow.Schema] = CustomerSchema()
