#!/usr/bin/python3
""" test the first module """
import io
import sys
import unittest
from unittest.mock import patch, call
from models.rectangle import Rectangle
from models.square import Square


class Test_String_Methods(unittest.TestCase):
    """ Test some methods using unittest """
    def test_area_square(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        s_1 = Square(5)
        print(s_1)
        print(s_1.area())
        s_1.display()

        s_2 = Square(5, 4, 3, 12)
        print(s_2)
        print(s_2.area())
        s_2.display()

        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(
            ), "[Square] (1) 0/0 - 5\n"
            "25\n""#####\n#####\n#####\n#####\n#####\n"
            "[Square] (12) 4/3 - 5\n"
            "25\n"
            "\n\n\n    #####\n    #####\n    #####\n    #####\n    #####\n")

    def test_Value_error(self):
        """ test value error """
        with self.assertRaises(ValueError) as exc:
            obj = Square(-1, 4, 5, 12)
            obj.width = 0
        self.assertEqual(str(exc.exception), "width must be > 0")

        with self.assertRaises(ValueError) as exc:
            obj = Square(1, -4, 5, 12)
            obj.x = 0
        self.assertEqual(str(exc.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as exc:
            obj = Square(1, 4, -5, 12)
            obj.y = 0
        self.assertEqual(str(exc.exception), "y must be >= 0")

    def test_Type_error(self):
        """ test the typeError for all variables """
        with self.assertRaises(TypeError) as exc:
            obj = Square("Ahmed", 3, 4, 12)
            obj.width = "MO"
            obj.width = [1, 2, 3]
            obj.width = (1, 2, 3)
            obj.width = {"key": 1, "key_2": 3}
            obj.width = None
        self.assertEqual(str(exc.exception), "width must be an integer")

        with self.assertRaises(TypeError) as exc:
            obj = Square(3, "Ahmed", 4, 12)
            obj.x = "MO"
            obj.x = [1, 2, 3]
            obj.x = (1, 2, 3)
            obj.x = {"key": 1, "key_2": 3}
            obj.x = None
        self.assertEqual(str(exc.exception), "x must be an integer")

        with self.assertRaises(TypeError) as exc:
            obj = Square(3, 4, "Ahmed", 12)
            obj.y = "MO"
            obj.y = [1, 2, 3]
            obj.y = (1, 2, 3)
            obj.y = {"key": 1, "key_2": 3}
            obj.y = None
        self.assertEqual(str(exc.exception), "y must be an integer")
