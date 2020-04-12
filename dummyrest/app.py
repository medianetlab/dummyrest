from flask import Flask
from flask_restful import Api
from dummyrest.resources.dummyresource import DummyApiList, DummyApi

# Create the app
app = Flask(__name__)
api = Api(app)

# Add the APIs
api.add_resource(DummyApiList, "/dummy")
api.add_resource(DummyApi, "/dummy/<string:_id>")

if __name__ == "__main__":
    app.run(debug=True)
