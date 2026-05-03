import random

from Player import Player

class BaselinePlayer(Player):
    prob = 0.1

    def chooseDice1(self, state: list[bool], dices: list[int]) -> list[bool]:
        ret = []
        for i in range(5):
            rethrow = random.random() < self.prob
            ret.append(rethrow)

    def chooseDice2(self, state: list[bool], dices: list[int], freeDices: list[bool]) -> list[bool]:
        ret = []
        for i in range(5):
            rethrow = freeDices[i] and random.random() < self.prob
            ret.append(rethrow)

    def chooseCombination(self, state: list[bool], dices: list[int]) -> int:
        max = -1
        bestChoice = None
        for i in range(14):
            if state[i]:
                score = self.calcScore(i, dices)
                if score > max:
                    max = score
                    bestChoice = i
        return bestChoice