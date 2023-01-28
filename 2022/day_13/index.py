# aoc_template.py

import pathlib
import sys
from collections import deque
import json


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
    i = 0
    groups = []
    valid_indices = []

    for i in range(0, len(data) - 1, 3):
        temp = []

        temp.append(deque(json.loads(data[i])))
        temp.append(deque(json.loads(data[i + 1])))

        groups.append(temp)

    index = 1
    for group in groups:
        print(group[0], group[1])

        while group[0] and group[1]:
            left, right = group[0].popleft(), group[1].popleft()

            if isinstance(left, int) and isinstance(right, int):
                print(left, right)
                if left == right:
                    """"""
                elif left < right:
                    valid_indices.append(index)
                    break
                elif left > right:
                    break

            elif isinstance(left, list) and isinstance(right, list):
                print(left, right)

        index += 1

        print(valid_indices)
    return sum(valid_indices)


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
