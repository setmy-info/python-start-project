import logging

from person_dao import person_dao

logger = logging.getLogger(__name__)


class PersonService:

    def __init__(self):
        self.person_dao = person_dao;

    def get_all_persons(self):
        logger.info("Getting all persons at service layer")
        persons = self.person_dao.get_all_persons()
        logger.info("Persons: " + str(persons))
        return self.person_dao.get_all_persons()


person_service = PersonService()
