import sys
from typing import List


def getMinimumPower(games: List[str]) -> int:
    minimumValues = {"red": 0, "green": 0, "blue": 0}

    for game in games:
        pairs = game.split(',')
        pairs = [pair.strip() for pair in pairs]
        for pair in pairs:
            count, color = pair.split(" ")
            count = int(count)
            if count > minimumValues[color]:
                minimumValues[color] = count

    minimumPower = 1
    for count in minimumValues.values():
        minimumPower *= count

    print(games, minimumValues, minimumPower)

    return minimumPower


def getGames(line: str) -> List[str]:
    games = line.split(":")[1]
    games = games.split(";")
    games = [game.strip() for game in games]
    return games


def main(fileName: str) -> None:

    sum = 0

    with open(fileName, "r", encoding="utf-8") as file:
        for line in file:
            # extract list of games
            games = getGames(line)

            # get minimum power
            sum += getMinimumPower(games)

    print(f"sum: {sum}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 solution1.py <file_name>")
        exit(1)

    main(sys.argv[1])
