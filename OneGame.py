import random

for step in range(14):
    dices = []
    for i in range(5):
        dice = random.randint(1, 6)
        dices.append(dice)
    print(dices)

