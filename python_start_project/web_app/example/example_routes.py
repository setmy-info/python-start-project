from flask import Flask

from python_start_project.web_app.flask_application import FlaskApplication

PATH = "example"


def add_example_routes(flask: Flask, flask_application: FlaskApplication):
    # http://localhost:5000/examnple
    # http://localhost:5000/examnple/
    def index():
        return "Hello World from example index"

    @flask.route(flask_application.get_path(path("")))
    def idx():
        return index()


def path(base_path):
    return PATH + "/" + base_path
