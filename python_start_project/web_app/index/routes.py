from flask import Flask

from python_start_project.web_app.flask_application import FlaskApplication

PATH = ""


def add_index_routes(flask: Flask, flask_application: FlaskApplication):
    def index():
        return "Hello World from Index"

    @flask.route(flask_application.get_path(PATH))
    def idx():
        return index()
