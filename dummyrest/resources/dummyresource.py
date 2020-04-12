# -*- coding: utf-8 -*-
"""
Module that creates the dummy REST API
"""

from flask import request
from flask_restful import Resource


class DummyApiList(Resource):
    """
    Class that creates the resources for the Dummy REST API
    """

    def get(self):
        """
        GET Method Function
        """
        return "Dummy REST API", 200

    def post(self):
        """
        POST Method Function
        """
        return f"Created data {request.json}", 201


class DummyApi(Resource):
    """
    Class that creates the resources for the Dummy REST API
    """

    def get(self, _id):
        """
        GET Method Function
        """
        return f"Get item {_id}", 200

    def post(self, _id):
        """
        POST Method Function
        """
        data = request.json
        data["uuid"] = _id
        return f"Created item {_id} | Data {data}", 201

    def put(self, _id):
        """
        PUT Method Function
        """
        data = request.json
        data["uuid"] = _id
        return f"Updated element {_id}. New data: {request.json}", 200

    def delete(self, _id):
        """
        DELETE Method Function
        """
        return f"Deleted item {_id}", 200
