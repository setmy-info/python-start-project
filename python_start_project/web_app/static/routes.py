from flask import Flask, send_from_directory

from python_start_project.web_app.flask_application import FlaskApplication

PATH = "static"


def add_static_routes(flask: Flask, flask_application: FlaskApplication):
    @flask.route('/static')
    def static_content_index():
        try:
            return send_from_directory(flask.static_folder, 'index.html')
        except FileNotFoundError as e:
            raise e

    # http://localhost:5000/static/another
    @flask.route('/static/<path:path>')
    def static_content(path):
        try:
            return send_from_directory(flask.static_folder, path + '/' + 'index.html')
        except FileNotFoundError as e:
            raise e


def path(base_path):
    return PATH + "/" + base_path
