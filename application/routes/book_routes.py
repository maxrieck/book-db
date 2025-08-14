from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from ..extensions import db
from ..models import Book
from ..schemas import book_schema, books_schema


book_bp = Blueprint("book", __name__)


# Book routes

@book_bp.route("", methods=["POST"])
def create_book():
    try:
        book = book_schema.load(request.json)
        db.session.add(book)
        db.session.commit()
        return jsonify(book_schema.dump(book)), 201
    except ValidationError as err:
        return {"errors": err.messages}, 400
    except Exception as e:
        return {"error": str(e)}, 500
    


@book_bp.route("", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify(books_schema.dump(books))



@book_bp.route("<int:id>", methods=["GET"])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book_schema.dump(book))



@book_bp.route("<int:id>", methods=["PUT"])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.json
    book.title = data.get("title", book.title)
    book.author = data.get("author", book.author)
    book.pages = data.get("pages", book.pages)
    db.session.commit()
    return jsonify(book_schema.dump(book))



@book_bp.route("<int:id>", methods=["DELETE"])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return {"message": "Book deleted successfully"}, 200
