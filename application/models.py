from .extensions import db
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


# Models --- python classes that turn into SQL tables

class Book(db.Model):
    __tablename__= "book"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    title:Mapped[str] = mapped_column(String(100), nullable=False)
    author:Mapped[str] = mapped_column(String(50))
    pages:Mapped[int] = mapped_column(Integer, nullable=False)

    publisher_id:Mapped[int] = mapped_column(Integer, ForeignKey("publisher.id"), nullable=False)
    publisher:Mapped["Publisher"] = relationship(back_populates="books")

class Publisher(db.Model):
    __tablename__ = "publisher"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String(100), nullable=False)

    books:Mapped[list["Book"]] = relationship("Book", back_populates="publisher", lazy=True)
