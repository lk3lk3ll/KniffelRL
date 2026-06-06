import unittest
from CalcScore import calcScore, Ones, ThreeOfKind, FourOfKind, FullHouse, SmallStreet, BigStreet, Kniffel, Chance, \
    Threes, Twos, Sixes


class TestCalcScore(unittest.TestCase):
    def testSumOf(self):
        self.assertEqual(5, calcScore(Ones, [1, 1, 1, 1, 1]))
        self.assertEqual(3, calcScore(Ones, [1, 2, 1, 3, 1]))
        self.assertEqual(0, calcScore(Ones, [1, 3, 1, 3, 2]))
        self.assertEqual(0, calcScore(Ones, [2, 3, 1, 3, 2]))
        self.assertEqual(0, calcScore(Threes, [2, 3, 2, 3, 2]))
        self.assertEqual(0, calcScore(Twos, [3, 2, 3, 2, 3]))
        self.assertEqual(0, calcScore(Sixes, [6, 2, 3, 2, 3]))
        self.assertEqual(9, calcScore(Threes, [3, 2, 3, 2, 3]))

    def testThreeOfAKind(self):
        self.assertEqual(17,calcScore(ThreeOfKind,[5, 5, 5, 1, 1]))
        self.assertEqual(0,calcScore(ThreeOfKind,[2, 5, 5, 1, 1]))
        self.assertEqual(15,calcScore(ThreeOfKind,[3, 5, 3, 1, 3]))
        self.assertEqual(0, calcScore(ThreeOfKind, [3, 5, 2, 1, 4]))

    def testFourOfAKind(self):
        self.assertEqual(21, calcScore(FourOfKind, [5, 5, 5, 1, 5]))
        self.assertEqual(0, calcScore(FourOfKind, [2, 5, 5, 1, 1]))
        self.assertEqual(15, calcScore(FourOfKind, [3, 3, 3, 3, 3]))

    def testFullHouse(self):
        self.assertEqual(25, calcScore(FullHouse, [2, 5, 5, 2, 5]))
        self.assertEqual(0, calcScore(FullHouse, [5, 5, 5, 5, 5]))
        self.assertEqual(0, calcScore(FullHouse, [3, 3, 1, 3, 3]))
        self.assertEqual(0, calcScore(FullHouse, [3, 3, 1, 2, 2]))

    def testSmallStreet(self):
        self.assertEqual(30, calcScore(SmallStreet, [4, 3, 5, 2, 4]))
        self.assertEqual(0, calcScore(SmallStreet, [5, 5, 5, 5, 5]))
        self.assertEqual(0, calcScore(SmallStreet, [1, 2, 1, 3, 3]))
        self.assertEqual(0, calcScore(SmallStreet, [3, 3, 1, 2, 2]))

    def testBigStreet(self):
            self.assertEqual(40, calcScore(BigStreet, [4, 3, 5, 2, 6]))
            self.assertEqual(0, calcScore(BigStreet, [5, 5, 5, 5, 5]))
            self.assertEqual(0, calcScore(BigStreet, [1, 1, 2, 3, 4]))
            self.assertEqual(0, calcScore(BigStreet, [1, 2, 4, 6, 3]))
            self.assertEqual(0, calcScore(BigStreet, [3, 3, 1, 3, 3]))

    def testKniffel(self):
        self.assertEqual(50, calcScore(Kniffel, [5, 5, 5, 5, 5]))
        self.assertEqual(0, calcScore(Kniffel, [2, 5, 5, 1, 1]))
        self.assertEqual(0, calcScore(Kniffel, [3, 3, 3, 2, 3]))

    def testChance(self):
        self.assertEqual(21, calcScore(Chance, [5, 5, 5, 1, 5]))
        self.assertEqual(14, calcScore(Chance, [2, 5, 5, 1, 1]))
        self.assertEqual(15, calcScore(Chance, [3, 3, 3, 3, 3]))

if __name__ == '__main__':
    unittest.main()
