import math
import sys

BASE = 62

UPPERCASE_OFFSET = 55
LOWERCASE_OFFSET = 61
DIGIT_OFFSET = 48

def true_ord(char):   
    if char.isdigit():
        return ord(char) - DIGIT_OFFSET
    elif 'A' <= char <= 'Z':
        return ord(char) - UPPERCASE_OFFSET
    elif 'a' <= char <= 'z':
        return ord(char) - LOWERCASE_OFFSET
    else:
        raise ValueError("%s is not a valid character" % char)

def true_chr(integer):
    if integer < 10:
        return chr(integer + DIGIT_OFFSET)
    elif 10 <= integer <= 35:
        return chr(integer + UPPERCASE_OFFSET)
    elif 36 <= integer < 62:
        return chr(integer + LOWERCASE_OFFSET)
    else:
        raise ValueError("%d is not a valid integer in the range of base %d" % (integer, BASE))


def encode(key):
    int_sum = 0
    reversed_key = key[::-1]
    for idx, char in enumerate(reversed_key):
        print(true_ord(char))
        int_sum += true_ord(char) * int(math.pow(BASE, idx))
    return int_sum


def decode(integer):
    if integer == 0:
        return '0'
    
    string = ""
    while integer > 0:
        remainder = integer % BASE
        string = true_chr(remainder) + string
        integer =int(integer/BASE)
    return string