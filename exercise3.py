#!/usr/bin/env python3


def decide_rps(player1, player2):
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

    test=(player1,player2)

    if type(player1) is not str or type(player2) is not str:
        raise TypeError("Wrong input, try again")
    elif test not in rps.keys():
        raise ValueError("Wrong input, try again")
    else:
        return rps[test]
