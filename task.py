"""
Authors: Matthew O'Malley-Nichols, Pedram Jarahzedah, Devin Fahnestock
Description: Tasks for our group project
"""


def conv_num(num_str):
    """Takes in a str representing a num, converts it to base 10, and returns it."""
    pass


def my_datetime(num_sec):
    """Takes in an int representing the num of secs since the epoch,
      and returns it as a string formatted as MM-DD-YYYY"""
    pass


def convert_to_hex(num):
    hexmap = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
    }
    return hexmap[num]


def conv_endian(num, endian='big'):
    """Takes in an int as num and converts it to a hexadecimal num.
    The endian type is determined by the flag endian. Returns a string."""
    pass
