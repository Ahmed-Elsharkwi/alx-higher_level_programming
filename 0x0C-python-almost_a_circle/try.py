import io
import sys
import unittest

def foo(name):
    print(name)

class TestFoo(unittest.TestCase):
    def test_foo(self):
        capturedOutput = io.StringIO() # Create StringIO object
        sys.stdout = capturedOutput # and redirect stdout.
        foo("Ahmed") # Call function.
        sys.stdout = sys.__stdout__ # Reset redirect.
        self.assertEqual(capturedOutput.getvalue(), ("Ahmed\n")) # Assert output.

        capturedOutput = io.StringIO() # Create StringIO object
        sys.stdout = capturedOutput
        foo("Mo")
        sys.stdout = sys.__stdout__ # Reset redirect.
        self.assertEqual(capturedOutput.getvalue(), ("Mo\n")) # Assert output.
if __name__ == '__main__':
    unittest.main()
