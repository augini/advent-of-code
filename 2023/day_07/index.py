# aoc_template.py

import pathlib
import sys
from collections import defaultdict, Counter


def parse(puzzle_input, type=1, seperator="\n"):
    # Parses the input
    if type == 1:
        return list(puzzle_input.split())
    elif type == 2:
        return list(puzzle_input.split(seperator))
    elif type == 3:
        return list(puzzle_input.strip().split(seperator))


def part1(data):
    """Solve part 1."""
    hands = defaultdict(list)

    for line in data:
        hand, bid = line.split(" ")
        if len(hand) == len(set(hand)):
            hands["five"].append(hand)
        c = Counter(hand)
        print(c)


def part2(data):
    """Solve part 1."""


def solve(puzzle_input):
    # parse the given input
    data = parse(puzzle_input, 2)

    # get the solutions for each problem
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
