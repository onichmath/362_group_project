"""
Authors: Matthew O'Malley-Nichols, Pedram Jarahzedah, Devin Fahnestock
Description: Unit tests for our 362 group project.
"""
import unittest
from task import conv_endian, convert_to_hex


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    # Testing For conv_endian

    def test_helper_valid(self):
        self.assertEqual('A', convert_to_hex(10))


if __name__ == "__main__":
    unittest.main()
