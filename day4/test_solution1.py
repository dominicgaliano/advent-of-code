import unittest
from solution1 import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        self.solution.loadData("test-input")

    def test_getWinningNumbers(self):
        self.assertEqual(self.solution.getWinningNumbers(
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"), {41, 48, 83, 86, 17})

    def test_getCardNumbers(self):
        self.assertEqual(self.solution.getCardNumbers(
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"), [83, 86, 6, 31, 17, 9, 48, 53])

    def test_getGamePoints(self):
        self.assertEqual(self.solution.getGamePoints(
            {41, 48, 83, 86, 17}, [83, 86, 6, 31, 17, 9, 48, 53]), 8)

    def test_getSolution(self):
        self.assertEqual(self.solution.getSolution(), 13)


if __name__ == '__main__':
    unittest.main()
