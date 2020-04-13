from flask_restful import Resource, reqparse
from dummyrest.models.author import AuthorListModel, AuthorModel


class AuthorApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "name", type=str, required=False, default=None, help="Define the name of the author"
    )
    parser.add_argument("nationality", type=str, required=False, default="Unknown")

    def get(self, name):
        """
        Return a author by name
        """
        author = AuthorModel.find_by_name(name)
        return (author.json(), 200) if author else (f"Author {name} was not found", 404)

    def post(self, name):
        """
        Add a new author
        """
        data = self.parser.parse_args()
        data["name"] = name
        new_author = AuthorModel(**data)
        store = new_author.store_to_db()
        return (
            (f"Added author {name}", 201) if not store else (f"Author {name} already exists", 400)
        )

    def put(self, name):
        """
        Updates or adds a new author
        """
        data = self.parser.parse_args()

        author = AuthorModel.find_by_name(name)
        if not author:
            data["name"] = name
            new_author = AuthorModel(**data)
            new_author.store_to_db()
            return f"Added author {name}", 201
        else:
            updated = author.update_author(**data)
            return (
                (f"Updated author {name}", 200)
                if not updated
                else (f"Author {data['name']} already exists", 400)
            )

    def delete(self, name):
        """
        Delete an author if exists
        """
        author = AuthorModel.find_by_name(name)
        if not author:
            return f"Author {name} doesn't exists", 404
        else:
            author.delete_from_db()
            return f"Succesfully deleted author {name}", 200


class AuthorListApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True, help="Define the name of the author")
    parser.add_argument("nationality", type=str, required=False, default="Unknown")

    def get(self):
        """
        Returns a list with all the authors
        """
        return AuthorListModel.get_list(), 200

    def post(self):
        """
        Adds a new author
        """
        data = self.parser.parse_args()
        new_author = AuthorModel(**data)
        store = new_author.store_to_db()
        return (
            (f"Added author {data['name']}", 201)
            if not store
            else (f"Author {data['name']} already exists", 400)
        )
