import datetime
import unittest

from test.layers_example.person import Person


class PersonTest(unittest.TestCase):

    def test_str_for_single_element(self):
        person = Person("Imre", "Tabur", datetime.datetime(1975, 12, 23))
        self.assertEqual("first_name=Imre, last_name=Tabur, birth_date=23.12.1975", str(person),
                         "Should be correct str (__repr__) presentation for element")

    def test_str_for_list(self):
        persons = [
            Person("Imre", "Tabur", datetime.datetime(1975, 12, 23))
        ]
        self.assertEqual("[first_name=Imre, last_name=Tabur, birth_date=23.12.1975]", str(persons),
                         "Should be correct str (__repr__) presentation for element")


if __name__ == '__main__':
    unittest.main()
