import unittest
from src.AddTwoNumbers import add


class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # Check if 2 + 3 equals 5
        self.assertEqual(add(-1, 1), 0)  # Check if -1 + 1 equals 0
        # self.assertEqual(add(0,0), 10) # Check if 0 + 0 equals 10

    def test_add2(self):
        self.assertEqual(add(2, 3), 5)  # Check if 2 + 3 equals 5

    def second_test(self):
        self.assertEqual(add(1, 1), 2)
