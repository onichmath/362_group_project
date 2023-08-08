"""
Authors: Matthew O'Malley-Nichols, Pedram Jarahzedah, Devin Fahnestock
Description: Unit tests for our 362 group project.
"""
import unittest
from task import conv_endian, convert_to_hex, create_hex_array, conv_num


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    # Testing for conv_num

    def test_conv_int_123(self):
        self.assertEqual(int(123), conv_num("123"))

    def test_conv_int_0(self):
        self.assertEqual(int(0), conv_num("0"))

    def test_conv_int_n123(self):
        self.assertEqual(int(-123), conv_num("-123"))

    def test_conv_float_123p45(self):
        self.assertEqual(float(123.45), conv_num("123.45"))

    def test_conv_float_123p(self):
        self.assertEqual(float(123.0), conv_num("123."))

    def test_conv_float_p45(self):
        self.assertEqual(float(0.45), conv_num(".45"))

    def test_conv_int_n123p45(self):
        self.assertEqual(float(-123.45), conv_num("-123.45"))

    def test_conv_empty(self):
        self.assertEqual(None, conv_num(""))

    def test_conv_float_1(self):
        self.assertEqual(None, conv_num("-"))

    def test_conv_float_n1p1(self):
        self.assertEqual(float(-1.1), conv_num("-1.1"))

    def test_double_dot(self):
        self.assertEqual(None, conv_num("123.45.67"))

    def test_single_p(self):
        self.assertEqual(float(0), conv_num("."))

    def test_hex_FF(self):
        self.assertEqual(int(255), conv_num("0xFF"))



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
        self.assertEqual(['1', 'F', 'A', '0'], create_hex_array(2801))

    def test_hexarr_3(self):
        self.assertEqual(['0', '0'], create_hex_array(0))

    def test_endian_1(self):
        self.assertEqual('1F', conv_endian(31))

    def test_endian_2(self):
        self.assertEqual('0A F1', conv_endian(2801))

    def test_endian_3(self):
        self.assertEqual('1F', conv_endian(31, 'little'))

    def test_endian_4(self):
        self.assertEqual('F1 0A', conv_endian(2801, 'little'))

    def test_endian_5(self):
        self.assertEqual(None, conv_endian(2801, 'small'))

    def test_endian_6(self):
        self.assertEqual('0A F1', conv_endian(2801, 'big'))

    def test_endian_7(self):
        self.assertEqual('-0A F1', conv_endian(-2801, 'big'))

    def test_endian_8(self):
        self.assertEqual('-F1 0A', conv_endian(-2801, 'little'))

    # Example Tests From Module
    def test_endian_module_1(self):
        self.assertEqual(conv_endian(954786, 'big'), '0E 91 A2')

    def test_endian_module_2(self):
        self.assertEqual(conv_endian(954786), '0E 91 A2')

    def test_endian_module_3(self):
        self.assertEqual(conv_endian(-954786), '-0E 91 A2')

    def test_endian_module_4(self):
        self.assertEqual(conv_endian(954786, 'little'), 'A2 91 0E')

    def test_endian_module_5(self):
        self.assertEqual(conv_endian(-954786, 'little'), '-A2 91 0E')

    def test_endian_module_6(self):
        self.assertEqual(conv_endian(
            num=-954786, endian='little'), '-A2 91 0E')

    def test_endian_module_7(self):
        self.assertEqual(conv_endian(num=-954786, endian='small'), None)


if __name__ == "__main__":
    unittest.main()
