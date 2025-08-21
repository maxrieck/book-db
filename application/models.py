from .extensions import db
from sqlalchemy import String, Integer, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship


# Models --- python classes that turn into SQL tables


# Association table for many to many with books and categories 
book_category: Table = Table(
    "book_category",
    db.metadata,
    Column("book_id", Integer, ForeignKey("book.id"), primary_key=True),
    Column("category_id", Integer, ForeignKey("category.id"), primary_key=True),
)


class Book(db.Model):
    __tablename__= "book"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    title:Mapped[str] = mapped_column(String(100), nullable=False)
    author:Mapped[str] = mapped_column(String(50))
    pages:Mapped[int] = mapped_column(Integer, nullable=False)

    publisher_id:Mapped[int] = mapped_column(Integer, ForeignKey("publisher.id"), nullable=False)
    publisher:Mapped["Publisher"] = relationship(back_populates="books")

    categories: Mapped[list["Category"]] = relationship(
    "Category", secondary=book_category, back_populates="books")

class Publisher(db.Model):
    __tablename__ = "publisher"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String(100), nullable=False)

    books:Mapped[list["Book"]] = relationship("Book", back_populates="publisher", lazy=True)


class Category(db.Model):
    __tablename__ = "category"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    books: Mapped[list["Book"]] = relationship(
    "Book", secondary=book_category, back_populates="categories")

