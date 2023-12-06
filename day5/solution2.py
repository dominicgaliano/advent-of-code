import sys
import re


class Solution:

    def __init__(self):
        self.data = []

    def loadData(self, filePath: str) -> None:
        with open(filePath, "r", encoding="utf-8") as file:
            self.data = list(file)

            # remove empty lines and \n
            self.data = list(filter(lambda elem: elem, map(
                lambda elem: elem.strip(), self.data)))

    def getSeeds(self) -> set:
        seeds = set()
        pairs = list((match.group())
                     for match in re.finditer(r"\d+\s\d+", self.data[0]))

        for pair in pairs:
            start, rang = map(int, pair.split(' '))

            for n in range(start, start + rang):
                seeds.add(n)

        return seeds

    def getMaps(self) -> dict:
        maps = []
        currentMap = []
        for line in self.data[1:]:
            if re.search(r"map", line):
                # save map
                if currentMap:
                    maps.append(currentMap)

                currentMap = []
                continue

            x, y, z = map(
                lambda elem: int(elem.group()), re.finditer(r"\d+", line))

            currentMap.append((x, y, z))

        maps.append(currentMap)
        return maps

    def getLocation(self, seed: int, maps: list) -> int:
        next = seed
        for map in maps:
            for mapEntry in map:
                dest, source, rnge = mapEntry
                if next >= source and next < source + rnge:
                    next = dest + (next - source)
                    break

        return next

    def getSolution(self) -> int:
        seeds = self.getSeeds()
        maps = self.getMaps()
        return min([self.getLocation(seed, maps) for seed in seeds])


def main() -> None:

    if len(sys.argv) != 2:
        print("Usage: python3 solution2.py <file_name>")
        exit(1)

    solution = Solution()
    solution.loadData(sys.argv[1])
    print(solution.getSolution())


if __name__ == "__main__":
    main()
