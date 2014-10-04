#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Peymon & Haoran'
__email__ = "Payran@payran.com"

__copyright__ = "2014 PeyRan"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def checksum(upc):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a string
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
    else:
        num = list(upc)[0:11]
        # generate checksum using the first 11 digits provided
        # add the digits in the odd-numbered positions together and multiply by three
        odd = sum(int(x) for x in num[::2])

       # find digits in even-numbered positions
        even = sum(int(x) for x in num[1::2])

        # add the digits in the even-numbered positions to the result.
        add = odd * 3 + even

        # find the result modulo 10, subtract from 10
        x = 10 - add % 10

        # check against the the twelfth digit
        if x == int(list(upc)[11]):

            # return True if they are equal, False otherwise
            return True
        return False

