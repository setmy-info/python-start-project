import unittest


# Example integration test
class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_name(self):
        self.assertEqual('Imre', 'Imre')


if __name__ == "__main__":
    unittest.main()
