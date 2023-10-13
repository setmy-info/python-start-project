import logging

from smi_python_commons.config.application import Application

from python_start_project.web_app.flask_application import FlaskApplication
from python_start_project.web_app.flask_main import main

log = logging.getLogger(__name__)


class FlaskRunner:

    def __init__(self):
        self.name = "flask-runner"

    def get_name(self):
        return self.name

    def execute(self, app: Application, sub_command: str):
        log.info("Executing Flask runner")
        FlaskApplication.flask_application = FlaskApplication(app, sub_command)
        return main(FlaskApplication.flask_application)
