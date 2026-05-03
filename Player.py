from abc import ABC, abstractmethod

# description of function arguments
# state: list of 13 booleans, stating if we already have a score on that position
# true is a free space
# dices: the 5 dices with values from 1-6
# freeDices: list of 5 boolean values
# True means you can rethrow

class Player(ABC):
    @abstractmethod
    def chooseDice1(self, state: list[bool], dices: list[int]) -> list[bool]:
        pass

    @abstractmethod
    def chooseDice2(self, state: list[bool], dices: list[int], freeDices: list[bool]) -> list[bool]:
        pass

    @abstractmethod
    def chooseCombination(self, state: list[bool], dices: list[int]) -> int:
        pass
