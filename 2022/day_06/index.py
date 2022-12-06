# aoc_template.py

import pathlib
import sys
from collections import Counter


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

    result = ""

    for char in data[0]:
        if len(list(Counter(result[-4:]))) >= 4:
            break
        result += char

    return len(result)


def part2(data):
    """Solve part 2."""

    result = ""
    for char in data[0]:
        if len(list(Counter(result[-14:]))) >= 14:
            break
        result += char

    return len(result)


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
