import datetime

import logging

logger = logging.getLogger(__name__)


class Person:

    def __init__(self, first_name: str, last_name: str, birth_date: datetime):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def __repr__(self):
        logger.info("Through __repr__")
        return "first_name=" + self.first_name + ", last_name=" + self.last_name + ", birth_date=" + \
            self.birth_date.strftime("%d.%m.%Y")

    def __str__(self):
        logger.info("Through __str__")
        return "first_name=" + self.first_name + ", last_name=" + self.last_name + ", birth_date=" + \
            self.birth_date.strftime("%d.%m.%Y")
