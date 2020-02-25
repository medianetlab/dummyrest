# -*- coding: utf-8 -*-
"""
Module that creates the dummy REST API
"""

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class DummyApi(Resource):
    """
    Class that creates the resources for the Dummy REST API
    """
    def get(self):
        """
        GET Method Function
        """
        return "Dummy REST API"

    def post(self):
        """
        POST Method Function
        """
        return request.json


api.add_resource(DummyApi, '/api')

if __name__ == '__main__':
    app.run(debug=True)
