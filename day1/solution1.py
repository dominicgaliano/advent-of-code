import sys


def main(fileName: str) -> None:

    sum = 0

    with open(fileName, "r", encoding="utf-8") as file:
        for line in file:
            first, last = 0, 0

            for char in line:
                if char.isnumeric():
                    first = int(char)
                    break

            for char in reversed(line):
                if char.isnumeric():
                    last = int(char)
                    break

            sum += (10 * first + last)

    print(f"sum: {sum}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 solution1.py <file_name>")
        exit(1)

    main(sys.argv[1])
