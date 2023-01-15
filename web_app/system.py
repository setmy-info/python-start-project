import os

from flask import Flask
from application_loader_service import ApplicationLoaderService
import logging
from logging.handlers import RotatingFileHandler

global system


class System:
    ENVIRONMENT = 'ENVIRONMENT'

    def __init__(self):
        self.applicationLoaderService = ApplicationLoaderService.get_instance()
        self.app = None
        self.application_properties = None

    def init(self):
        self.load_config()
        self.logger_init(self.application_properties.log)
        self.flask_init()

    def load_config(self):
        self.application_properties = self.applicationLoaderService.load_application_properties()

    @staticmethod
    def logger_init(log):
        logging.basicConfig(filename=log.directory + log.fileName, format=log.format, level=log.level)
        handler = RotatingFileHandler(filename=log.directory + log.fileName, maxBytes=log.size, backupCount=1)
        log = logging.getLogger()
        log.addHandler(handler)

    def flask_init(self):
        self.app = Flask(__name__, template_folder=self.application_properties.server.templateFolder,
                         static_folder=self.application_properties.server.staticFolder, static_url_path='')
        self.app.config.from_object(os.environ[System.ENVIRONMENT])

    def path(self, path):
        return self.application_properties.rest.root + path

    def get_host(self):
        return self.application_properties.server.host

    def get_port(self):
        return self.application_properties.server.port


system = System()
