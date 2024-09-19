import unittest


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class TestMathOperations(unittest.TestCase):
    def test_divide(self):
        self.assertRaises(ValueError, divide, 10, 0)  # Check if ValueError is raised
