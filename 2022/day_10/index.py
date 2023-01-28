# aoc_template.py

import pathlib
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

    cycle = 0
    add_x = 1

    signal_strengths = []
    for item in data:
        parts = item.split(" ")

        if parts[0] == "addx":
            add_x += int(parts[1])
            c = 2
            for i in range(2):
                if cycle in [20, 60, 100, 140, 180, 220]:
                    temp = cycle * add_x
                    signal_strengths.append(temp)

                cycle += 1
        else:
            c = 1

        for i in range(c):
            if cycle in [20, 60, 100, 140, 180, 220]:
                temp = cycle * add_x
                signal_strengths.append(temp)

            cycle += 1

    print(signal_strengths)


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
