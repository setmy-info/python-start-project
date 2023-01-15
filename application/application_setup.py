import logging
import os
from argparse import ArgumentParser

import yaml

from log import logging_setup

logger = logging.getLogger(__name__)


class Application:
    APPLICATION_PROFILES_ENVIRONMENT = 'APPLICATION_PROFILES'

    def __init__(self, name: str, version: str, argument_parser: ArgumentParser):
        self.name: str = name
        self.version: str = version
        self.argument_parser = argument_parser
        self.vcs: str = None
        self.environ = os.environ
        self.args = None
        self.profiles: [str] = ["default"]
        self.yaml_list = []
        self.effective_yaml = None


def parse_environment_variables(application: Application):
    try:
        profiles: str = application.environ["APPLICATION_PROFILES"]
        profiles_list = profiles.split(',')
        profiles_list = list(map(lambda profile_item: profile_item.strip(), profiles_list))
        application.profiles.extend(profiles_list)
    except:
        logger.info("No APPLICATION_PROFILES is set")


def parse_arguments(application: Application):
    if application.argument_parser is not None:
        application.argument_parser.add_argument('--profiles', help='Comma separated profiles.',
                                                 type=str, nargs='*', action='append', required=False)
        application.args = application.argument_parser.parse_args()
        profiles = application.args.profiles
        if profiles is not None:
            for profile_inner_list in profiles:
                for inner_list_item in profile_inner_list:
                    profiles_list = inner_list_item.split(',')
                    profiles_list = list(map(lambda profile_item: profile_item.strip(), profiles_list))
                    application.profiles.extend(profiles_list)


def unique(it):
    s = set()
    for el in it:
        if el not in s:
            s.add(el)
            yield el


def clean_profiles(application: Application):
    application.profiles = list(unique(application.profiles))
    logger.info("Profiles: " + str(application.profiles))


def load_yaml_list(application: Application):
    with open('./resources/application.yaml', 'r') as file:
        application.yaml_list.append(yaml.safe_load(file))
    return application


def make_effective_yaml(application: Application):
    # TODO : overloading by list. Currently first.
    application.effective_yaml = application.yaml_list[0]


def application_setup(application: Application):
    logging_setup(application)
    parse_environment_variables(application)
    parse_arguments(application)
    clean_profiles(application)
    make_effective_yaml(load_yaml_list(application))
    logger.info(str(application.yaml_list))
    pass
