from flask import Flask
from waitress import serve

from python_start_project.web_app.flask_application import FlaskApplication
from python_start_project.web_app.flask_routes import add_routes


def main(flask_application: FlaskApplication):
    flask = Flask(
        flask_application.application.name,
        template_folder="python_start_project/web_app/www/templates",
        static_folder="python_start_project/web_app/www/static",
        static_url_path=''
    )

    add_routes(flask, flask_application)

    server_type = flask_application.get_server_type()
    if server_type == "waitress":
        serve(
            flask,
            host=flask_application.get_host(),
            port=flask_application.get_port()
        )
    elif server_type == "werkzeug":
        flask.run(
            host=flask_application.get_host(),
            port=flask_application.get_port()
        )
    return 0
