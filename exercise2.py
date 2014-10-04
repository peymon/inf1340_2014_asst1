#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Peymon & Haoran'
__email__ = ""

__copyright__ = "2014 PeyRan"
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
    if type(upc) is not str:
    # raise TypeError if not string
        raise TypeError("Wrong input, try again")
    # check length of string
    elif len(upc) != 12:
    # raise ValueError if not 12
        raise ValueError("Wrong input, try again")
    # convert string to array
    # hint: use the list function
    else:
        num=list(upc)[0:11]
    # generate checksum using the first 11 digits provided
        odd =sum(int(x) for x in num[::2])
        even = sum(int(x) for x in num[1::2])
        Sum = odd*3+even
        X = 10 - Sum%10
    # check against the the twelfth digit
        if X == int(list(upc)[11]):
    # return True if they are equal, False otherwise
            return True
        return False

