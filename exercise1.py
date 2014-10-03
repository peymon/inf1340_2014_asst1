#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Peymon & Haoran'
__email__ = ""

__copyright__ = "2014 Susan Sim"
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

    gpa = 0.0
    if type(grade) is not str:
       raise ValueError("Wrong input, try again")

    else:
        return letter_grade[grade]


        # remove this line once the code is implemented
        # check that the grade is one of the accepted values
        # assign grade to letter_grade

    if type(grade) is not int:
        raise TypeError("Invalid type passed as parameter")

    elif 85 <= grade <= 100:
            #print ("Your GPA is 4.0")
            gpa = 4.0
    elif 80 <= grade <= 84:
            #print ("Your GPA is 3.7")
            gpa = 3.7
    elif 77 <= grade <= 79:
            gpa = 3.3 # assigns value to gpa. Could also be print ("Your GPA is 3.3")
    elif 73 <= grade <= 76:
            #print ("Your GPA is 3.0")
            gpa = 3.0
    elif 70 <= grade <= 72:
            #print ("Your GPA is 2.7")
            gpa = 2.7
    elif 0 <= grade <= 69:
            #print ("Your GPA is 0")
            gpa = 0
    return gpa
        # remove this line once the code is implemented
        # check that grade is in the accepted range
        # convert the numeric grade to a letter grade
        # assign the value to letter_grade
        # hint: letter_grade = mark_to_letter(grade)
    else:
        # raise a TypeError exception


  # write a long if-statement to convert letter_grade
   # assign the value to gpa
print (grade_to_gpa("A"))