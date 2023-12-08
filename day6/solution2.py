import sys
import re
import math


class Solution:

    def __init__(self):
        self.data = []

    def loadData(self, filePath: str) -> None:
        with open(filePath, "r", encoding="utf-8") as file:
            data = list(file)
            times = list((m.group()) for m in re.finditer(r"\d+", data[0]))
            distances = list((m.group())
                             for m in re.finditer(r"\d+", data[1]))
            self.data = [(int("".join(times)), int("".join(distances)))]

    def getRaceSolution(self, pair: tuple) -> int:
        total_t = pair[0]
        distance_record = pair[1]
        root1 = (-total_t + (total_t ** 2 - 4 * distance_record) ** 0.5) / -2
        root2 = (-total_t - (total_t ** 2 - 4 * distance_record) ** 0.5) / -2
        return math.ceil(root2 - 1) - math.floor(root1)

    def getSolution(self) -> int:
        return math.prod(self.getRaceSolution(pair) for pair in self.data)


def main() -> None:

    if len(sys.argv) != 2:
        print("Usage: python3 solution2.py <file_name>")
        exit(1)

    solution = Solution()
    solution.loadData(sys.argv[1])
    print(solution.getSolution())


if __name__ == "__main__":
    main()


# speed = button_t
# distance = speed * (total_t - button_t)
# find button_t such that distance > distance_record
# solve: button_t * (total_t - button_t) > distance_record
#        x = button_t now
#        x ** 2 - total_t * x + distance_record < 0
#        roots = (-total_t +- (total_t ** 2 - 4 * distance_record) ** 0.5) / -2
