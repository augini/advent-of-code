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
    races = defaultdict(int)

    times = data[0].split("Time:")[1].split(" ")
    times = [int(x) for x in times if len(x)]

    distances = data[1].split("Distance:")[1].split(" ")
    distances = [int(x) for x in distances if len(x)]

    length = len(times)

    for i in range(length):
        # print(times[i], distances[i])
        for j in range(times[i] + 1):
            remaining = times[i] - j
            distance = remaining * j
            if distance > distances[i]:
                races[i] += 1

    return math.prod(races.values())


def part2(data):
    """Solve part 2."""
    races = defaultdict(int)

    times = data[0].split("Time:")[1].split(" ")
    times = [int("".join(times))]

    distances = data[1].split("Distance:")[1].split(" ")
    distances = [int("".join(distances))]

    length = len(times)

    for i in range(length):
        for j in range(times[i] + 1):
            remaining = times[i] - j
            distance = remaining * j
            if distance > distances[i]:
                races[i] += 1

    return math.prod(races.values())


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
