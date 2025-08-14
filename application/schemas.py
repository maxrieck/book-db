from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .extensions import db, ma
from .models import Book, Publisher


# Schema --- validates the model and converts the modal into JSON

class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True
    id = ma.auto_field()
    title = ma.auto_field(required=True)
    author = ma.auto_field
    pages = ma.auto_field(required=True)
    publisher_id = ma.auto_field(required=True)
    publisher = ma.Nested("PublisherSchema", only=("id","name"))
    # Nesting allows this to be automatically added to publisher when created

class PublisherSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Publisher
        load_instance = True
    id = ma.auto_field()
    name = ma.auto_field()
    books = ma.Nested("BookSchema", many=True, exclude = ("publisher",)) 

book_schema = BookSchema(session=db.session)
books_schema = BookSchema(many=True, session=db.session)

publisher_schema = PublisherSchema(session=db.session)
publishers_schema = PublisherSchema(many=True, session=db.session)