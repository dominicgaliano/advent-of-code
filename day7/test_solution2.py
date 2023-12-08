import unittest
from solution2 import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        self.solution.loadData("test-input")

    def test_getHandType(self):
        self.assertEqual(self.solution.getHandType("23456"), 0)  # high card
        self.assertEqual(self.solution.getHandType("32TJK"), 1)  # one pair
        self.assertEqual(self.solution.getHandType("K67K6"), 2)  # two pair
        self.assertEqual(self.solution.getHandType("5J523"), 3)  # three of a kind 
        self.assertEqual(self.solution.getHandType("2332J"), 4)  # full house
        self.assertEqual(self.solution.getHandType("23J23"), 4)  # full house
        self.assertEqual(self.solution.getHandType("AAAJ2"), 5)  # four of a kind
        self.assertEqual(self.solution.getHandType("JJJJJ"), 6)  # five of a kind
        self.assertEqual(self.solution.getHandType("JJJAA"), 6)  # five of a kind

    def test_convertHandToHex(self):
        self.assertEqual(self.solution.convertHandToHex("23456"), 0x023456)  # high card
        self.assertEqual(self.solution.convertHandToHex("32T3K"), 0x132a3d)  # one pair
        self.assertEqual(self.solution.convertHandToHex("KK677"), 0x2dd677)  # two pair
        self.assertEqual(self.solution.convertHandToHex("T55J5"), 0x5a5515)  # four of a kind

    def test_calculateWinnings(self):
        self.assertEqual(self.solution.calculateWinnings(
            [('32T3K', '765'), ('T55J5', '684'), ('KK677', '28'), ('KTJJT', '220'), ('QQQJA', '483')]), [765, 684*2, 28*3, 220*4, 483*5])

    def test_getSolution(self):
        self.assertEqual(self.solution.getSolution(), 5905)


if __name__ == '__main__':
    unittest.main()
