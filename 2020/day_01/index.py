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
    else:
        return "Freestyle"


def part1(data, number):
    """Solve part 1."""
    _dict = defaultdict(int)

    for i in data:
        curr = int(i)
        if curr in list(_dict.values()):
            return curr * (number - curr)
        else:
            _dict[curr] = number - curr
    return False


def part2(data):
    """Solve part 2."""

    for i in data:
        curr = int(i)
        res = part1(data, (2020 - curr))

        if res:
            return curr * res
    return False


def solve(puzzle_input):
    # Solve the puzzle for the given input.

    # parse the given input
    data = parse(puzzle_input, 2)

    # get the solutions for each problem
    solution1 = part1(data, 2020)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    #  print(sys.argv)
    for path in sys.argv[1:]:
        #   print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
