from smi_python_commons.config.application import Application


class FlaskApplication:

    def __init__(self, application: Application, sub_command: str):
        self.application = application
        self.sub_command = sub_command

    def get_path(self, path: str):
        # TODO : get values from config
        return "" + path

    def get_host(self):
        # TODO : get values from config
        return "0.0.0.0"

    def get_port(self):
        # TODO : get values from config
        return 5000

    def get_workers(self):
        # TODO : get values from config
        return 4

    def get_server_type(self):
        # TODO : get values from config
        return "waitress"
        #return "werkzeug"
