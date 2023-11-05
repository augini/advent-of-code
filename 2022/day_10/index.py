# aoc_template.py

import pathlib
import sys
from collections import defaultdict
import time
import sys


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

    length = len(data)
    X, cycle = 1, 0
    signal_strength = defaultdict(int)

    def update_register(cycle):
        cycle += 1
        if (cycle - 20) % 40 == 0:
            signal_strength[cycle] = X
        return cycle

    for i in range(length):
        parts = data[i].split()

        if parts[0] == "noop":
            cycle = update_register(cycle)

        elif parts[0] == "addx":
            for i in range(2):
                cycle = update_register(cycle)

            X += int(parts[1])

    if parts[0] == "addx":
        update_register(cycle + 1)

    return sum(map(lambda x: x[0] * x[1], signal_strength.items()))


def part2(data):
    """Solve part 2."""

    length = len(data)
    X, cycle = 1, 0
    signal_strength = defaultdict(int)

    def update_register(cycle):
        cycle += 1
        signal_strength[cycle] = X
        return cycle

    for i in range(length):
        parts = data[i].split()

        if parts[0] == "noop":
            cycle = update_register(cycle)

        elif parts[0] == "addx":
            for i in range(2):
                cycle = update_register(cycle)

            X += int(parts[1])

    if parts[0] == "addx":
        update_register(cycle + 1)

    for item in signal_strength.items():
        cycle, register = item[0], item[1]
        if register <= (cycle % 40) and (cycle % 40) <= register + 2:
            sys.stdout.flush()
            time.sleep(0.02)
            print("\033[1;32m#", end=" ")
        else:
            sys.stdout.flush()
            time.sleep(0.02)
            print("\033[91m.", end=" ")

        if cycle % 40 == 0:
            print("")


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
