import unittest
from solution1 import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        self.solution.loadData("test-input")

    def test_getSeeds(self):
        self.assertEqual(self.solution.getSeeds(), {79, 14, 55, 13})

    def test_getLocation(self):
        maps = self.solution.getMaps()
        self.assertEqual(self.solution.getLocation(79, maps), 82)
        self.assertEqual(self.solution.getLocation(14, maps), 43)
        self.assertEqual(self.solution.getLocation(55, maps), 86)
        self.assertEqual(self.solution.getLocation(13, maps), 35)

    def test_getSolution(self):
        self.assertEqual(self.solution.getSolution(), 35)


if __name__ == '__main__':
    unittest.main()
