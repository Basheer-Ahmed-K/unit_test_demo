import unittest


class TestWithSetup(unittest.TestCase):

    def setUp(self):
        # This method runs before each test case
        self.number = 10

    # setUp() is used to set up any initial state required for tests.

    def tearDown(self):
        # This method runs after each test case
        pass

    # tearDown() can be used to clean up after a test is executed (e.g., closing connections).

    def test_addition(self):
        result = self.number + 5
        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()
