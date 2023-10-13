from smi_python_commons.arguments.argument import Argument
from smi_python_runner.services.arguments_register_service import arguments_register_service
from smi_python_runner.services.runner_register_service import runner_register_service

from python_start_project.web_app.flask_runner import FlaskRunner


def register():
    arguments_register_service.register(Argument('example', 'e', str, 'Example', True))
    runner_register_service.register(FlaskRunner())
