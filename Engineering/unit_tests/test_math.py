# William Pulkownik
# 11Nov2019
# unit_tests.py
# this set of unit tests verifies select functions 
# from the Math and Square classes

from unittest import TestCase
from unittest.mock import patch
from mathStuff import Math

class TestMath(TestCase):
    def setUp(self):
        self.calculator = Math()

    def test_factorial(self):
        self.assertEqual(self.calculator.factorial(4), 24, "find factorial of 4")

    def test_power_simple(self):
        self.assertEqual(self.calculator.power(2,3), 8, "test small base and exponent")

    def test_power_negative(self):
        self.assertEqual(self.calculator.power(2,-3), 8, "test a negative exponent")

    def test_is_even(self):
        self.assertEqual(self.calculator.is_even(8), True)
