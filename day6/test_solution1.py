import unittest
from solution1 import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        self.solution.loadData("test-input")

    def test_getSolution(self):
        self.assertEqual(self.solution.getSolution(), 288)


if __name__ == '__main__':
    unittest.main()
