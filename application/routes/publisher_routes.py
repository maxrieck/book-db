from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from ..extensions import db
from ..models import Publisher
from ..schemas import publisher_schema, publishers_schema, books_schema



publisher_bp = Blueprint("publisher", __name__)


# Publisher routes

@publisher_bp.route("", methods=["POST"])
def create_publisher():
    try:
        data = request.json
        new_publisher = publisher_schema.load(data)
        db.session.add(new_publisher)
        db.session.commit()
        return jsonify(publisher_schema.dump(new_publisher)), 201
    except ValidationError as err:
        return {"errors": err.messages}, 400
    except Exception as e:
        return {"error": str(e)}, 500

@publisher_bp.route("", methods=["GET"])
def get_publishers():
    publishers = Publisher.query.all()
    return jsonify(publishers_schema.dump(publishers))


@publisher_bp.route("<int:id>", methods=["GET"])
def get_publisher(id):
    publisher = Publisher.query.get_or_404(id)
    return jsonify(publisher_schema.dump(publisher))


# Getting books from specific publisher
@publisher_bp.route("<int:publisher_id>/books", methods=["GET"])
def get_books_by_publisher(publisher_id):
    publisher = Publisher.query.get_or_404(publisher_id)
    books = publisher.books

    return jsonify(books_schema.dump(books))


@publisher_bp.route("<int:id>", methods=["PUT"])
def update_publisher(id):
    publisher = Publisher.query.get_or_404(id)
    data = request.json
    publisher.name = data.get("name", publisher.name)
    
    db.session.commit()
    return jsonify(publisher_schema.dump(publisher))

@publisher_bp.route("<int:id>", methods=["DELETE"])
def delete_publisher(id):
    publisher = Publisher.query.get_or_404(id)
    db.session.delete(publisher)
    db.session.commit()
    return {"message": "Publisher deleted successfully"}, 200
