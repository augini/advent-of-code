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


def part1(data):
    """Solve part 1."""
    coor_y = defaultdict(int)
    coor_x = defaultdict(int)

    _min, _max = math.inf, -math.inf

    for item in data:
        parts = item.strip().split(":")
        pieces = parts[1].split(" ")

        y = int(pieces[-1].split("=")[-1])
        x = int(pieces[-2].split("=")[-1].split(",")[-2])
        _x = int(parts[0].split(" ")[-2].split(",")[0].split("=")[-1])

        if min(x, _x) < _min:
            _min = min(x, _x)
        if max(x, _x) > _max:
            _max = max(x, _x)

        coor_y[(x, y)] += 1
        coor_x[x] += 1

    temp = 0
    for keys in coor_y:
        # print(keys[1])
        if keys[1] == 2000000:
            temp += 1

    return (abs(_min) + abs(_max)) - temp


def part2(data):
    """Solve part 2."""


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
