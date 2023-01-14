import logging

from person_dao import PersonDAO

logger = logging.getLogger(__name__)


class PersonService:

    @staticmethod
    def get_all_persons():
        logger.info("Getting all persons at service layer")
        persons = PersonDAO.get_all_persons()
        logger.info("Persons: " + str(persons))
        return PersonDAO.get_all_persons()
