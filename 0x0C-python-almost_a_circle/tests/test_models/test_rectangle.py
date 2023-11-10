#!/usr/bin/python3
""" test the first module """
import unittest
from models.rectangle import Rectangle


class TestStringMethods(unittest.TestCase):
    """ Test some methods using unittest """
    def test_constructure_getter(self):
        """
        pass values through constructure
        and get the values using getter
        """
        obj = Rectangle(1, 2, 5, 8, 12)
        self.assertEqual(obj.id, 12)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 5)
        self.assertEqual(obj.y, 8)

    def test_setter_getter(self):
        """pass values with setter and get it with getter"""
        obj = Rectangle(9, 8)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 9)
        self.assertEqual(obj.height, 8)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

        obj.width = 10
        self.assertEqual(obj.width, 10)

        obj.height = 20
        self.assertEqual(obj.height, 20)

        obj.x = 2
        self.assertEqual(obj.x, 2)

        obj.y = 4
        self.assertEqual(obj.y, 4)

    def test_type_error(self):
        """ test the typeError for all variables """
        with self.assertRaises(TypeError) as exc:
            obj = Rectangle("Ahmed", 2, 3, 4, 12)
            obj.width = "MO"
            obj.width = [1, 2, 3]
            obj.width = (1, 2, 3)
            obj.width = {"key": 1, "key_2": 3}
            obj.width = None
        self.assertEqual(str(exc.exception), "width must be an integer")

        with self.assertRaises(TypeError) as exc:
            obj = Rectangle(2, "Ahmed", 3, 4, 12)
            obj.height = "MO"
            obj.height = [1, 2, 3]
            obj.height = (1, 2, 3)
            obj.height = {"key": 1, "key_2": 3}
            obj.height = None
        self.assertEqual(str(exc.exception), "height must be an integer")

        with self.assertRaises(TypeError) as exc:
            obj = Rectangle(3, 2, "Ahmed", 4, 12)
            obj.x = "MO"
            obj.x = [1, 2, 3]
            obj.x = (1, 2, 3)
            obj.x = {"key": 1, "key_2": 3}
            obj.x = None
        self.assertEqual(str(exc.exception), "x must be an integer")

        with self.assertRaises(TypeError) as exc:
            obj = Rectangle(3, 2, 4, "Ahmed", 12)
            obj.y = "MO"
            obj.y = [1, 2, 3]
            obj.y = (1, 2, 3)
            obj.y = {"key": 1, "key_2": 3}
            obj.y = None
        self.assertEqual(str(exc.exception), "y must be an integer")

    def test_Value_Error(self):
        """ test the valueError for all variables """
        with self.assertRaises(ValueError) as exc:
            obj = Rectangle(-1, 2, 4, 5, 12)
            obj.width = 0
        self.assertEqual(str(exc.exception), "width must be > 0")

        with self.assertRaises(ValueError) as exc:
            obj = Rectangle(1, -2, 4, 5, 12)
            obj.height = 0
        self.assertEqual(str(exc.exception), "height must be > 0")

        with self.assertRaises(ValueError) as exc:
            obj = Rectangle(1, 2, -4, 5, 12)
            obj.x = 0
        self.assertEqual(str(exc.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as exc:
            obj = Rectangle(1, 2, 4, -5, 12)
            obj.y = 0
        self.assertEqual(str(exc.exception), "y must be >= 0")
