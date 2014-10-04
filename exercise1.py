#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Peymon & Haoran'
__email__ = "Payran@payran.com"

__copyright__ = "2014 PayRan"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.

    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """


    letter_grade = {'A+': 4.0,
                    'A': 4.0,
                    'A-': 3.7,
                    'B+': 3.3,
                    'B': 3.0,
                    'B-': 2.7,
                    'FZ': 0
                    }
    # initial value of gpa
    gpa = 0.0

    # input grade value must be string or integer, otherwise raise TypeError

    #if grade input is a string and its value corresponds with any of letter_grade dictionary keys,
    #return the corresponding key value. For ex. if grade input is "A+" return 4.0
    if type(grade) is str:
        if grade in letter_grade.keys():
            return letter_grade[grade]
        #if input is not one of the keys in letter_grade, raise ValueError
        else:
            raise ValueError("Wrong input, try again")
    # if grade input is integer it must be between 0-100, otherwise raise ValueError
    # assign value to gpa according to where grade falls between 0-100
    elif type(grade) is int:

        if 85 <= grade <= 100:
            #assign value to gpa.
            gpa = 4.0
        elif 80 <= grade <= 84:
            #assign value to gpa.
            gpa = 3.7
        elif 77 <= grade <= 79:
            #assign value to gpa.
            gpa = 3.3
        elif 73 <= grade <= 76:
            #assign value to gpa.
            gpa = 3.0
        elif 70 <= grade <= 72:
            #assign value to gpa.
            gpa = 2.7
        elif 0 <= grade <= 69:
            #assign value to gpa.
            gpa = 0
        else:
            raise ValueError("Please make sure your input is between 0 - 100%")
        # return gpa
        return gpa

    # if grade input is not string or integer raise an error
    else:
        # raise a TypeError exception
        raise TypeError("Invalid type passed as parameter")
