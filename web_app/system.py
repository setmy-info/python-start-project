import os

from flask import Flask

from application import Application


class System:
    app = None
    application_properties = None

    @staticmethod
    def init():
        System.app = Flask(
            __name__,
            template_folder="../templates",
            static_folder="../static",
            static_url_path=''
        )
        try:
            System.app.config.from_object(os.environ[Application.APPLICATION_PROFILES_ENVIRONMENT])
        except:
            pass

    @staticmethod
    def path(path):
        return "" + path

    @staticmethod
    def get_host():
        return "0.0.0.0"

    @staticmethod
    def get_port():
        return 5000
