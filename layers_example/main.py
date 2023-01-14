import logging
import sys

from application import application_setup
from layers_example import application
from person_service import PersonService

logger = logging.getLogger(__name__)


def main():
    logger.info(sys.version)
    logger.info("Persons: " + str(PersonService.get_all_persons()))
    logger.info("Person: " + str(PersonService.get_all_persons()[0]))


if __name__ == "__main__":
    application_setup(application)
    main()
