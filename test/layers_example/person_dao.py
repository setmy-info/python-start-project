import datetime
import logging

from person import Person

logger = logging.getLogger(__name__)


class PersonDAO:

    def get_all_persons(self):
        logger.info("Getting all persons at DAO layer")
        return [
            Person("Imre", "Tabur", datetime.datetime(1975, 12, 23))
        ]


person_dao = PersonDAO()
