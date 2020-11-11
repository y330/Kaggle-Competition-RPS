# author: avivy
# created: 11/09/2020
# modified: 11/09/2020
"""
using method from http://datagenetics.com/blog/march52013/index.html

monte-carlo."""

import random
import numpy as np


def AI():
    return random.choice([0, 1, 2])


def round_pick():
    selection = random.choices(opponents, k=2)
    return selection


def get_results(sample):
    global log, wins, shifted, matrix, times
    for i in range(3):
        # matrix.rotate(1)
        matrix = list(np.roll(matrix, 1))
        # matrix = list(matrix)[::2]
        if sample == matrix[1::]:
            times[sample[0]] += 1
            wins.append(C[sample[0]])
            log.append(sample)
            opponents.remove(sample[1])
            pass


"""the follwing reperesents the possible outcome, starting from R(0): S(2) P(1) R(0). the winning outcome(the one we care about) is the first 2 indices in each row for each hand:
    0(R)  210
    1(P)  021
    2(S)  102
"""
matrix = [2, 1, 0]  # r: [win(s), lose(p), tier)]
# matrix = collections.deque(matrix)  # convert to deque to cycle
log = []
wins = []
times = [0, 0, 0]
C = ["rock", "paper", "scissors"]
rounds = 0
game_length = []
opponents = [AI() for i in range(50)]


# while len(opponents) < 10:
#     opponents.append(AI())
# print(opponents)
def game():
    global rounds
    while len(opponents) > 1:
        rounds += 1
        get_results(round_pick())
    game_length.append(rounds)


for i in range(129):
    game()
    # for (i,j) in zip(wins, log):
    #     print(i,j)
    cc = {i: C[i] for i in range(3)}
    # print([[wins[i],log[i]] for i in range(len(log))])

avrgame = np.average(game_length)

print(avrgame)
