import uuid

from flask_sqlalchemy import sqlalchemy

from dummyrest.db import db


class BookModel(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Text, primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    price = db.Column(db.Float(precision=2), nullable=False)

    author_name = db.Column(db.String(50), db.ForeignKey("authors.name"))
    author = db.relationship("AuthorModel")
    # reviews = None

    def __init__(self, title, author, price):
        self.id = str(uuid.uuid4())
        self.title = title
        self.author_name = author
        self.price = price

    def json(self):
        data = {
            "title": self.title,
            "author": self.author_name,
            # "reviews": self.reviews,
            "price": self.price,
        }
        return data

    def __str__(self):
        data_json = self.json()
        return str(data_json)

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def store_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
            return 0
        except sqlalchemy.exc.IntegrityError:
            return 1

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def update_book(self, author, price, title=None):
        if title:
            self.title = title
        self.price = price
        self.author_name = author
        return self.store_to_db()


class BookModelList:
    @classmethod
    def get_list(cls):
        book_list = BookModel.query.all()
        return [book.json() for book in book_list]
