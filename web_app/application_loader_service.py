from yaml_loader_service import YamlLoaderService
from properties import ApplicationProperties


class ApplicationLoaderService:
    CONFIG_FILE_NAME = "./resources/application.yaml"

    __instance = None

    def __init__(self):
        self.yamlLoaderService = YamlLoaderService.getInstance()
        self.loaded = None

    def load_application_properties(self):
        loaded = self.load()
        return ApplicationProperties(loaded)

    def load(self):
        self.loaded = self.yamlLoaderService.load(ApplicationLoaderService.CONFIG_FILE_NAME)
        return self.loaded

    @staticmethod
    def get_instance():
        if ApplicationLoaderService.__instance is None:
            ApplicationLoaderService.__instance = ApplicationLoaderService()
        return ApplicationLoaderService.__instance
