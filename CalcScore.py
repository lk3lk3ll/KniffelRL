Ones = 0
Twos = 1
Threes = 2
Fours = 3
Fives = 4
Sixes = 5
ThreeOfKind = 6
FourOfKind = 7
FullHouse = 8
SmallStreet = 9
BigStreet = 10
Kniffel = 11
Chance = 12
CombinationCount = 13




def sumOf(dices, number):
    result = 0
    for i in range(5):
        if dices[i] == number:
            result += number
    if result < 3:
        result = 0
    return result



def totalSum(dices):
    sum = 0
    for i in range(5):
        sum = sum + dices[i]
    return sum



def threeOfAKind(dices):
    if maxCountOfSameKind(dices) >= 3:
        return totalSum(dices)
    else:
        return 0


def fourOfAKind(dices):
    if maxCountOfSameKind(dices) >= 4:
        return totalSum(dices)
    else:
        return 0



def maxCountOfSameKind(dices):
    count = 1
    maxCount = 1
    for i in range(1, 5):
        if dices[i] == dices[i-1]:
            count += 1
            if maxCount < count:
                maxCount = count
        else:
            count = 1
    return maxCount


def fullHouse(dices):
    if dices[0] == dices[1] and dices[3] == dices[4]:
        if (dices[2] == dices[1]) != (dices[2] == dices[3]):
            return 25
        else:
            return 0
    else:
        return 0


def smallStraight(dices):
    count = 1
    for i in range(1, 5):
        diff = (dices[i] - dices[i-1])
        if diff == 1:
            count += 1
            if count == 4:
                return 30
        elif diff >= 2:
            count = 1
    return 0




def largeStraight(dices):
    for i in range(1, 5):
        diff = (dices[i] - dices[i-1])
        if diff != 1:
            return 0
    else:
        return 40


def kniffel(dices):
    if maxCountOfSameKind(dices) == 5:
        return 50
    else:
        return 0


def chance(dices):
    return totalSum(dices)


def calcScore(comb: int, dices: list[int]) -> int:
    dices.sort()
    match comb:
        case 0 | 1 | 2 | 3 | 4 | 5 :
            return sumOf(dices, comb + 1);
        case 6:
            return threeOfAKind(dices);
        case 7:
            return fourOfAKind(dices);
        case 8:
            return fullHouse(dices);
        case 9:
            return smallStraight(dices);
        case 10:
            return largeStraight(dices);
        case 11:
            return kniffel(dices);
        case 12:
            return chance(dices);



