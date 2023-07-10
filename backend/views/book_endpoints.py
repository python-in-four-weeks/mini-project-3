from flask import Blueprint, request, jsonify, abort
from ..config.sqlalchemy import db
from ..models.book import Book

book_endpoints = Blueprint("book_endpoints", __name__, url_prefix="/books")


@book_endpoints.get("/")
def view_books():
    query = db.session.query(Book)
    search = request.args.get("search")
    if search:
        pattern = f"%{search}%"
        query = query.filter(Book.title.like(pattern) | (Book.author.like(pattern)))
    matching_books = query.all()
    return jsonify(matching_books)


@book_endpoints.get("/<int:id>")
def view_book(id):
    matching_book = db.session.query(Book).filter_by(id=id).first_or_404()
    return jsonify(matching_book)


@book_endpoints.post("/")
def add_book():
    if not (
        request.json.get("title")
        and request.json.get("author")
        and request.json.get("description")
    ):
        abort(400)
    new_book = Book(
        request.json.get("title"),
        request.json.get("author"),
        request.json.get("description"),
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book)


@book_endpoints.put("/<int:id>")
def update_book(id):
    matching_book = db.session.query(Book).filter_by(id=id).first_or_404()
    if not (
        request.json.get("title")
        and request.json.get("author")
        and request.json.get("description")
    ):
        abort(400)
    matching_book.title = request.json.get("title")
    matching_book.author = request.json.get("author")
    matching_book.description = request.json.get("description")
    db.session.commit()
    return jsonify(matching_book)


@book_endpoints.delete("/<int:id>")
def delete_book(id):
    matching_book = db.session.query(Book).filter_by(id=id).first_or_404()
    db.session.delete(matching_book)
    db.session.commit()
    return jsonify(matching_book)
