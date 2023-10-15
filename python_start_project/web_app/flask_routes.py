from flask import Flask

from python_start_project.web_app.example.routes import add_example_routes
from python_start_project.web_app.flask_application import FlaskApplication
from python_start_project.web_app.index.routes import add_index_routes
from python_start_project.web_app.static.routes import add_static_routes


def add_routes(flask: Flask, flask_application: FlaskApplication):
    add_index_routes(flask, flask_application)
    add_static_routes(flask, flask_application)
    add_example_routes(flask, flask_application)
