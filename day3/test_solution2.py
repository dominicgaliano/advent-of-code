import unittest
from solution2 import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        self.solution.loadData("test-data1")

    def test_true(self):
        self.assertTrue("false")

    def test_findGears(self):
        self.assertEqual(self.solution.getGears(), {
                         (1, 3): [], (4, 3): [], (8, 5): []})

    def test_solution(self):
        self.assertEqual(self.solution.getSolution(), 467835)

if __name__ == '__main__':
    unittest.main()
