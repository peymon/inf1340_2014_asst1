#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def checksum (upc):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a strong
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """

    # check type of input
    if upc is not str:
    # raise TypeError if not string
         raise TypeError("Wrong input, try again")
    # check length of string
    elif len(upc) != 12:
    # raise ValueError if not 12
         raise ValueError("Wrong input, try again")
    # convert string to array
    # hint: use the list function
    else:
        num = list(upc)
    # generate checksum using the first 11 digits provided
    sum=3*(int(num(0))+int(num(2))+int(num(4))+int(num(6))+int(num(8))+int(num(10)))+int(num(1))+int(num(3))+int(num(5))+int(num(7))+int(num(9));
    # check against the the twelfth digit
    if sum == int(num(11)):
    # return True if they are equal, False otherwise
        return True
    return False

