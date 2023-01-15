'''
Created on 20. mai 2019

@author: Imre Tabur <imre.tabur@eesti.ee>
'''
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_name(self):
        self.assertEqual('Imre', 'Imre')


if __name__ == "__main__":
    unittest.main()
