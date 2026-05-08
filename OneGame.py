import random
from operator import ifloordiv

from Player import Player
from BaselinePlayer import BaselinePlayer
from CalcScore import calcScore, CombinationCount

def calcTotalScore(scores):
    total = 0
    for i in range(6):
        total += scores[i]
    if total >= 63:
        total += 35
    for i in range(6,13):
        total += scores[i]
    return total


def PlayGame(player: Player, doPrint: bool):
    state = [True for i in range(CombinationCount)]
    score = [0 for i in range(CombinationCount)]
    for step in range(CombinationCount):
        dices = [random.randint(1, 6) for i in range(5)]
        if doPrint:
            print("Step ", (step + 1), ", dices=", dices)
        rethrow1 = player.chooseDice1(state, dices)
        if doPrint:
            print("Step ", (step + 1), ", rethrow1=", rethrow1)
        for i in range(5):
            if rethrow1[i]:
                dices[i] = random.randint(1, 6)
        if doPrint:
            print("Step ", (step + 1), ", dices=", dices)
        rethrow2 = player.chooseDice2(state, dices, rethrow1)
        if doPrint:
            print("Step ", (step + 1), ", rethrow2=", rethrow2)
        for i in range(5):
            if rethrow2[i]:
                if not rethrow1[i]:
                    raise RuntimeError("Invalid action")
                dices[i] = random.randint(1, 6)
        if doPrint:
            print("Step ", (step + 1), ", dices=", dices)
        comb = player.chooseCombination(state, dices)
        if not state[comb]:
            raise RuntimeError("Invalid action")
        state[comb] = False
        score[comb] = calcScore(comb, dices)
        if doPrint:
            print("Combination ", comb, ", score=", score[comb])
    total = calcTotalScore(score)
    if doPrint:
        print("Total score=", total)
    return total

def PrintGame(player: Player):
    PlayGame(player, doPrint=True)

def EvaluateGame(player: Player):
    return     PlayGame(player, doPrint=False)

if __name__ == '__main__':
    PrintGame(BaselinePlayer())
