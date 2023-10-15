from flask import Flask, request, jsonify, render_template

from python_start_project.web_app.flask_application import FlaskApplication

PATH = "example"


def add_example_routes(flask: Flask, flask_application: FlaskApplication):
    # http://localhost:5000/example
    # http://localhost:5000/example/
    # http://localhost:5000/example/second
    @flask.route(flask_application.get_path(PATH))
    @flask.route(flask_application.get_path(path("second")))
    def example():
        return "Hello World from example index"

    # http://localhost:5000/post
    # Content for POST method {"firstName": "Imre"}
    # Content-Type: application/json and Accept: application/json
    @flask.route(flask_application.get_path(path("post")), methods=['POST'])
    def example_post():
        content = request.get_json()
        print(content)
        return jsonify(content)

    # http://localhost:5000/example/template
    # http://localhost:5000/example/template/index
    @flask.route(flask_application.get_path(path("template")))
    @flask.route(flask_application.get_path(path("template/index")))
    def example_templates():
        user_data = {'firstName': 'Imre'}
        return render_template('index.html', title='Microservice', data=user_data)

    @flask.route(flask_application.get_path(path('echo/<name>')))
    def example_hello_name(name):
        return "ECHO: Hello {}!".format(name)


def path(base_path):
    return PATH + "/" + base_path
