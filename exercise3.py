#!/usr/bin/env python3

"""
    Rock, Paper, Scissors

    Assignment 1, Exercise 3, INF1340 Fall 2014
"""

__author__ = "Peymon & Haoran"
__email__ = "Payran@payran.com"

__copyright__ = "2014 PeyRan"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def decide_rps(player1, player2):
    """
    Choosing a winner based on their hand

    :param player1: first player's hand
    :param player2: second player's hand

    :raises:
        ValueError: if input is not in the dictionary
        TypeError: if type is not a string
    :return: the winner of the match
    """
    # input all conditions in a dictionary
    rps = {
        ("Rock", "Paper"): 2,
        ("Rock", "Scissors"): 1,
        ("Rock", "Rock"): 0,
        ("Paper", "Scissors"): 2,
        ("Paper", "Rock"): 1,
        ("Paper", "Paper"): 0,
        ("Scissors", "Rock"): 2,
        ("Scissors", "Paper"): 1,
        ("Scissors", "Scissors"): 0
    }

    # convert players' input into tuple
    test = (player1, player2)

    # raise a TypeError exception if input not string
    if type(player1) is not str or type(player2) is not str:
        raise TypeError("Wrong input, try again")

    # if the test is not in rps raise ValueError
    elif test not in rps.keys():
        raise ValueError("Wrong input, try again")

    # if conditions met return the result
    else:
        return rps[test]
