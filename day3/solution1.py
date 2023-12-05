import sys


class Solution:
    invalid_characters = "1234567890."
    digits = "1234567890"

    def __init__(self):
        self.data = []

    def loadData(self, filePath: str) -> None:
        with open(filePath, "r", encoding="utf-8") as file:
            for line in file:
                self.data.append([*line.strip()])

    def peek(self):
        print(self.data)

    def hasAdjacentSymbol(self, row, col):
        maxRow, maxCol = len(self.data), len(self.data[0])
        for row_offset in range(-1, 2):
            for col_offset in range(-1, 2):
                calc_row, calc_col = row + row_offset, col + col_offset
                if calc_row > -1 and calc_row < maxRow and calc_col > -1 and calc_col < maxCol:
                    if self.data[calc_row][calc_col] not in self.invalid_characters:
                        return True

        return False

    def getValidNumbers(self) -> None:
        validNumbers = []
        currentNumberString = ""
        hasAdjacentSymbol = False

        for row, line in enumerate(self.data):
            for col, char in enumerate(line):
                if col == 0 or char not in self.digits:
                    # add to valid numbers if constraints met
                    if hasAdjacentSymbol and currentNumberString:
                        validNumbers.append(int(currentNumberString))

                    # reset variables
                    currentNumberString = ""
                    hasAdjacentSymbol = False

                if char in self.digits:
                    currentNumberString += char
                    hasAdjacentSymbol = hasAdjacentSymbol or self.hasAdjacentSymbol(
                        row, col)

        # check if last cells were valid numbers
        # TODO: eliminate duplicated code
        if hasAdjacentSymbol and currentNumberString:
            validNumbers.append(int(currentNumberString))

        return validNumbers

    def getSolution(self) -> int:
        return sum(self.getValidNumbers())

    def __str__(self):
        outputString = ""
        for line in self.data:
            outputString += "".join(line)
            outputString += "\n"
        return outputString.strip()


def main() -> None:

    if len(sys.argv) != 2:
        print("Usage: python3 solution1.py <file_name>")
        exit(1)

    solution = Solution()
    solution.loadData(sys.argv[1])
    print(solution.getValidNumbers())
    print(solution.getSolution())


if __name__ == "__main__":
    main()
