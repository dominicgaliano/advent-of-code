import sys


class Solution:

    def __init__(self):
        self.data = []

    def loadData(self, filePath: str) -> None:
        with open(filePath, "r", encoding="utf-8") as file:
            self.data = list(file)

    def getSolution(self) -> int:
        return 0


def main() -> None:

    if len(sys.argv) != 2:
        print("Usage: python3 solution1.py <file_name>")
        exit(1)

    solution = Solution()
    solution.loadData(sys.argv[1])
    print(solution.getSolution())


if __name__ == "__main__":
    main()
