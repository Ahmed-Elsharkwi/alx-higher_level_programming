import unittest
import contextlib
import io

def foo(inStr):
    print("hi" + inStr)

class TestFoo(unittest.TestCase):
    def test_foo(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            foo('bar')
        self.assertEqual(f.getvalue(), 'hibar\n')

if __name__ == '__main__':
    unittest.main()

