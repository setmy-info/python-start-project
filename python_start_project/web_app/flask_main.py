from flask import Flask, render_template, send_from_directory, request, jsonify

from python_start_project.web_app.flask_application import FlaskApplication


def main(flask_application: FlaskApplication):
    flask = Flask(
        flask_application.application.name,
        template_folder="python_start_project/web_app/templates",
        static_folder="python_start_project/web_app/static",
        static_url_path=''
    )

    add_routes(flask, flask_application)

    flask.run(
        host=flask_application.get_host(),
        port=flask_application.get_port()
    )
    return 0


def add_routes(flask: Flask, flask_application: FlaskApplication):
    def index():
        return "Hello World from Index"

    @flask.route(flask_application.get_path("/"))
    def idx():
        return index()

    # http://localhost:5000/ImreTabur
    @flask.route(flask_application.get_path('/<name>'))
    def hello_name(name):
        return "Hello {}!".format(name)

    # http://localhost:5000/template/
    # http://localhost:5000/template/index
    @flask.route('/template/')
    @flask.route('/template/index')
    def templates():
        user_data = {'firstName': 'Imre'}
        return render_template('index.html', title='Microservice', data=user_data)

    # http://localhost:5000/static/another
    @flask.route('/static/<path:path>')
    def static_content(path):
        try:
            return send_from_directory(flask.static_folder, path + '/' + 'index.html')
        except FileNotFoundError as e:
            raise e

    # http://localhost:5000/post
    # Content for POST method {"firstName": "Imre"}
    # Content-Type: application/json and Accept: application/json
    @flask.route('/post', methods=['POST'])
    def post():
        content = request.get_json()
        print(content)
        return jsonify(content)
