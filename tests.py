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

    def test_wrong_type_1(self):
        self.assertEqual(None, conv_num(1234))

    def test_wrong_type_2(self):
        self.assertEqual(None, conv_num(False))

    def test_hex_F22B4C(self):
        self.assertEqual(int(15870796), conv_num("0xF22B4C"))

    def test_hex_nFF(self):
        self.assertEqual(int(-255), conv_num("-0xFF"))

    def test_hex_decimal(self):
        self.assertEqual(None, conv_num("0xFF.23"))

    def test_double_hyphen(self):
        self.assertEqual(None, conv_num("-213-213"))

    def test_hex_lowercase(self):
        self.assertEqual(int(255), conv_num("0xff"))

    def test_hex_wrongalpha_1(self):
        self.assertEqual(None, conv_num("0xFz23"))

    def test_int_wrong_alpha_1(self):
        self.assertEqual(None, conv_num("213zo34"))

    def test_float_wrong_alpha_1(self):
        self.assertEqual(None, conv_num("123.45oz4"))

    def test_float_wrong_alpha_2(self):
        self.assertEqual(None, conv_num("123o4.34"))

    def test_int_wrong_alpha_2(self):
        self.assertEqual(None, conv_num("1230x"))

    def test_hex_prefix_1(self):
        self.assertEqual(None, conv_num("21040x4312"))

    def test_hex_prefix_2(self):
        self.assertEqual(None, conv_num("0xFD0x32df"))

    def test_hex_prefix_3(self):
        self.assertEqual(None, conv_num("-0xFD0x32df"))

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
