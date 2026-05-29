import random
from typing import Optional
import torch
import gymnasium as gym

from CalcScore import CombinationCount, calcScore
from OneGame import calcTotalScore


class Dice:
    def __init__(self, value: int):
        self.value = value
        self.chosen = False
        self.free = True

    def __str__(self):
        return str(self.value) if not self.chosen else "-"

class Combination:
    def __init__(self):
        self.free = True
        self.score = 0

    def __str__(self):
        return str(self.score) if not self.free else "-"

class KniffelEnv(gym.Env):
    def __init__(self):
        self.action_space = gym.spaces.Discrete(19) # 1-5 choose dice 6 rethrow 7-19 choose combination
        self.observation_space = gym.spaces.MultiBinary(120)
        self.stage = None
        self.state = None
        self.dices = None

    def get_info(self):
        return " ".join([str(d) for d in self.dices]) + "; " + " ".join([str(c) for c in self.state]) + "; " + str(self.total_score())

    def reset(self, seed: Optional[int] = None, options: Optional[dict] = None):
        super().reset(seed=seed, options=options)
        self.stage = 0
        self.state = [Combination() for i in range(CombinationCount)]
        self.dices = [Dice(random.randint(1, 6)) for i in range(5)]
        return self._get_obs(), self.get_info()

    def _get_obs(self):
        x = torch.zeros(120)
        x[self.stage] = True
        pos = 3
        for dice in self.dices:
            if dice.free:
                x[pos] = 1
            if dice.chosen:
                x[pos + 1] = 1
            else:
                x[pos + 1 + dice.value] = 1
            pos += 8
        for i in range(CombinationCount):
            if not self.state[i].free:
                x[pos + i] = 1
        pos += CombinationCount
        score6 = 0
        for i in range(6):
            score6 += self.state[i].score
        if score6 > 63:
            score6 = 63
        x[pos + score6] = 1
        return x

    def step(self, action):
        assert self.action_space.contains(action)
        if self.stage == 0 or self.stage == 1:
            return self.select_dice(action)
        elif self.stage == 2:
            return self.select_combination(action)
        else:
            raise RuntimeError("oops")

    def invalid_action(self):
        # give a small reward for total score gained so far
        return self._get_obs(), 0.1 * self.total_score(), True, False, self.get_info()

    def valid_action(self):
        # give a small reward for every valid action, in order
        # to train policy to play to an end of the game
        return self._get_obs(), 0.001, False, False, self.get_info()

    def select_dice(self, action):
        if 0 <= action <= 4:
            dice = self.dices[action]
            if dice.chosen or not dice.free:
                return self.invalid_action()
            dice.chosen = True
            return self.valid_action()
        elif action == 5:
            self.stage += 1
            for dice in self.dices:
                if dice.chosen:
                    dice.value = random.randint(1, 6)
                    dice.chosen = False
                else:
                    dice.free = False
            return self.valid_action()
        else:
            return self.invalid_action()

    def select_combination(self, action):
        if 6 <= action <= 18:
            comb = action - 6
            if self.state[comb].free:
                self.state[comb].free = False
                self.state[comb].score = calcScore(comb, [dice.value for dice in self.dices])
                if self.finished():
                    return self._get_obs(), self.total_score(), True, False, self.get_info()
                else:
                    self.stage = 0
                    for dice in self.dices:
                        dice.value = random.randint(1, 6)
                        dice.chosen = False
                        dice.free = True
                    return self.valid_action()
            else:
                return self.invalid_action()
        else:
            return self.invalid_action()

    def total_score(self):
        return calcTotalScore([s.score for s in self.state])

    def free_comb(self):
        cnt = 0
        for s in self.state:
            if s.free:
                cnt += 1
        return cnt

    def finished(self):
        return self.free_comb() == 0
