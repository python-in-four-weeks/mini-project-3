from __future__ import annotations
from typing import TYPE_CHECKING, List, ClassVar
from sqlalchemy.orm import Mapped
from ..config.sqlalchemy import db
from ..config.marshmallow import marshmallow
from ..utils.json_serializable_model import JSONSerializableModel
from ..schemas.book_schema import BookSchema

if TYPE_CHECKING:
    from .loan import Loan
else:
    Loan = "Loan"


class Book(db.Model, JSONSerializableModel):
    def __init__(self, title, author, description):
        self.title = title
        self.author = author
        self.description = description

    id: int = db.Column(db.Integer, primary_key=True)
    title: str = db.Column(db.String, nullable=False)
    author: str = db.Column(db.String, nullable=False)
    description: str = db.Column(db.String, nullable=False)

    loans: Mapped[List[Loan]] = db.relationship(
        "Loan", back_populates="book", cascade="all, delete", lazy="subquery"
    )

    schema: ClassVar[marshmallow.Schema] = BookSchema()
