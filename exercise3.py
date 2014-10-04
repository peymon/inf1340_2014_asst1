#!/usr/bin/env python3

"""
    Rock, Paper, Scissors

    Assignment 1, Exercise 3, INF1340 Fall 2014
"""

__author__ = 'Peymon & Haoran'
__email__ = ""

__copyright__ = "2014 PeyRan"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

def decide_rps(player1, player2):
    # input all conditions in a dictionary
    rps = {
    ("Rock","Paper"):2,
    ("Rock","Scissors"):1,
    ("Rock","Rock"):0,
    ("Paper","Scissors"):2,
    ("Paper","Rock"):1,
    ("Paper","Paper"):0,
    ("Scissors","Rock"):2,
    ("Scissors","Paper"):1,
    ("Scissors","Scissors"):0
    }
    # convert players' input into tuple
    test=(player1,player2)
    # raise a TypeError exception
    if type(player1) is not str or type(player2) is not str:
        raise TypeError("Wrong input, try again")
    # check if the test is in rps
    elif test not in rps.keys():
        raise ValueError("Wrong input, try again")
    # return the result
    else:
        return rps[test]
