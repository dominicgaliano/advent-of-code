import sys
import re

STRING_NUMBERS = ["one", "two", "three", "four",
                  "five", "six", "seven", "eight", "nine"]

stringNumbers = dict()
for i, stringNumber in enumerate(STRING_NUMBERS):
    stringNumbers[stringNumber] = i + 1


def asInteger(input: str | int) -> int:
    return int(input) if input.isnumeric() else stringNumbers[input]


def main(fileName: str) -> None:

    REGEX_QUERY = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"
    prog = re.compile(REGEX_QUERY)

    sum = 0

    with open(fileName, "r", encoding="utf-8") as file:
        for line in file:
            result = prog.findall(line)
            first = asInteger(result[0])
            last = asInteger(result[-1])
            sum += (10 * first + last)

    print(f"sum: {sum}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 solution2.py <file_name>")
        exit(1)

    main(sys.argv[1])
