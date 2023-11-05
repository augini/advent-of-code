# aoc_template.py

import pathlib
import sys
from collections import defaultdict
import math


def parse(puzzle_input, type=1, seperator="\n"):
    # Parses the input

    #  print(puzzle_input)
    if type == 1:
        return list(puzzle_input.split())
    elif type == 2:
        return list(puzzle_input.split(seperator))
    elif type == 3:
        return list(puzzle_input.strip().split(seperator))


def get_rocks(coors):
    rocks = set()

    for item in coors:
        parts = item.split("->")
        prev = parts[0]

        for i in range(1, len(parts)):
            prev, curr = prev.strip().split(","), parts[i].strip().split(",")

            for x in range(2):
                prev[x], curr[x] = int(prev[x]), int(curr[x])

            x1, y1 = prev
            x2, y2 = curr

            if x1 == x2:
                _min = min(y1, y2)
                _max = max(y1, y2)

                for y in range(_min, _max + 1):
                    rocks.add((x1, y))

            if y1 == y2:
                _min = min(x1, x2)
                _max = max(x1, x2)

                for y in range(_min, _max + 1):
                    rocks.add((y, y1))
            prev = parts[i]
    return rocks


def part1(data):
    """Solve part 1."""
    # create the lines that include rocks
    rocks = get_rocks(data)

    # get the bottom of the floow as the row that has the lowest coor
    bottom = max(r[1] for r in rocks)

    sands, count = set(), 0

    while count < 1000:
        count += 1
        sand = (500, 0)

        while True:
            if sand[1] > bottom:
                return count - 1
            if (sand[0], sand[1] + 1) not in rocks and (
                sand[0],
                sand[1] + 1,
            ) not in sands:
                sand = (sand[0], sand[1] + 1)
            elif (sand[0] - 1, sand[1] + 1) not in rocks and (
                sand[0] - 1,
                sand[1] + 1,
            ) not in sands:
                sand = (sand[0] - 1, sand[1] + 1)
            elif (sand[0] + 1, sand[1] + 1) not in rocks and (
                sand[0] + 1,
                sand[1] + 1,
            ) not in sands:
                sand = (sand[0] + 1, sand[1] + 1)
            else:
                break
        sands.add(sand)

    return 1


def part2(data):
    """Solve part 2."""
    # create the lines that include rocks
    rocks = get_rocks(data)

    # get the bottom of the floow as the row that has the lowest coor
    bottom = max(r[1] for r in rocks) + 2

    left = min(r[0] for r in rocks) - 500
    right = max(r[0] for r in rocks) + 500

    for x in range(left, right):
        rocks.add((x, bottom))

    sands = set()
    count = 0
    while count < 100000:
        count += 1
        sand = (500, 0)
        while True:
            if (sand[0], sand[1] + 1) not in rocks and (
                sand[0],
                sand[1] + 1,
            ) not in sands:
                sand = (sand[0], sand[1] + 1)
            elif (sand[0] - 1, sand[1] + 1) not in rocks and (
                sand[0] - 1,
                sand[1] + 1,
            ) not in sands:
                sand = (sand[0] - 1, sand[1] + 1)
            elif (sand[0] + 1, sand[1] + 1) not in rocks and (
                sand[0] + 1,
                sand[1] + 1,
            ) not in sands:
                sand = (sand[0] + 1, sand[1] + 1)
            else:
                break
        if sand == (500, 0):
            return count
        sands.add(sand)

    return 1


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
