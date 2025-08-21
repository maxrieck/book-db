from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .extensions import db, ma
from .models import Book, Publisher, Category
from marshmallow import post_load, fields


# Schema --- validates the model and converts the modal into JSON

class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True
    id = ma.auto_field()
    title = ma.auto_field(required=True)
    author = ma.auto_field()
    pages = ma.auto_field(required=True)
    publisher_id = ma.auto_field(required=True)
    publisher = ma.Nested("PublisherSchema", only=("id","name"))
    # Nesting allows this to be automatically added to publisher when created
    categories = ma.Nested("CategorySchema", many=True, exclude=("books",))
    category_ids = fields.List(fields.Integer(), load_only=True)

    @post_load
    def load_categories(self, data, **kwargs):
            if "category_ids" in data:
                data["categories"] = db.session.query(Category).filter(Category.id.in_(data["category_ids"])).all()
            return data

class PublisherSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Publisher
        load_instance = True
    id = ma.auto_field()
    name = ma.auto_field()
    books = ma.Nested("BookSchema", many=True, exclude = ("publisher",)) 


class CategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        load_instance = True
    id = ma.auto_field()
    name = ma.auto_field(required=True)
    books = ma.Nested("BookSchema", many=True, exclude=("categories",))



book_schema = BookSchema(session=db.session)
books_schema = BookSchema(many=True, session=db.session)

publisher_schema = PublisherSchema(session=db.session)
publishers_schema = PublisherSchema(many=True, session=db.session)

category_schema = CategorySchema(session=db.session)
categorys_schema = CategorySchema(many=True, session=db.session)

