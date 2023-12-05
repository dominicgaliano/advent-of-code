import unittest
from solution1 import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        self.solution.loadData("test-data1")

    def test_str_method(self):
        self.assertEqual(str(self.solution), """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""")

    def test_solution(self):
        self.assertEqual(self.solution.getSolution(), 4361)

    # def test_peek(self):
    #     self.solution.peek()

    def test_hasAdjacentSymbol(self):
        self.assertFalse(self.solution.hasAdjacentSymbol(0, 0))
        self.assertFalse(self.solution.hasAdjacentSymbol(9, 0))
        self.assertTrue(self.solution.hasAdjacentSymbol(2, 6))
        self.assertTrue(self.solution.hasAdjacentSymbol(2, 5))
        self.assertTrue(self.solution.hasAdjacentSymbol(2, 4))

    def test_getValidNumbers(self):
        self.assertEqual(self.solution.getValidNumbers(), [
                         467, 35, 633, 617, 592, 755, 664, 598])


if __name__ == '__main__':
    unittest.main()
