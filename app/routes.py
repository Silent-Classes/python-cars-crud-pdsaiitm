from flask import jsonify, request

cars = []


def register_routes(app):

    @app.route('/')
    def home():
        return 'hello'

    # create crud routes here, use in memory list to store the items
