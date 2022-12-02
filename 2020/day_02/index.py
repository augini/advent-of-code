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
    else:
        return "Freestyle"


def part1(data):
    """Solve part 1."""

    valid = 0

    for i in data:
        items = i.split(":")
        # print(items)
        digits, char = items[0].split(" ")
        _min, _max = digits.split("-")
        # print(digits, char, _min, _max)
        _min, _max = int(_min), int(_max)

        counter = 0
        for c in items[1]:
            if c == char:
                counter += 1
        if _min <= counter <= _max:
            valid += 1
    return valid


def part2(data):
    """Solve part 2."""
    valid = 0
    min_valid, max_valid = False, False

    for i in data:
        items = i.split(":")
        # print(items)
        min_valid, max_valid = False, False
        digits, char = items[0].split(" ")
        _min, _max = digits.split("-")
        # print(digits, char, _min, _max)
        _min, _max = int(_min), int(_max)

        for i in range(len(items[1])):
            if items[1][i] == char:

                if i == _min:
                    if not min_valid:
                        min_valid = True
                    else:
                        continue

                if i == _max:
                    if not max_valid:
                        max_valid = True
                    else:
                        continue
        if (min_valid and not max_valid) or (max_valid and not min_valid):
            valid += 1

    return valid


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
