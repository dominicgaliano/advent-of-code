import sys


class Solution:

    hexMap = {"J": 0x1, "2": 0x2, "3": 0x3, "4": 0x4, "5": 0x5, "6": 0x6,
              "7": 0x7, "8": 0x8, "9": 0x9, "T": 0xA, "Q": 0xC, "K": 0xD,
              "A": 0xE}

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
        wildcardCount = 0
        for card in hand:
            if card == "J":
                wildcardCount += 1
                continue
            if card not in counts:
                counts[card] = 1
                continue
            counts[card] += 1

        values = list(counts.values())
        # five-of-a-kind
        # possible ways: AAAAA or AAAAJ or AAAJJ or AAJJJ or AJJJJ or JJJJJ
        if not values or len(values) == 1:
            return 6
        # four-of-a-kind
        # possible ways: AAAA2 or AAAJ2 or AAJJ2 or AJJJ2
        if max(values) + wildcardCount == 4:
            return 5
        # full house
        # possible ways: AAAKK, AAKKJ (can't have two or more  J ever, would go to better hand)
        if len(values) == 2:
            return 4
        # three of a kind:
        # possible ways: AAA23, AA23J, A23JJ (can't have three J as above)
        if max(values) + wildcardCount == 3:
            return 3
        # two pairs
        # possible ways: AA223  (must come naturally)
        if len(values) == 3:
            return 2
        # one pair
        if len(values) == 4:
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
        print("Usage: python3 solution2.py <file_name>")
        exit(1)

    solution = Solution()
    solution.loadData(sys.argv[1])
    print(solution.getSolution())


if __name__ == "__main__":
    main()
