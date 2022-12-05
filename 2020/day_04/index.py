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

    validator = {
        "byr": False,
        "iyr": False,
        "eyr": False,
        "hgt": False,
        "hcl": False,
        "ecl": False,
        "pid": False,
    }
    data.append("")

    for item in data:
        if item != "":
            parts = item.split(" ")
            for p in parts:
                pieces = p.split(":")
                if pieces[0] != "cid":
                    validator[pieces[0]] = True
        else:
            if all(value == True for value in validator.values()) == True:
                valid += 1
            validator = {key: False for key in validator}

    return valid


def part2(data):
    """Solve part 2."""
    valid = 0

    validator = {
        "byr": False,
        "iyr": False,
        "eyr": False,
        "hgt": False,
        "hcl": False,
        "ecl": False,
        "pid": False,
    }
    data.append("")

    for item in data:
        if item != "":
            parts = item.split(" ")
            for p in parts:
                pieces = p.split(":")
                if pieces[0] != "cid":
                    validator[pieces[0]] = True
        else:
            if all(value == True for value in validator.values()) == True:
                valid += 1
            validator = {key: False for key in validator}

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
