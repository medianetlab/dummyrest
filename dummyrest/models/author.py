import uuid

from flask_sqlalchemy import sqlalchemy

from dummyrest.db import db


class AuthorModel(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Text, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    nationality = db.Column(db.String(20), default="Unknown")

    books = db.relationship("BookModel")

    def __init__(self, name, nationality):
        self.id = str(uuid.uuid4())
        self.name = name
        self.nationality = nationality

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def json(self):
        data = {
            "name": self.name,
            "nationality": self.nationality,
            "books": [book.json() for book in self.books],
        }
        return data

    def __str__(self):
        data = self.json()
        return str(data)

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

    def update_author(self, nationality, name=None):
        self.nationality = nationality
        if name:
            self.name = name
        return self.store_to_db()


class AuthorListModel:
    @classmethod
    def get_list(cls):
        author_list = AuthorModel.query.all()
        return [author.json() for author in author_list]
