from flask import Blueprint, request, jsonify
from ..models import Category, db
from ..schemas import category_schema, categorys_schema


category_bp = Blueprint("categories", __name__)

@category_bp.route("", methods=["POST"])
def create_category():
    data = request.json
    name = data.get("name")
    new_category = Category (name=name)
    db.session.add(new_category)
    db.session.commit()
    return category_schema.dumps(new_category)
