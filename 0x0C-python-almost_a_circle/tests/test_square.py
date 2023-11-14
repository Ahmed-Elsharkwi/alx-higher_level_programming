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
            ), "[Square] (24) 0/0 - 5\n"
            "25\n""#####\n#####\n#####\n#####\n#####\n"
            "[Square] (12) 4/3 - 5\n"
            "25\n"
            "\n\n\n    #####\n    #####\n    #####\n    #####\n    #####\n")

    def test_Value_error(self):
        """ test value error """
        with self.assertRaises(ValueError) as exc:
            obj = Square(-1, 4, 5, 12)
            obj.size = 0
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
            obj.size = "MO"
            obj.size = [1, 2, 3]
            obj.size = (1, 2, 3)
            obj.size = {"key": 1, "key_2": 3}
            obj.size = None
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

    def test_setter_getter(self):
        """ set the value of size and get the value"""
        s = Square(3)
        self.assertEqual(s.size, 3)

        s.size = 7
        self.assertEqual(s.size, 7)

    def test_update(self):
        """ test the update method"""
        r = Square(4)

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        print(r)

        r.update(98)
        print(r)

        r.update(98, 3)
        print(r)

        r.update(98, 3, 5)
        print(r)

        r.update(98, 3, 5, 6)
        print(r)

        r.update(id=5)
        print(r)

        r.update(size=7)
        print(r)

        r.update(y=8, x=5, size=2, id=7)
        print(r)

        r.update(x=8, y=9, size=3, id=5)
        print(r)

        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(
            ), "[Square] (26) 0/0 - 4\n"
               "[Square] (98) 0/0 - 4\n"
               "[Square] (98) 0/0 - 3\n"
               "[Square] (98) 5/0 - 3\n"
               "[Square] (98) 5/6 - 3\n"
               "[Square] (5) 5/6 - 3\n"
               "[Square] (5) 5/6 - 7\n"
               "[Square] (7) 5/8 - 2\n"
               "[Square] (5) 8/9 - 3\n")

    def test_dict(self):
        """ test the dict method """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        r1 = Square(10, 2, 1, 9)
        dic = r1.to_dictionary()
        print(dic)
        print(type(dic))

        r1.update(12, 10, 5, 9)
        dic_1 = r1.to_dictionary()
        print(dic_1)
        print(type(dic_1))

        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(
            ),
            "{'x': 2, 'y': 1, 'size': 10, 'id': 9}\n"
            "<class 'dict'>\n"
            "{'x': 5, 'y': 9, 'size': 10, 'id': 12}\n"
            "<class 'dict'>\n")


if __name__ == '__main__':
    unittest.main()
