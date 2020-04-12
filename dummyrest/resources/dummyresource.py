# -*- coding: utf-8 -*-
"""
Module that creates the dummy REST API
"""

from flask import request
from flask_restful import Resource


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
