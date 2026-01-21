import logging
import sys

from container import person_service

logger = logging.getLogger(__name__)


def main():
    logger.info(sys.version)
    logger.info("Persons: " + str(person_service.get_all_persons()))
    logger.info("Person: " + str(person_service.get_all_persons()[0]))


if __name__ == "__main__":
    main()
