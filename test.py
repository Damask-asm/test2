from main import add, multiply
import unittest

class TestAdd(unittest.TestCase):
    def test_add(self):
        result = add(1, 2)
        expected_value = 3

        self.assertEqual(result, expected_value)

    def test_add_int_str(self):
        result = add(3, "4")
        expected_value = 7

        if result == expected_value:
            print("Test passed")
        else:
            print("Test failed")


class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        result = multiply(1, 2)
        expected_value = 2

        self.assertEqual(result, expected_value)


