# William Pulkownik
# test_square.py
# this program will run unit tests on the test_square
# class with a mock object

import unittest
from unittest.mock import MagicMock, patch
from squareStuff import Square

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.math_mock = MagicMock()
        self.math_mock.power = MagicMock(return_value = 100)
        self.square = Square(side=10, math=self.math_mock)

    def test_area(self):
        self.assertEqual(self.square.area(), 100)
        self.math_mock.power.assert_called_with(10, 2)
