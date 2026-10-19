
import unittest

from src.solutions import is_even


class TestIsEven(unittest.TestCase):

    def test_positive_even_number(self):
        self.assertTrue(is_even(4))

    def test_positive_odd_number(self):
        self.assertFalse(is_even(7))

    def test_negative_even_number(self):
        self.assertTrue(is_even(-4))

    def test_negative_odd_number(self):
        self.assertFalse(is_even(-3))

    def test_zero_is_even(self):
        self.assertTrue(is_even(0))


if __name__ == "__main__":
    unittest.main()
