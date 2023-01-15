from web_app.system import System

from flask import render_template
from flask import send_from_directory
from flask import request
from flask import jsonify
from web_app.index import index
import werkzeug

System.init()


@System.app.route(System.path("/"))
def idx():
    return index()


# http://localhost:5000/ImreTabur
@System.app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


# http://localhost:5000/template/
# http://localhost:5000/template/index
@System.app.route('/template/')
@System.app.route('/template/index')
def templates():
    user_data = {'firstName': 'Imre'}
    return render_template('index.html', title='Microservice', data=user_data)


# http://localhost:5000/static/another
@System.app.route('/static/<path:path>')
def static_content(path):
    try:
        return send_from_directory(System.app.static_folder, path + '/' + 'index.html')
    except werkzeug.exceptions.NotFound as e:
        raise e


# http://localhost:5000/post
# Content for POST method {"firstName": "Imre"}
# Content-Type: application/json and Accept: application/json
@System.app.route('/post', methods=['POST'])
def post():
    content = request.get_json()
    print(content)
    return jsonify(content)


def main():
    System.app.run(host=System.get_host(), port=System.get_port())


if __name__ == '__main__':
    main()
