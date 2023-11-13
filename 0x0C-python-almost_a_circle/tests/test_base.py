#!/usr/bin/python3
""" test the first module """
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


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

    def test_to_json_string(self):
        """
        test the method to json string
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        print(json_dictionary)
        print(type(json_dictionary))

        json_dictionary = Base.to_json_string([])
        print(json_dictionary)

        json_dictionary = Base.to_json_string([{}])
        print(json_dictionary)

        json_dictionary = Base.to_json_string(None)
        print(json_dictionary)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(
            ), '[{"id": 5, "width": 10, "height": 7, "x": 2, "y": 8}]\n'
               "<class 'str'>\n"
               "[]\n"
               "[]\n"
               "[]\n")


class Test_Methods(unittest.TestCase):
    """ test other methods """
    def test_save_to_file(self):
        """ test the save file method """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            print(file.read())

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            print(file.read())

        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(
            ),  '[{"id": 8, "width": 10, "height": 7, "x": 2, "y": 8},'
                ' {"id": 9, "width": 2, "height": 4, "x": 0, "y": 0}]\n'
               "[]\n")

    def test_from_json_string(self):
        """ test the from json string """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        print("[{}] {}".format(type(list_output), list_output))

        json_list_input = Rectangle.to_json_string([])
        print(json_list_input)

        json_list_input = Rectangle.to_json_string([{}])
        print(json_list_input)

        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(
        ),  "[<class 'list'>] [{'id': 89, 'width': 10, 'height': 4},"
            " {'id': 7, 'width': 1, 'height': 7}]\n"
            "[]\n"
            "[]\n")

    def test_create(self):
        """ test the method create"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        print(r1)
        print(r2)
        print(r1 is r2)
        print(r1 == r2)

        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(
        ), "[Rectangle] (6) 1/0 - 3/5\n"
           "[Rectangle] (6) 1/0 - 3/5\n"
           "False\nFalse\n")


if __name__ == '__main__':
    unittest.main()
