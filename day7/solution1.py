import sys


class Solution:

    hexMap = {"2": 0x2, "3": 0x3, "4": 0x4, "5": 0x5, "6": 0x6, "7": 0x7,
              "8": 0x8, "9": 0x9, "T": 0xA, "J": 0xB, "Q": 0xC, "K": 0xD, "A": 0xE}

    def __init__(self):
        self.data = []

    def loadData(self, filePath: str) -> None:
        with open(filePath, "r", encoding="utf-8") as file:
            lines = list(file)
            self.data = [tuple(line.strip().split(" ")) for line in lines]

    def getHandType(self, hand: str) -> int:
        # Hand types represented as an int from 0 - 6 with 0 being the
        # worst hand (high card) and 6 being the best hand (five of a kind)
        counts = dict()
        for card in hand:
            if card not in counts:
                counts[card] = 1
                continue
            counts[card] += 1

        # TODO: Come up with better solution here
        values = set(counts.values())
        if 5 in values:
            return 6
        if 4 in values:
            return 5
        if values == set([3, 2]):
            return 4
        if 3 in values:
            return 3
        if sorted(list(counts.values())) == [1, 2, 2]:
            return 2
        if 2 in values:
            return 1
        return 0

    def convertHandToHex(self, hand: str) -> int:
        handType = self.getHandType(hand)
        handValue = handType
        for card in hand:
            handValue = handValue * 16 + self.hexMap[card]

        return handValue

    def calculateWinnings(self, sortedHands: list) -> list:
        winnings = []
        for i, position in enumerate(sortedHands):
            winnings.append(int(position[1]) * (i + 1))
        return winnings

    def getSolution(self) -> int:
        # sort hands by strength
        sortedHands = sorted(
            self.data, key=lambda hand: self.convertHandToHex(hand[0]))

        # calculate winnings based on hand order
        winnings = self.calculateWinnings(sortedHands)

        # return sum
        return sum(winnings)


def main() -> None:

    if len(sys.argv) != 2:
        print("Usage: python3 solution1.py <file_name>")
        exit(1)

    solution = Solution()
    solution.loadData(sys.argv[1])
    print(solution.getSolution())


if __name__ == "__main__":
    main()
