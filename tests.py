"""
Authors: Matthew O'Malley-Nichols, Pedram Jarahzedah, Devin Fahnestock
Description: Unit tests for our 362 group project.
"""
import unittest
from task import conv_endian, convert_to_hex, create_hex_array


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    # Testing For conv_endian

    def test_hex_ten(self):
        self.assertEqual('A', convert_to_hex(10))

    def test_hex_fifteen(self):
        self.assertEqual('F', convert_to_hex(15))

    def test_hex_zero(self):
        self.assertEqual('0', convert_to_hex(0))

    def test_hexarr_1(self):
        self.assertEqual(['F', '1'], create_hex_array(31))

    def test_hexarr_2(self):
        self.assertEqual(['1', 'F', 'A'], create_hex_array(2801))

    def test_hexarr_3(self):
        self.assertEqual(['0'], create_hex_array(0))


if __name__ == "__main__":
    unittest.main()
