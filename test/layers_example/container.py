from person_dao import PersonDAO
from person_service import PersonService

person_dao = PersonDAO()
person_service = PersonService(person_dao)
