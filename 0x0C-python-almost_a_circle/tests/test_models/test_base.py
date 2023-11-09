#!/usr/bin/python3
""" test the first module """
import unittest
from models.base import Base


class TestStringMethods(unittest.TestCase):
    """ Test some methods """
    def test_id_no_argumet(self):
        """
        if we do not pass any number
        and the value of the id is None
        """
        obj = Base()
        self.assertEqual(obj.id, 1)

        obj_1 = Base()
        self.assertEqual(obj_1.id, 2)

        obj_2 = Base(None)
        self.assertEqual(obj_2.id, 3)

        obj_2 = Base()
        self.assertEqual(obj_2.id, 4)

    def test_id_with_argument(self):
        """
        test the value of id
        if we pass an argument to construct
        """
        obj = Base(12)
        self.assertEqual(obj.id, 12)

        obj_1 = Base(-1)
        self.assertEqual(obj_1.id, -1)


if __name__ == '__main__':
    unittest.main()
