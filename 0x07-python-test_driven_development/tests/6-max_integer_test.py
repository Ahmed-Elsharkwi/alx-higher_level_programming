import unittest
max_integer = __import__('6-max_integer').max_integer

class Test_code(unittest.TestCase):
    def test_len(self):
        self.assertEqual(max_integer([]), None)
    def test_list(self):
        self.assertEqual(max_integer([2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 3, 4, 2]), 5)
        self.assertEqual(max_integer([5, 3, 6, 1, 2]), 6)
        self.assertEqual(max_integer([-1, 0, 2, 4, 5]), 5)
        self.assertEqual(max_integer([5]), 5)
if __name__ == '__main__':
    unittest.main()
