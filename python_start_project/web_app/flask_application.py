from smi_python_commons.config.application import Application


class FlaskApplication:

    def __init__(self, application: Application, sub_command: str):
        self.application = application
        self.sub_command = sub_command

    def get_path(self, path: str):
        return "" + path

    def get_host(self):
        return "0.0.0.0"

    def get_port(self):
        return 5000

    def get_workers(self):
        return 4
