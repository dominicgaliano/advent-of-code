import sys
import re
import math

# algorithm:
# 1. find all gears (*)
# 2. Iterate through grid, find numbers
# 3. For each number found, check determine which cells are adjacent
# 4. Check adjacent cells for gears
# 5. For any gear found, add the current number to that gears list
# 6. After grid fully iterated through, calculate final solution according to
#    problem criteria.


class Solution:
    def __init__(self):
        self.data = []

    def loadData(self, filePath: str) -> None:
        with open(filePath, "r", encoding="utf-8") as file:
            self.data = list(file)

    def getGears(self):
        return {(r, c): [] for r in range(len(self.data))
                for c in range(len(self.data[0])-1) if self.data[r][c] == "*"}

    def getSolution(self) -> int:
        gears = self.getGears()

        for r, row in enumerate(self.data):
            for n in re.finditer(r'\d+', row):
                edge = {(r, c) for r in (r-1, r, r+1)
                        for c in range(n.start()-1, n.end() + 1)}

                for o in edge & gears.keys():
                    gears[o].append(int(n.group()))

        return sum(math.prod(p) for p in gears.values() if len(p) == 2)


def main() -> None:

    if len(sys.argv) != 2:
        print("Usage: python3 solution2.py <file_name>")
        exit(1)

    solution = Solution()
    solution.loadData(sys.argv[1])
    print(solution.getSolution())


if __name__ == "__main__":
    main()
