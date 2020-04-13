import os

from flask import Flask
from flask_restful import Api

from dummyrest.resources.dummyresource import DummyApi, DummyApiList
from dummyrest.resources.book import BookApi, BookListApi
from dummyrest.resources.author import AuthorApi, AuthorListApi

from dummyrest.db import db

# Create the app
app = Flask(__name__)
api = Api(app)

# Add the APIs
api.add_resource(DummyApiList, "/dummy")
api.add_resource(DummyApi, "/dummy/<string:_id>")
api.add_resource(BookApi, "/book/<string:title>")
api.add_resource(BookListApi, "/books")
api.add_resource(AuthorApi, "/author/<string:name>")
api.add_resource(AuthorListApi, "/authors")

# Add the database configuration
db.init_app(app)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL", "sqlite:///data.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.before_first_request
def create_tables():
    db.create_all()


# Create a Hello World route
@app.route("/")
def hello():
    return "Hello, world!", 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
