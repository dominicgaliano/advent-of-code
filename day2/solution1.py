import sys
import re
from typing import List

REGEX_QUERY = r"(?<=Game\s)\d+"
gamePattern = re.compile(REGEX_QUERY)

maxValues = {"red": 12, "green": 13, "blue": 14}


def validGame(game: str) -> bool:
    pairs = game.split(',')
    pairs = [pair.strip() for pair in pairs]
    for pair in pairs:
        count, color = pair.split(" ")
        count = int(count)
        if count > maxValues[color]:
            return False

    return True


def getGameNumber(line: str) -> int:
    match = gamePattern.search(line)
    if not match:
        raise Exception("Invalid input syntax")

    return int(match.group())


def getGames(line: str) -> List[str]:
    games = line.split(":")[1]
    games = games.split(";")
    games = [game.strip() for game in games]
    return games


def main(fileName: str) -> None:

    sum = 0

    with open(fileName, "r", encoding="utf-8") as file:
        for line in file:
            # extract game number
            gameNumber = getGameNumber(line)

            # extract list of games
            games = getGames(line)

            # evaluate feasibility
            if all(map(validGame, games)):
                # add to sum if feasible
                sum += gameNumber

    print(f"sum: {sum}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 solution1.py <file_name>")
        exit(1)

    main(sys.argv[1])
