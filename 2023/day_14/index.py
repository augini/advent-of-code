# aoc_template.py

import pathlib
import sys
from collections import defaultdict


def parse(puzzle_input, type=1, seperator="\n"):
    # Parses the input

    #  print(puzzle_input)
    if type == 1:
        return list(puzzle_input.split())
    elif type == 2:
        return list(puzzle_input.split(seperator))
    elif type == 3:
        return list(puzzle_input.strip().split(seperator))


def part1(data):
    """Solve part 1."""
    clubs = []
    rounds = []

    length = len(data)

    for ind, line in enumerate(data):
        for i, char in enumerate(line):
            if char == "#":
                clubs.append((ind, i))
            elif char == "O":
                rounds.append((ind, i))

    for i, round in enumerate(rounds):
        y, x = round[0], round[1]
        while True:
            if y == 0:
                break

            if (y - 1, x) not in rounds and (y - 1, x) not in clubs:
                y = y - 1
            else:
                break
        rounds[i] = (y, x)

    sm = 0
    for item in rounds:
        sm += length - item[0]
    return sm


def part2(data):
    """Solve part 2."""
    clubs = []
    rounds = []

    length = len(data)

    for ind, line in enumerate(data):
        for i, char in enumerate(line):
            if char == "#":
                clubs.append((ind, i))
            elif char == "O":
                rounds.append((ind, i))

    hashes = set()

    steps = 0
    billion = 1000000000

    while steps <= billion:
        # tilt north
        for i, round in enumerate(rounds):
            y, x = round[0], round[1]
            while True:
                if y == 0:
                    break

                if (y - 1, x) not in rounds and (y - 1, x) not in clubs:
                    y = y - 1
                else:
                    break
            rounds[i] = (y, x)

        # tilt west
        for i, round in enumerate(rounds):
            y, x = round[0], round[1]
            while True:
                if x == 0:
                    break

                if (y, x - 1) not in rounds and (y, x - 1) not in clubs:
                    x = x - 1
                else:
                    break
            rounds[i] = (y, x)

        # tilt south
        for i, round in enumerate(rounds):
            y, x = round[0], round[1]
            while True:
                if y == length - 1:
                    break

                if (y + 1, x) not in rounds and (y + 1, x) not in clubs:
                    y = y + 1
                else:
                    break
            rounds[i] = (y, x)

        # tilt east
        for i, round in enumerate(rounds):
            y, x = round[0], round[1]
            while True:
                if x == len(data[0]) - 1:
                    break

                if (y, x + 1) not in rounds and (y, x + 1) not in clubs:
                    x = x + 1
                else:
                    break
            rounds[i] = (y, x)

        if set(rounds) in hashes:
            for ind, item in enumerate(hashes):
                if set(rounds) == item:
                    print(ind, steps)
                    diff = steps - ind
                    print(diff)
                    while steps < billion:
                        if steps + diff < billion:
                            steps = steps + diff
                        else:
                            break
                    print(steps)
                    break
            break
        else:
            hashes.add(frozenset(rounds))
        steps += 1

    sm = 0
    for item in rounds:
        sm += length - item[0]
    return sm


def solve(puzzle_input):
    # Solve the puzzle for the given input.
    # parse the given input
    data = parse(puzzle_input, 2)

    # get the solutions for each problem
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    #  print(sys.argv)
    for path in sys.argv[1:]:
        #   print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
