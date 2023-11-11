#!/usr/bin/python3
""" test the first module """
import io
import sys
import unittest
from unittest.mock import patch, call
from models.rectangle import Rectangle
from models.base import Base


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


class Test_other_methods(unittest.TestCase):
    """ test the rest methods of the class rectangle """
    def test_area(self):
        """ test the area function"""
        obj = Rectangle(5, 4, 0, 0, 2)
        self.assertEqual(obj.area(), 20)

        obj.width = 10
        obj.height = 20
        self.assertEqual(obj.area(), 200)

    def test_display(self):
        """ test the display function """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        obj_1 = Rectangle(5, 6, 0, 0, 2)
        obj_1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), (
            "#####\n#####\n#####\n#####\n#####\n#####\n"))

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        obj_1.width = 6
        obj_1.height = 4
        obj_1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), (
            "######\n######\n######\n######\n"))

    def test__str__(self):
        """ test str method """
        r = Rectangle(4, 6)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r)
        r.width = 7
        r.height = 5
        r.id = 12
        r.x = 8
        r.y = 7
        print(r)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(
            ), "[Rectangle] (2) 0/0 - 4/6\n[Rectangle] (12) 8/7 - 7/5\n")


if __name__ == '__main__':
    unittest.main()