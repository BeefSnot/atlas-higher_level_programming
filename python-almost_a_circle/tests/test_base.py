# tests/test_base.py

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id_provided(self):
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_id_not_provided(self):
        Base._Base__nb_objects = 0  # Resetting the class attribute for testing
        b2 = Base()
        self.assertEqual(b2.id, 1)
        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_id_mixed(self):
        Base._Base__nb_objects = 0  # Resetting the class attribute for testing
        b4 = Base()
        self.assertEqual(b4.id, 1)
        b5 = Base(5)
        self.assertEqual(b5.id, 5)
        b6 = Base()
        self.assertEqual(b6.id, 2)

if __name__ == '__main__':
    unittest.main()
