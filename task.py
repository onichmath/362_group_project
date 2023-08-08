"""
Authors: Matthew O'Malley-Nichols, Pedram Jarahzedah, Devin Fahnestock
Description: Tasks for our group project
"""


def str_to_num(num_str):
    """Takes a str representing a num and converts it to an number"""
    map = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "A": 10,
            "B": 11,
            "C": 12,
            "D": 13,
            "E": 14,
            "F": 15
            }
    return map[num_str]

def conv_int(int_str, parity):
    """Converts a string representing an int to an int"""
    result = 0
    power = 0
    for num in int_str[::-1]:
        result += str_to_num(num) * (10 ** power)
        power += 1
    return parity * result

def conv_float(left_num_str, right_num_str, parity):
    """Converts a str representing a float to a float"""
    result = 0
    left_power = 0
    right_power = -1
    for num in left_num_str[::-1]:
        result += str_to_num(num) * (10 ** left_power)
        left_power += 1
    for num in right_num_str:
        result += str_to_num(num) * (10 ** right_power)
        right_power -= 1
    return parity * result

def conv_hex(hex_str, parity):
    """Converts a str representing a hex to an int"""
    print(hex_str)
    result = 0
    power = 0
    for num in hex_str[::-1]:
        if num == ".":
            return None
        result += str_to_num(num) * (16 ** power)
        power += 1
    return parity * result


def conv_num(num_str_param):
    """Takes in a str representing a num, converts it to base 10, and returns it."""
    if type(num_str_param) is not str:
        return None
    parity = 1
    num_str = str(num_str_param)
    if num_str.count("-") > 0:
        if num_str[0] == "-":
            parity = -1
            num_str = num_str[1::]
        else:
            return None
    if num_str.count("0x") > 0:
        if num_str[:2] == "0x":
            num_str = num_str[2::]
            return conv_hex(num_str, parity)
    if num_str.count(".") == 1:
        split_num_str = num_str.split('.') 
        return conv_float(split_num_str[0], split_num_str[1], parity)
    if num_str.isdecimal():
        return conv_int(num_str, parity)
    return None

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


def create_hex_array(num):
    hex = []
    if num == 0:
        hex.append(convert_to_hex(0))
        hex.append(convert_to_hex(0))
    while num > 0:
        hex.append(convert_to_hex(num % 16))
        num //= 16
    if len(hex) % 2 != 0:
        hex.append(convert_to_hex(0))
    return hex


def conv_endian(num, endian='big'):
    """Takes in an int as num and converts it to a hexadecimal num.
    The endian type is determined by the flag endian. Returns a string."""
    hexstr = ""
    if num < 0:
        num = abs(num)
        hexstr += "-"
    hex = create_hex_array(num)
    if endian == 'little':
        spacer = False
        while len(hex) > 0:
            if spacer:
                hexstr += " "
            hexstr += hex.pop(1)
            hexstr += hex.pop(0)
            spacer = True
    elif endian == 'big':
        spacer = False
        while len(hex) > 0:
            if spacer:
                hexstr += " "
            hexstr += hex.pop()
            hexstr += hex.pop()
            spacer = True
    else:
        return None

    return hexstr
