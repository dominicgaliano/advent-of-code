import sys
import re
from functools import reduce


class Solution:

    def __init__(self):
        self.data = []

    def loadData(self, filePath: str) -> None:
        with open(filePath, "r", encoding="utf-8") as file:
            self.data = list(file)

    def getWinningNumbers(self, game: str) -> list:
        return set(map(int, re.findall(r'(\d+)(?![^\r\n:]*\:)(?=[^\r\n]*\|)', game)))

    def getCardNumbers(self, game: str) -> set:
        return list(map(int, re.findall(r'(\d+)(?![^\r\n|]*\|)', game)))

    def getGamePoints(self, winningNumbers: set, cardNumbers: list) -> int:

        def reducer(points, cardNumber):
            if cardNumber in winningNumbers:
                if points == 0:
                    return 1
                return points * 2
            return points

        return reduce(reducer, cardNumbers, 0)

    def getSolution(self) -> int:
        sum = 0
        for line in self.data:
            winningNumbers = self.getWinningNumbers(line)
            cardNumbers = self.getCardNumbers(line)
            sum += self.getGamePoints(winningNumbers, cardNumbers)

        return sum


def main() -> None:

    if len(sys.argv) != 2:
        print("Usage: python3 solution1.py <file_name>")
        exit(1)

    solution = Solution()
    solution.loadData(sys.argv[1])
    print(solution.getSolution())


if __name__ == "__main__":
    main()
