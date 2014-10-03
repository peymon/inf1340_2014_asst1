#!/usr/bin/env python3


def decide_rps(player1, player2):
    dic = {"rock,paper":2, "rock,scissors":1, "paper,rock":1, "paper,scissors":2, "scissors,rock":2, "scissors,paper":1}
    result = []
    player1 = str(player1.lower())
    player2 = str(player2.lower())
    if player1 is not "paper" and not "rock" and not "scissors":
        raise ValueError("Wrong input, try again")
    elif player2 is not "paper" and not "rock" and not "scissors":
        raise ValueError("Wrong input, try again")
    elif player1 == player2:
        return 0
    else:
        result.append(player1)
        result.append(player2)
        compare = ','.join(str(i) for i in result)
        return dic[compare]

