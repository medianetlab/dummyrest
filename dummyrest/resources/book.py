from flask_restful import Resource, reqparse
from dummyrest.models.book import BookModel, BookModelList


class BookApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "title", type=str, required=False, default=None, help="Please define the title of the book"
    )
    parser.add_argument("price", type=float, required=True, help="Please define price of the book")
    parser.add_argument("author", type=str, required=True, help="Please define author of the book")

    def get(self, title):
        """
        Find a book from the database and return it
        """
        book = BookModel.find_by_title(title)
        return (book.json(), 200) if book else ("Book not found", 404)

    def post(self, title):
        """
        Create a new book object and insert it into the database
        """
        # if BookModel.find_by_title(title):
        #     return f"Book {title} already exists", 400
        data = self.parser.parse_args()
        data["title"] = title
        new_book = BookModel(**data)
        store = new_book.store_to_db()
        return (f"Added book {title}", 201) if not store else (f"Book {title} already exists", 400)

    def put(self, title):
        """
        Update a book or create it if it doesn't exists
        """
        data = self.parser.parse_args()

        book = BookModel.find_by_title(title)
        if not book:
            data["title"] = title
            new_book = BookModel(**data)
            store = new_book.store_to_db()
            return (
                (f"Added book {title}", 201) if not store else (f"Book {title} already exists", 400)
            )
        else:
            update = book.update_book(**data)
            return (
                (f"Updated {title}", 200)
                if not update
                else (f"Book {data['title']} already exists", 400)
            )

    def delete(self, title):
        """
        Delete a book from the database
        """
        book = BookModel.find_by_title(title)
        if not book:
            return f"Book {title} was not found", 404

        book.delete_from_db()
        return f"Book {title} succesfully deleted", 200


class BookListApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "title", type=str, required=True, help="Please define the title of the book"
    )
    parser.add_argument("price", type=float, required=True, help="Please define price of the book")
    parser.add_argument("author", type=str, required=True, help="Please define author of the book")

    def get(self):
        """
        Returns a list with all the stored books
        """
        return BookModelList.get_list(), 200

    def post(self):
        """
        Create a new book object and insert it into the database
        """
        data = self.parser.parse_args()
        new_book = BookModel(**data)
        store = new_book.store_to_db()
        return (
            (f"Added book {data['title']}", 201)
            if not store
            else (f"Book {data['title']} already exists", 400)
        )
