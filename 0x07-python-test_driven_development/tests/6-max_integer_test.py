import unittest
max_integer = __import__('6-max_integer').max_integer

class Test_code(unittest.TestCase):
    def test_len(self):
        self.assertEqual(max_integer([]), None)
    def test_list(self):
        self.assertEqual(max_integer([2, 3, 4, 5]), 5)
if __name__ == '__main__':
    unittest.main()
