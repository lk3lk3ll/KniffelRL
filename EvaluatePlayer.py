from BaselinePlayer import BaselinePlayer
from OneGame import EvaluateGame
from Player import Player


def CalcStatistic(player: Player):
    sum = 0
    for i in range(1000):
        sum += EvaluateGame(player)
    return sum / 1000


if __name__ == '__main__':
    print( "Average Score:" + str(CalcStatistic(BaselinePlayer())))



